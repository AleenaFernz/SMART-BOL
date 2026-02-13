import hashlib  # built-in cryptographic library


def generate_sha256(file_bytes: bytes) -> str:
    """
    Generates SHA-256 hash of uploaded file bytes.
    Returns 0x-prefixed hexadecimal string
    compatible with Solidity bytes32.
    """

    sha256 = hashlib.sha256()
    sha256.update(file_bytes)  # feeds file content into hashing algorithm

    hash_hex = sha256.hexdigest()

    # Prefix with 0x for Solidity compatibility
    return "0x" + hash_hex
