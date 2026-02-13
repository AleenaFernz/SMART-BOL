SMART-BOL+
AI-Verified, Blockchain-Enforced Bill of Lading System
📌 Problem

In international trade, Bills of Lading (BoL) are:

Often paper-based or PDF documents

Legally powerful documents of title

Used as collateral in trade finance

Relied upon by ports, banks, insurers

Fraud occurs when:

Duplicate BoLs are issued

Forged BoLs secure multiple financings

Ownership disputes arise at ports

Multiple parties claim the same cargo

Banks and institutions have lost billions due to duplicate or fraudulent Bills of Lading.

There is no globally trusted, singular digital ownership registry.

💡 Core Solution

SMART-BOL+ separates verification from enforcement.

AI verifies authenticity and structural consistency of a BoL

Only verified documents are allowed to proceed

Blockchain mints a Digital Bill of Lading NFT

NFT represents digital ownership of cargo

Ownership transfer occurs only via smart contract

Immutable ledger prevents duplicate ownership

🔐 Core Principle

AI protects the blockchain from lies.
Blockchain protects AI decisions from denial.

🏗 High-Level Architecture

User → Backend → AI Verification → Mint Gate → Smart Contract → Blockchain

Source of Truth:

Ownership → Blockchain

Verification → AI risk scoring logic

⚙️ Tech Stack
Backend

FastAPI (Python)

SHA-256 hashing

In-memory duplicate detection (demo scope)

AI Layer

Tesseract OCR

Format-based structured parsing

Weighted fraud scoring engine

Blockchain

Solidity

ERC-721 NFT

Hardhat

Polygon / Ethereum testnet

Frontend

React

MetaMask integration

🧠 AI Verification Pipeline

SMART-BOL+ performs layered verification before minting.

Step-by-Step Flow

User uploads Bill of Lading

Backend generates SHA-256 document hash

Duplicate hash detection (AI layer)

OCR extracts raw document text

Structured fields are parsed using format-based detection

Weighted fraud scoring evaluates anomalies

Minting allowed only if fraud_score < threshold

📊 Fraud Scoring Logic

Fraud detection is weighted and configurable.

Examples of checks:

Missing Bill of Lading number

Missing container ID

Missing or invalid shipment date

Future shipment date

Unrealistic cargo weight

Missing port information

Suspicious vessel name

Duplicate document hash

Fraud score threshold determines mint eligibility.

Duplicate documents are blocked before blockchain interaction.

🔁 Duplicate Protection

SMART-BOL+ prevents duplicate ownership at two layers:

AI Layer – Duplicate SHA-256 hash detection

Blockchain Layer – Smart contract prevents duplicate documentHash minting

This ensures layered defense against duplicate issuance.

📦 API Response Example
{
  "document_hash": "4ae495558934b6f42f2e16fa27db6e2ea2417eba2937839ec9cea39d9eeadcd8",
  "parsed_fields": {
    "bill_of_lading_no": "ZIMUCOK6014947",
    "container_id": null,
    "shipped_on_date": "18/09/2017",
    "cargo_weight": "34,710.00",
    "vessel": "VOV",
    "port_of_loading": "...",
    "port_of_destination": "..."
  },
  "fraud_score": 20,
  "flags": ["Missing container ID"],
  "mint_allowed": true
}

📌 Current Status

✔ Backend architecture complete
✔ SHA-256 hashing implemented
✔ OCR extraction integrated
✔ Structured field parsing operational
✔ Weighted fraud scoring engine active
✔ Duplicate document hash protection enabled
✔ Mint gating logic implemented

Next Phase: Smart contract integration and NFT mint enforcement.

🚀 Hackathon Scope

This system:

Does NOT:

Replace shipping companies

Guarantee physical cargo existence

Eliminate all fraud

It DOES:

Prevent duplicate digital ownership

Reduce probability of forged documents

Enforce single on-chain ownership

Create immutable audit trail

Introduce AI-based pre-mint verification

📁 Project Structure
backend/
│
├── main.py
├── requirements.txt
│
├── ai/
│   ├── ocr.py
│   ├── parser.py
│   └── fraud_engine.py
│
├── utils/
│   ├── hash_utils.py
│   └── hash_registry.py

🧭 Future Improvements

Carrier-specific parsing models

Named Entity Recognition for ports

Database-backed duplicate detection

Multi-node distributed hash registry

Trade finance integration

On-chain verification metadata anchoring

🏁 Vision

SMART-BOL+ aims to introduce probabilistic AI verification before deterministic blockchain enforcement.

A layered trust architecture for international trade documentation.