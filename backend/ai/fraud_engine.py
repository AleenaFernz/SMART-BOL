from datetime import datetime


# ------------------------
# Configurable Risk Weights
# ------------------------

RISK_WEIGHTS = {
    "missing_bol_number": 30,
    "missing_container_id": 20,
    "missing_date": 15,
    "invalid_date": 15,
    "missing_weight": 15,
    "unrealistic_weight": 25,
    "missing_ports": 15,
    "invalid_vessel": 10,
}

FRAUD_THRESHOLD = 50


# ------------------------
# Fraud Scoring Function
# ------------------------

def calculate_fraud_score(parsed_data: dict) -> dict:
    """
    Takes parsed Bill of Lading fields
    Returns fraud score and flags
    """

    score = 0
    flags = []

    # 1️⃣ Bill of Lading number check
    if not parsed_data.get("bill_of_lading_no"):
        score += RISK_WEIGHTS["missing_bol_number"]
        flags.append("Missing Bill of Lading number")

    # 2️⃣ Container ID check
    if not parsed_data.get("container_id"):
        score += RISK_WEIGHTS["missing_container_id"]
        flags.append("Missing container ID")

    # 3️⃣ Date validation
    shipped_date = parsed_data.get("shipped_on_date")
    if not shipped_date:
        score += RISK_WEIGHTS["missing_date"]
        flags.append("Missing shipment date")
    else:
        try:
            parsed_date = datetime.strptime(shipped_date, "%d/%m/%Y")
            if parsed_date > datetime.now():
                score += RISK_WEIGHTS["invalid_date"]
                flags.append("Shipment date is in the future")
        except ValueError:
            score += RISK_WEIGHTS["invalid_date"]
            flags.append("Invalid date format")

    # 4️⃣ Cargo weight validation
    weight = parsed_data.get("cargo_weight")
    if not weight:
        score += RISK_WEIGHTS["missing_weight"]
        flags.append("Missing cargo weight")
    else:
        try:
            numeric_weight = float(weight.replace(",", ""))
            if numeric_weight <= 0 or numeric_weight > 200000:
                score += RISK_WEIGHTS["unrealistic_weight"]
                flags.append("Unrealistic cargo weight")
        except ValueError:
            score += RISK_WEIGHTS["unrealistic_weight"]
            flags.append("Invalid cargo weight format")

    # 5️⃣ Port presence check
    if not parsed_data.get("port_of_loading") or not parsed_data.get("port_of_destination"):
        score += RISK_WEIGHTS["missing_ports"]
        flags.append("Missing port information")

    # 6️⃣ Vessel plausibility check
    vessel = parsed_data.get("vessel")
    if vessel and len(vessel) < 3:
        score += RISK_WEIGHTS["invalid_vessel"]
        flags.append("Suspicious vessel name")

    # ------------------------
    # Final Decision
    # ------------------------

    mint_allowed = score < FRAUD_THRESHOLD

    return {
        "fraud_score": score,
        "flags": flags,
        "mint_allowed": mint_allowed
    }
