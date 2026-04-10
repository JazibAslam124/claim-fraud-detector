import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID     = os.getenv("CAMUNDA_CLIENT_ID")
CLIENT_SECRET = os.getenv("CAMUNDA_CLIENT_SECRET")
CLUSTER_ID    = os.getenv("CAMUNDA_CLUSTER_ID")
REGION        = os.getenv("CAMUNDA_REGION")

def get_token():
    response = requests.post(
        "https://login.cloud.camunda.io/oauth/token",
        data={
            "grant_type":    "client_credentials",
            "client_id":     CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "audience":      "zeebe.camunda.io"
        }
    )
    return response.json()["access_token"]

def start_process(claim: dict, fraud_score: int):
    print(f"\n🔁 Starting Camunda process...")
    print(f"   Claim ID:     {claim['claim_id']}")
    print(f"   Fraud Score:  {fraud_score}")
    print(f"   Claim Amount: ${claim['claim_amount']}")

    token = get_token()

    url = f"https://{REGION}.zeebe.camunda.io:443/{CLUSTER_ID}/v2/process-instances"

    payload = {
        "processDefinitionId": "Process_1vksbz2",
        "variables": {
            "fraudScore": fraud_score,
            "claimAmount": claim["claim_amount"],
            "claimId": claim["claim_id"]
        }
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type":  "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        if fraud_score > 80:
            decision = "Reject"
        elif claim["claim_amount"] > 10000:
            decision = "Manual Review"
        else:
            decision = "Approve"
        print(f"   Decision: ✅ {decision}")
        print(f"   Camunda Instance: {response.json().get('processInstanceKey')}")
        return decision
    else:
        print(f"   ❌ Camunda error: {response.status_code} — {response.text}")
        return None