from model import predict_fraud_score
from camunda import start_process

claims = [
    {
        "claim_id": 1,
        "claim_amount": 5000,
        "customer_age": 35,
        "num_claims_past": 8,
        "days_since_policy": 30
    },
    {
        "claim_id": 2,
        "claim_amount": 15000,
        "customer_age": 45,
        "num_claims_past": 1,
        "days_since_policy": 1200
    },
    {
        "claim_id": 3,
        "claim_amount": 3000,
        "customer_age": 55,
        "num_claims_past": 0,
        "days_since_policy": 2000
    },
    {
        "claim_id": 4,
        "claim_amount": 2000,
        "customer_age": 22,
        "num_claims_past": 9,
        "days_since_policy": 5
    }

]

print("=" * 45)
print("   INSURANCE CLAIM FRAUD DETECTION SYSTEM")
print("=" * 45)

for claim in claims:
    fraud_score = predict_fraud_score(claim)
    decision = start_process(claim, fraud_score)
    print(f"   → Claim {claim['claim_id']} processed: {decision}")
    print("-" * 45)