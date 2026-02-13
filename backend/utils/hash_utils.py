import hashlib #built-in cryptographic library

def generate_sha256(file_bytes: bytes) -> str:    #function accepts raw file bytes
    """
    Generates SHA-256 hash of uploaded file bytes.
    Returns hexadecimal string.
    """

    sha256 = hashlib.sha256()
    sha256.update(file_bytes)  #feeds file content into hashing algorithm
    return sha256.hexdigest()