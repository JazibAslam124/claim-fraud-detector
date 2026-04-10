# import streamlit as st
# import pandas as pd
# import time
# from model import predict_fraud_score
# from camunda import start_process
#
# st.set_page_config(
#     page_title="Insurance Claim Fraud Detector",
#     page_icon="🔍",
#     layout="wide"
# )
#
# st.title("🔍 Insurance Claim Fraud Detection System")
# st.markdown("*Powered by Random Forest ML + Camunda Process Automation*")
# st.markdown("---")
#
# # ── Sample claims for batch processing ──────────────────────
# SAMPLE_CLAIMS = [
#     {"claim_id": 1, "claim_amount": 5000,  "customer_age": 35, "num_claims_past": 8, "days_since_policy": 12},
#     {"claim_id": 2, "claim_amount": 15000, "customer_age": 45, "num_claims_past": 1, "days_since_policy": 1200},
#     {"claim_id": 3, "claim_amount": 3000,  "customer_age": 55, "num_claims_past": 0, "days_since_policy": 2000},
#     {"claim_id": 4, "claim_amount": 2000,  "customer_age": 22, "num_claims_past": 9, "days_since_policy": 5},
#     {"claim_id": 5, "claim_amount": 8000,  "customer_age": 60, "num_claims_past": 2, "days_since_policy": 800},
# ]
#
# # ── Layout ───────────────────────────────────────────────────
# col_left, col_right = st.columns([1, 1])
#
# with col_left:
#     st.subheader("⚡ Batch Processing")
#     st.caption("Automatically processes all claims through the ML model and triggers Camunda routing")
#
#     if st.button("▶ Run Batch Processing", use_container_width=True, type="primary"):
#         results = []
#         feed = st.empty()
#
#         for claim in SAMPLE_CLAIMS:
#             with feed.container():
#                 st.markdown(f"**⚡ Processing Claim #{claim['claim_id']}...**")
#                 st.markdown(f"Amount: `${claim['claim_amount']:,}` | Age: `{claim['customer_age']}` | Past Claims: `{claim['num_claims_past']}`")
#
#                 prog = st.progress(0)
#                 for i in range(100):
#                     time.sleep(0.01)
#                     prog.progress(i + 1)
#
#                 fraud_score = predict_fraud_score(claim)
#                 decision = start_process(claim, fraud_score)
#
#                 if fraud_score > 80:
#                     score_color = "🔴"
#                     risk = "HIGH RISK"
#                 elif fraud_score > 40:
#                     score_color = "🟡"
#                     risk = "MEDIUM RISK"
#                 else:
#                     score_color = "🟢"
#                     risk = "LOW RISK"
#
#                 decision_emoji = {"Reject": "❌", "Manual Review": "⚠️", "Approve": "✅"}.get(decision, "❓")
#
#                 st.markdown(f"Fraud Score: **{fraud_score}/100** {score_color} `{risk}`")
#                 st.markdown(f"Decision: {decision_emoji} **{decision}**")
#                 st.markdown("---")
#
#                 results.append({
#                     "Claim ID": claim["claim_id"],
#                     "Amount ($)": f"${claim['claim_amount']:,}",
#                     "Fraud Score": fraud_score,
#                     "Risk": risk,
#                     "Decision": f"{decision_emoji} {decision}"
#                 })
#
#                 time.sleep(0.5)
#
#         feed.empty()
#         st.success(f"✅ Batch complete — {len(results)} claims processed")
#         st.session_state["results"] = results
#
# with col_right:
#     st.subheader("🧾 Single Claim Analysis")
#     st.caption("Manually enter claim details to analyse a single claim")
#
#     with st.form("single_claim"):
#         c1, c2 = st.columns(2)
#         with c1:
#             amount = st.number_input("Claim Amount ($)", min_value=100, max_value=100000, value=5000, step=500)
#             age = st.number_input("Customer Age", min_value=18, max_value=100, value=35)
#         with c2:
#             past = st.number_input("Past Claims", min_value=0, max_value=20, value=2)
#             days = st.number_input("Days Since Policy", min_value=1, max_value=3650, value=365)
#
#         submitted = st.form_submit_button("Analyse Claim", use_container_width=True)
#
#         if submitted:
#             claim = {
#                 "claim_id": 99,
#                 "claim_amount": amount,
#                 "customer_age": age,
#                 "num_claims_past": past,
#                 "days_since_policy": days
#             }
#
#             with st.spinner("Scoring fraud risk..."):
#                 fraud_score = predict_fraud_score(claim)
#                 decision = start_process(claim, fraud_score)
#
#             if fraud_score > 80:
#                 st.error(f"🔴 Fraud Score: {fraud_score}/100 — HIGH RISK")
#             elif fraud_score > 40:
#                 st.warning(f"🟡 Fraud Score: {fraud_score}/100 — MEDIUM RISK")
#             else:
#                 st.success(f"🟢 Fraud Score: {fraud_score}/100 — LOW RISK")
#
#             decision_emoji = {"Reject": "❌", "Manual Review": "⚠️", "Approve": "✅"}.get(decision, "❓")
#             st.metric("Decision", f"{decision_emoji} {decision}")
#
#             bar_val = fraud_score / 100
#             st.progress(bar_val)
#
# st.markdown("---")
#
# # ── Results table ────────────────────────────────────────────
# st.subheader("📋 Claims Processed This Session")
#
# if "results" in st.session_state and st.session_state["results"]:
#     df = pd.DataFrame(st.session_state["results"])
#     st.dataframe(df, use_container_width=True, hide_index=True)
#
#     total = len(df)
#     approved = len([r for r in st.session_state["results"] if "Approve" in r["Decision"]])
#     rejected = len([r for r in st.session_state["results"] if "Reject" in r["Decision"]])
#     manual = len([r for r in st.session_state["results"] if "Manual" in r["Decision"]])
#
#     m1, m2, m3, m4 = st.columns(4)
#     m1.metric("Total Processed", total)
#     m2.metric("✅ Approved", approved)
#     m3.metric("❌ Rejected", rejected)
#     m4.metric("⚠️ Manual Review", manual)
# else:
#     st.caption("Run batch processing or analyse a single claim to see results here.")
#
# st.markdown("---")
# st.caption("Built with Python · scikit-learn · Camunda Cloud · Streamlit")


