# import pandas as pd
# from pyexpat import features
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report
# import pickle
#
# def train():
#     df= pd.read_csv("data/claims.csv")
#
#     features = ["claim_amount", "customer_age", "num_claims_past", "days_since_policy"]
#     X = df[features]
#     y = df["is_fraud"]
#
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
#
#     model = RandomForestClassifier(n_estimators = 100, random_state = 42)
#     model.fit(X_train, y_train)
#
#     y_pred = model.predict(X_test)
#     print("Model trained")
#     print(classification_report(y_test, y_pred))
#
#     with open("model.pk1", "wb") as f:
#         pickle.dump(model, f)
#     print("Model saved to model.pk1")
#
#     return model
#
# def load():
#     with open("model.pk1", "rb") as f:
#         return pickle.load(f)
#
# def predict_fraud_score(claim: dict) -> int:
#     model = load()
#     features = [[
#         claim["claim_amount"],
#         claim["customer_age"],
#         claim["num_claims_past"],
#         claim["days_since_policy"]
#     ]]
#     proba = model.predict_proba(features)[0][1]
#     score = int(proba * 100)
#     return score
#
# if __name__ == "__main__":
#     train()
#
#


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

def train():
    df = pd.read_csv("data/claims.csv")

    features = ["claim_amount", "customer_age", "num_claims_past", "days_since_policy"]
    X = df[features]
    y = df["is_fraud"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("✅ Model trained!")
    print(classification_report(y_test, y_pred))

    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("✅ Model saved to model.pkl")

    return model

def load():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

def predict_fraud_score(claim: dict) -> int:
    model = load()
    features = pd.DataFrame([{
        "claim_amount":      claim["claim_amount"],
        "customer_age":      claim["customer_age"],
        "num_claims_past":   claim["num_claims_past"],
        "days_since_policy": claim["days_since_policy"]
    }])
    proba = model.predict_proba(features)[0][1]
    score = int(proba * 100)
    return score

if __name__ == "__main__":
    train()