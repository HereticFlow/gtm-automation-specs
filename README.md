# Workflow Specification: Automated Lead Routing (Make.com)

This document outlines a live, working scenario built in Make.com that processes incoming leads via a Webhook, evaluates their quality using a router, and routes them to the correct sales channel via Gmail.

## 1. Architecture
- **Trigger (Webhook):** Receives a JSON payload with lead data (Name, Company, Size, Role).
- **Scoring Router:** Splits the flow into two paths based on lead quality.
  - **Path A (Hot Leads):** If `role` contains "VP", "Head", or "CEO". Sends an immediate alert to the Senior AE via Gmail.
  - **Path B (Cold Leads):** Fallback for all other leads. Sends an email for the Marketing Nurture sequence.
- **Data Mapping:** Extracts the `first_name` and `company` from the Webhook payload to personalize the email subject and body dynamically.

## 2. Live Proof (Execution)
I tested this scenario locally using `curl` to send POST requests to the Make webhook.

### Test 1: Hot Lead (Executive)
**Payload sent:**
```json
{"first_name": "Alice", "company": "TechCorp", "role": "VP Sales"}

<img width="681" height="164" alt="Capture d’écran 2026-10-22 à 02 31 06" src="https://github.com/user-attachments/assets/5c90155a-7f46-4212-90b7-9ac958fb3b7f" />