import streamlit as st
import pandas as pd
import time
import os
from model import predict_fraud_score, train

st.set_page_config(
    page_title="Insurance Claim Fraud Detector",
    page_icon="🔍",
    layout="wide"
)

# Auto-train model if not found
if not os.path.exists("model.pkl"):
    with st.spinner("Training fraud detection model..."):
        train()

st.title("🔍 Insurance Claim Fraud Detection System")
st.markdown("*Powered by Random Forest ML + Camunda BPMN Process Automation*")
st.markdown("---")

# ── Sample claims ────────────────────────────────────────────
SAMPLE_CLAIMS = [
    {"claim_id": 1, "claim_amount": 5000, "customer_age": 35, "num_claims_past": 8, "days_since_policy": 12},
    {"claim_id": 2, "claim_amount": 15000, "customer_age": 45, "num_claims_past": 1, "days_since_policy": 1200},
    {"claim_id": 3, "claim_amount": 3000, "customer_age": 55, "num_claims_past": 0, "days_since_policy": 2000},
    {"claim_id": 4, "claim_amount": 2000, "customer_age": 22, "num_claims_past": 9, "days_since_policy": 5},
    {"claim_id": 5, "claim_amount": 8000, "customer_age": 60, "num_claims_past": 2, "days_since_policy": 800},
]


def get_decision(fraud_score, claim_amount):
    if fraud_score > 80:
        return "Reject"
    elif claim_amount > 10000:
        return "Manual Review"
    else:
        return "Approve"


