import json
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

RPC_URL = os.getenv("RPC_URL")
CONTRACT_ADDRESS = os.getenv("BOL_CONTRACT_ADDRESS")

if not RPC_URL or not CONTRACT_ADDRESS:
    raise Exception("Missing RPC_URL or BOL_CONTRACT_ADDRESS in .env")

# Connect to blockchain
w3 = Web3(Web3.HTTPProvider(RPC_URL))

if not w3.is_connected():
    raise Exception("Failed to connect to blockchain RPC")

# Load ABI
ABI_PATH = os.path.join(
    os.path.dirname(__file__),
    "abi",
    "contract_abi.json"
)

with open(ABI_PATH) as f:
    ABI = json.load(f)

contract = w3.eth.contract(
    address=Web3.to_checksum_address(CONTRACT_ADDRESS),
    abi=ABI
)

def anchor_bol_hash(bol_hash_hex: str) -> str:
    """
    Anchors a BoL hash on the blockchain.
    Returns transaction hash.
    """
    tx = contract.functions.mint(
        w3.eth.accounts[0],
        bytes.fromhex(bol_hash_hex.replace("0x", ""))
    ).transact({
        "from": w3.eth.accounts[0]
    })

    receipt = w3.eth.wait_for_transaction_receipt(tx)
    return receipt.transactionHash.hex()
