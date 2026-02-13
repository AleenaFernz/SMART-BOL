import pytesseract
from PIL import Image
import io

# Explicitly define Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(file_bytes: bytes) -> str:
    """
    Takes image bytes.
    Returns extracted text using Tesseract OCR.
    """

    image = Image.open(io.BytesIO(file_bytes))

    text = pytesseract.image_to_string(image)

    return text.strip()