def show_bpmn_routing(fraud_score, claim_amount, decision):
    st.markdown("**⚙️ Camunda BPMN Process Routing:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        if fraud_score > 80:
            st.error("🔴 Fraud Score > 80\nTriggered → YES")
        else:
            st.success("🟢 Fraud Score > 80\nTriggered → NO")
    with col2:
        if fraud_score <= 80:
            if claim_amount > 10000:
                st.warning("🟡 Claim > $10,000\nTriggered → YES")
            else:
                st.success("🟢 Claim > $10,000\nTriggered → NO")
        else:
            st.empty()
    with col3:
        if decision == "Reject":
            st.error("❌ Outcome: REJECT")
        elif decision == "Manual Review":
            st.warning("⚠️ Outcome: MANUAL REVIEW")
        else:
            st.success("✅ Outcome: APPROVE")


# ── Layout ───────────────────────────────────────────────────
col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("⚡ Batch Processing")
    st.caption("Automatically processes all claims through the ML model and routes via BPMN logic")

    if st.button("▶ Run Batch Processing", use_container_width=True, type="primary"):
        results = []
        feed = st.empty()

        for claim in SAMPLE_CLAIMS:
            with feed.container():
                st.markdown(f"**⚡ Processing Claim #{claim['claim_id']}...**")
                st.markdown(
                    f"Amount: `${claim['claim_amount']:,}` | Age: `{claim['customer_age']}` | Past Claims: `{claim['num_claims_past']}`")

                prog = st.progress(0)
                for i in range(100):
                    time.sleep(0.008)
                    prog.progress(i + 1)

                fraud_score = predict_fraud_score(claim)
                decision = get_decision(fraud_score, claim["claim_amount"])

                if fraud_score > 80:
                    score_color = "🔴"
                    risk = "HIGH RISK"
                elif fraud_score > 40:
                    score_color = "🟡"
                    risk = "MEDIUM RISK"
                else:
                    score_color = "🟢"
                    risk = "LOW RISK"

                decision_emoji = {
                    "Reject": "❌",
                    "Manual Review": "⚠️",
                    "Approve": "✅"
                }.get(decision, "❓")

                st.markdown(f"Fraud Score: **{fraud_score}/100** {score_color} `{risk}`")
                st.markdown(f"Decision: {decision_emoji} **{decision}**")
                st.markdown("---")

                results.append({
                    "Claim ID": claim["claim_id"],
                    "Amount ($)": f"${claim['claim_amount']:,}",
                    "Fraud Score": fraud_score,
                    "Risk": risk,
                    "Decision": f"{decision_emoji} {decision}"
                })

                time.sleep(0.4)

        feed.empty()
        st.success(f"✅ Batch complete — {len(results)} claims processed")
        st.session_state["results"] = results

with col_right:
    st.subheader("🧾 Single Claim Analysis")
    st.caption("Manually enter claim details to analyse a single claim")

    with st.form("single_claim"):
        c1, c2 = st.columns(2)
        with c1:
            amount = st.number_input("Claim Amount ($)", min_value=100, max_value=100000, value=5000, step=500)
            age = st.number_input("Customer Age", min_value=18, max_value=100, value=35)
        with c2:
            past = st.number_input("Past Claims", min_value=0, max_value=20, value=2)
            days = st.number_input("Days Since Policy", min_value=1, max_value=3650, value=365)

        submitted = st.form_submit_button("Analyse Claim", use_container_width=True)

        if submitted:
            claim = {
                "claim_id": 99,
                "claim_amount": amount,
                "customer_age": age,
                "num_claims_past": past,
                "days_since_policy": days
            }

            with st.spinner("Scoring fraud risk..."):
                fraud_score = predict_fraud_score(claim)
                decision = get_decision(fraud_score, amount)

            if fraud_score > 80:
                st.error(f"🔴 Fraud Score: {fraud_score}/100 — HIGH RISK")
            elif fraud_score > 40:
                st.warning(f"🟡 Fraud Score: {fraud_score}/100 — MEDIUM RISK")
            else:
                st.success(f"🟢 Fraud Score: {fraud_score}/100 — LOW RISK")

            decision_emoji = {"Reject": "❌", "Manual Review": "⚠️", "Approve": "✅"}.get(decision)
            st.metric("Decision", f"{decision_emoji} {decision}")
            st.progress(fraud_score / 100)

            st.markdown("---")
            show_bpmn_routing(fraud_score, amount, decision)

st.markdown("---")

# ── Results table ────────────────────────────────────────────
st.subheader("📋 Claims Processed This Session")

if "results" in st.session_state and st.session_state["results"]:
    df = pd.DataFrame(st.session_state["results"])
    st.dataframe(df, use_container_width=True, hide_index=True)

    total = len(df)
    approved = len([r for r in st.session_state["results"] if "Approve" in r["Decision"]])
    rejected = len([r for r in st.session_state["results"] if "Reject" in r["Decision"]])
    manual = len([r for r in st.session_state["results"] if "Manual" in r["Decision"]])

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Processed", total)
    m2.metric("✅ Approved", approved)
    m3.metric("❌ Rejected", rejected)
    m4.metric("⚠️ Manual Review", manual)

else:
    st.caption("Run batch processing or analyse a single claim to see results here.")

st.markdown("---")

# ── Architecture note ────────────────────────────────────────
with st.expander("ℹ️ How this system works"):
    st.markdown("""
    **ML Layer**
    - Random Forest classifier trained on synthetic claims data
    - Features: claim amount, customer age, past claims, days since policy
    - Outputs a fraud score from 0 to 100

    **BPMN Routing Logic (Camunda)**
    - `fraudScore > 80` → **Reject** — too risky
    - `fraudScore <= 80` AND `claimAmount > $10,000` → **Manual Review** — human checks high value
    - `fraudScore <= 80` AND `claimAmount <= $10,000` → **Approve** — safe to process

    **In production**, Python calls the Camunda Cloud REST API to automatically 
    start a BPMN process instance — routing the claim through a real workflow engine.
    The full Camunda integration is available in the source code.
    """)

st.caption("Built with Python · scikit-learn · Camunda BPMN · Streamlit")