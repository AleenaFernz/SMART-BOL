import re
from typing import Optional


def parse_bol_fields(text: str) -> dict:
    """
    Parses OCR text of a Bill of Lading and extracts
    high-confidence structured fields using format-based detection.

    This parser:
    - Avoids fragile block extraction
    - Uses pattern scanning instead of strict layout assumptions
    - Focuses on fraud-relevant fields
    """

    cleaned_text = text.replace("\r", " ")

    # ------------------------
    # Helper Functions
    # ------------------------

    def find_first(pattern: str) -> Optional[str]:
        match = re.search(pattern, cleaned_text, re.IGNORECASE)
        return match.group(1).strip() if match else None

    def find_all(pattern: str):
        return re.findall(pattern, cleaned_text, re.IGNORECASE)

    # ------------------------
    # 1️⃣ Bill of Lading Number
    # Format-based: 8–20 alphanumeric, must contain letters & digits
    # ------------------------

    candidates = find_all(r"\b[A-Z0-9]{8,20}\b")

    bill_of_lading_no = None
    for c in candidates:
        if re.search(r"[A-Z]", c) and re.search(r"\d", c):
            bill_of_lading_no = c
            break

    # ------------------------
    # 2️⃣ Container ID (4 letters + 7 digits)
    # ------------------------

    container_id = find_first(r"\b([A-Z]{4}\d{7})\b")

    # ------------------------
    # 3️⃣ Date (dd/mm/yyyy)
    # ------------------------

    shipped_on_date = find_first(r"\b(\d{2}/\d{2}/\d{4})\b")

    # ------------------------
    # 4️⃣ Cargo Weight (decimal numbers like 34,710.00)
    # ------------------------

    cargo_weight = find_first(r"\b([\d,]+\.\d+)\b")

    # ------------------------
    # 5️⃣ Vessel (look after keyword VESSEL)
    # ------------------------

    vessel = find_first(r"VESSEL\W*[:\-]?\s*([A-Z0-9]+)")

    # ------------------------
    # 6️⃣ Port Detection (basic uppercase location detection)
    # We look for patterns like "COCHIN, INDIA"
    # ------------------------

    port_candidates = find_all(r"\b([A-Z\s]+,\s*[A-Z\s]+)\b")

    port_of_loading = None
    port_of_destination = None

    if port_candidates:
        port_of_loading = port_candidates[0]
        if len(port_candidates) > 1:
            port_of_destination = port_candidates[1]

    # ------------------------
    # Final Parsed Output
    # ------------------------

    return {
        "bill_of_lading_no": bill_of_lading_no,
        "container_id": container_id,
        "shipped_on_date": shipped_on_date,
        "cargo_weight": cargo_weight,
        "vessel": vessel,
        "port_of_loading": port_of_loading,
        "port_of_destination": port_of_destination,
    }
