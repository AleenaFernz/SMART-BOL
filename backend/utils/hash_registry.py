"""
In-memory registry for verified document hashes.
For hackathon demo purposes only.
"""

VERIFIED_HASHES = set()


def is_duplicate(document_hash: str) -> bool:
    return document_hash in VERIFIED_HASHES


def register_hash(document_hash: str):
    VERIFIED_HASHES.add(document_hash)
