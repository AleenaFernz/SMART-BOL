from fastapi import FastAPI, UploadFile, File
from utils.hash_utils import generate_sha256
from ai.ocr import extract_text_from_image
from ai.parser import parse_bol_fields
from ai.fraud_engine import calculate_fraud_score
from utils.hash_registry import is_duplicate, register_hash
from blockchain.client import anchor_bol_hash



app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "SMART-BOL+ Backend Running"}


@app.post("/upload-bol")
async def upload_bol(file: UploadFile = File(...)):
    """
    Accepts a Bill of Lading file.
    Generates SHA-256 hash.
    Returns document hash.
    """

    file_bytes = await file.read()   #reads entire file into memory as bytes. This is what we hash

    document_hash = generate_sha256(file_bytes)

    return {
        "filename": file.filename,
        "document_hash": document_hash
    }

@app.post("/ocr-test")
async def ocr_test(file: UploadFile = File(...)):
    file_bytes = await file.read()
    text = extract_text_from_image(file_bytes)

    return {
        "extracted_text": text
    }

@app.post("/parse-test")
async def parse_test(file: UploadFile = File(...)):
    file_bytes = await file.read()

    text = extract_text_from_image(file_bytes)
    parsed = parse_bol_fields(text)

    return parsed


@app.post("/verify-bol")
async def verify_bol(file: UploadFile = File(...)):
    file_bytes = await file.read()

    document_hash = generate_sha256(file_bytes)

    # 🔴 Duplicate Detection (AI layer protection)
    if is_duplicate(document_hash):
        return {
            "document_hash": document_hash,
            "parsed_fields": None,
            "fraud_score": 100,
            "flags": ["Duplicate document detected"],
            "mint_allowed": False,
            "blockchain_tx": None
        }

    # Continue AI verification
    text = extract_text_from_image(file_bytes)
    parsed = parse_bol_fields(text)
    fraud_result = calculate_fraud_score(parsed)

    blockchain_tx = None

    # If safe → register hash + anchor on blockchain
    if fraud_result["mint_allowed"]:
        register_hash(document_hash)

        # 🔗 Blockchain anchoring (NEW)
        blockchain_tx = anchor_bol_hash(document_hash)

    return {
        "document_hash": document_hash,
        "parsed_fields": parsed,
        "fraud_score": fraud_result["fraud_score"],
        "flags": fraud_result["flags"],
        "mint_allowed": fraud_result["mint_allowed"],
        "blockchain_tx": blockchain_tx
    }


