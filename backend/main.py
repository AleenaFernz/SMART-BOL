from fastapi import FastAPI, UploadFile, File
from utils.hash_utils import generate_sha256

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
