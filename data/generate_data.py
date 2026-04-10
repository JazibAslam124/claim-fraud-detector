# import pandas as pd
# import numpy as np
#
# np.random.seed(42)
# n = 500
#
# df = pd.DataFrame({
#     "claim_id":          range(1, n+1),
#     "claim_amount":      np.random.randint(500, 50000, n),
#     "customer_age":      np.random.randint(18, 80, n),
#     "num_claims_past":   np.random.randint(0, 10, n),
#     "days_since_policy": np.random.randint(1, 3650, n),
#     "is_fraud":          np.random.choice([0, 1], n, p=[0.85, 0.15])
# })
#
# df.to_csv("claims.csv", index=False)
# print(f"✅ Generated {n} claims — {df['is_fraud'].sum()} fraudulent")


import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

claim_amount      = np.random.randint(500, 50000, n)
customer_age      = np.random.randint(18, 80, n)
num_claims_past   = np.random.randint(0, 10, n)
days_since_policy = np.random.randint(1, 3650, n)

# Fraud is more likely when:
# - many past claims
# - policy is very new
# - high claim amount
fraud_score = (
    (num_claims_past >= 7).astype(int) * 0.5 +
    (days_since_policy <= 30).astype(int) * 0.3 +
    (claim_amount >= 30000).astype(int) * 0.2
)
is_fraud = (fraud_score + np.random.uniform(0, 0.3, n) > 0.5).astype(int)

df = pd.DataFrame({
    "claim_id":          range(1, n+1),
    "claim_amount":      claim_amount,
    "customer_age":      customer_age,
    "num_claims_past":   num_claims_past,
    "days_since_policy": days_since_policy,
    "is_fraud":          is_fraud
})

df.to_csv("claims.csv", index=False)
print(f"✅ Generated {n} claims — {df['is_fraud'].sum()} fraudulent")