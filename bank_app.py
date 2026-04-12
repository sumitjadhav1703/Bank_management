import json
import random
import string
from pathlib import Path

import streamlit as st

from bank_ui_helpers import (
    build_dashboard_stats,
    format_account_details,
    format_currency,
    validate_account_input,
)

DATABASE = Path(__file__).parent / "data.json"

st.set_page_config(page_title="Bank Management Dashboard", page_icon="🏦", layout="wide")


def load_data():
    if DATABASE.exists():
        with open(DATABASE, "r") as file:
            return json.load(file)
    return []


def save_data(data):
    with open(DATABASE, "w") as file:
        json.dump(data, file, indent=4)


def generate_account_no(data):
    while True:
        acc = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if not any(user["accountNo"] == acc for user in data):
            return acc


def get_user(data, acc, pin):
    for user in data:
        if user["accountNo"] == acc and user["pin"] == pin:
            return user
    return None


def parse_pin(pin):
    return int(pin) if str(pin).isdigit() else None


def render_card(title, description):
    st.markdown(
        f"""
        <div class="panel-card feature-card">
          <h3>{title}</h3>
          <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_details(details):
    for label, value in details.items():
        st.markdown(
            f"""
            <div class="detail-row">
              <span>{label}</span>
              <strong>{value}</strong>
            </div>
            """,
            unsafe_allow_html=True,
        )


st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top right, rgba(34, 197, 94, 0.18), transparent 24%),
            radial-gradient(circle at top left, rgba(56, 189, 248, 0.20), transparent 30%),
            linear-gradient(180deg, #061826 0%, #0e2233 100%);
        color: #f4f7fb;
    }
    [data-testid="stSidebar"] {
        background: rgba(6, 24, 38, 0.92);
        border-right: 1px solid rgba(103, 232, 249, 0.16);
    }
    [data-testid="stMetric"] {
        background: rgba(15, 23, 42, 0.76);
        border: 1px solid rgba(103, 232, 249, 0.18);
        border-radius: 22px;
        padding: 0.9rem;
    }
    .hero-card, .metric-card, .panel-card {
        border-radius: 22px;
        padding: 1.2rem;
        background: rgba(15, 23, 42, 0.78);
        border: 1px solid rgba(103, 232, 249, 0.18);
        box-shadow: 0 20px 45px rgba(3, 8, 20, 0.25);
    }
    .hero-card h1, .panel-card h3 {
        color: #f8fafc;
        margin-bottom: 0.35rem;
    }
    .hero-card p, .panel-card p, .detail-row span {
        color: #cbd5e1;
    }
    .hero-card {
        padding: 1.6rem;
        margin-bottom: 1rem;
    }
    .eyebrow {
        letter-spacing: 0.18em;
        text-transform: uppercase;
        font-size: 0.78rem;
        color: #67e8f9;
        margin-bottom: 0.5rem;
    }
    .feature-card {
        min-height: 165px;
    }
    .section-label {
        margin: 1rem 0 0.5rem;
        color: #9bdaf1;
        font-size: 0.92rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    .detail-row {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        margin: 0.65rem 0;
        padding-bottom: 0.65rem;
        border-bottom: 1px solid rgba(148, 163, 184, 0.12);
    }
    .detail-row strong {
        color: #f8fafc;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

data = load_data()
stats = build_dashboard_stats(data)

if "update_account" not in st.session_state:
    st.session_state.update_account = None
if "delete_account" not in st.session_state:
    st.session_state.delete_account = None

st.markdown(
    """
    <div class="hero-card">
      <div class="eyebrow">Recruiter-facing showcase</div>
      <h1>Balanced Banking Showcase</h1>
      <p>A recruiter-friendly dashboard layered on top of the same JSON-backed banking workflow, built to make core CRUD and transaction handling easy to scan.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

metric_cols = st.columns(4)
metric_cols[0].metric("Total Accounts", stats["total_accounts"])
metric_cols[1].metric("Total Funds", format_currency(stats["total_balance"]))
metric_cols[2].metric("Average Balance", format_currency(stats["average_balance"]))
metric_cols[3].metric("Highest Balance", format_currency(stats["highest_balance"]))

action = st.sidebar.radio(
    "Choose Experience",
    [
        "Dashboard",
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account",
    ],
)

st.sidebar.caption("The same beginner-friendly banking logic, presented as a polished portfolio dashboard.")

if action == "Dashboard":
    st.markdown("### Portfolio Snapshot")
    summary_col, spotlight_col = st.columns([1.2, 1])

    with summary_col:
        st.markdown(
            """
            <div class="panel-card">
              <h3>What this screen demonstrates</h3>
              <p>The app keeps a lightweight JSON data layer while presenting the workflow as an intentional banking operations dashboard. Recruiters can quickly see account creation, secure account lookup with PIN validation, transaction handling, profile updates, and account deletion.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with spotlight_col:
        st.markdown(
            f"""
            <div class="panel-card">
              <h3>Current data posture</h3>
              <p>{stats["total_accounts"]} accounts currently tracked with {format_currency(stats["total_balance"])} in managed balances.</p>
              <p>Use the left-hand navigation to inspect each action route and the reusable helper-driven formatting layer.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-label">Feature Tour</div>', unsafe_allow_html=True)
    feature_cols = st.columns(3)
    with feature_cols[0]:
        render_card("Create and onboard", "Validates account setup with age and PIN rules, then assigns a unique account number.")
    with feature_cols[1]:
        render_card("Transact safely", "Deposit and withdrawal flows verify credentials and update balances with immediate feedback.")
    with feature_cols[2]:
        render_card("Maintain records", "Formatted detail, update, and delete routes keep the same data model readable and portfolio-ready.")

elif action == "Create Account":
    st.markdown("### Create Account")
    with st.form("create_account_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=0, max_value=100, step=1)
        email = st.text_input("Email")
        pin = st.text_input("4-Digit PIN", type="password")
        submitted = st.form_submit_button("Create Account")

    if submitted:
        validation_message = validate_account_input(name, age, email, pin)
        if validation_message:
            st.error(validation_message)
        else:
            acc_no = generate_account_no(data)
            new_user = {
                "name": name.strip(),
                "age": int(age),
                "email": email.strip(),
                "pin": int(pin),
                "accountNo": acc_no,
                "balance": 0,
            }
            data.append(new_user)
            save_data(data)
            st.success("Account created successfully.")
            render_details(format_account_details(new_user))

elif action == "Deposit Money":
    st.markdown("### Deposit Money")
    with st.form("deposit_money_form"):
        acc = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")
        amount = st.number_input("Deposit Amount", min_value=1.0, max_value=100000.0, step=500.0)
        submitted = st.form_submit_button("Deposit")

    if submitted:
        user = get_user(data, acc.strip(), parse_pin(pin))
        if not user:
            st.error("Invalid account number or PIN.")
        else:
            user["balance"] += amount
            save_data(data)
            st.success(f"Deposit completed. New balance: {format_currency(user['balance'])}")
            render_details(format_account_details(user))

elif action == "Withdraw Money":
    st.markdown("### Withdraw Money")
    with st.form("withdraw_money_form"):
        acc = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")
        amount = st.number_input("Withdraw Amount", min_value=1.0, step=500.0)
        submitted = st.form_submit_button("Withdraw")

    if submitted:
        user = get_user(data, acc.strip(), parse_pin(pin))
        if not user:
            st.error("Invalid account number or PIN.")
        elif user["balance"] < amount:
            st.error("Insufficient balance.")
        else:
            user["balance"] -= amount
            save_data(data)
            st.success(f"Withdrawal completed. New balance: {format_currency(user['balance'])}")
            render_details(format_account_details(user))

elif action == "Show Details":
    st.markdown("### Show Details")
    with st.form("show_details_form"):
        acc = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")
        submitted = st.form_submit_button("Show Details")

    if submitted:
        user = get_user(data, acc.strip(), parse_pin(pin))
        if not user:
            st.error("Invalid account number or PIN.")
        else:
            details = format_account_details(user)
            render_details(details)

elif action == "Update Details":
    st.markdown("### Update Details")
    with st.form("load_update_form"):
        acc = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")
        load_submitted = st.form_submit_button("Load Account")

    if load_submitted:
        user = get_user(data, acc.strip(), parse_pin(pin))
        if not user:
            st.session_state.update_account = None
            st.error("Invalid account number or PIN.")
        else:
            st.session_state.update_account = {
                "accountNo": user["accountNo"],
                "pin": user["pin"],
            }

    update_session = st.session_state.update_account
    if update_session:
        user = get_user(data, update_session["accountNo"], update_session["pin"])
        if user:
            with st.form("update_details_form"):
                name = st.text_input("New Name", value=user["name"])
                email = st.text_input("New Email", value=user["email"])
                new_pin = st.text_input("New PIN (leave blank to keep current)", type="password")
                update_submitted = st.form_submit_button("Update Details")

            if update_submitted:
                if new_pin and (len(new_pin) != 4 or not new_pin.isdigit()):
                    st.error("PIN must be 4 digits.")
                elif not name.strip() or not email.strip():
                    st.error("Name and email are required.")
                else:
                    user["name"] = name.strip()
                    user["email"] = email.strip()
                    if new_pin:
                        user["pin"] = int(new_pin)
                        st.session_state.update_account["pin"] = user["pin"]
                    save_data(data)
                    st.success("Account details updated.")
                    render_details(format_account_details(user))
        else:
            st.session_state.update_account = None
            st.warning("The selected account is no longer available.")

elif action == "Delete Account":
    st.markdown("### Delete Account")
    with st.form("load_delete_form"):
        acc = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")
        load_submitted = st.form_submit_button("Load Account")

    if load_submitted:
        user = get_user(data, acc.strip(), parse_pin(pin))
        if not user:
            st.session_state.delete_account = None
            st.error("Invalid account number or PIN.")
        else:
            st.session_state.delete_account = {
                "accountNo": user["accountNo"],
                "pin": user["pin"],
            }

    delete_session = st.session_state.delete_account
    if delete_session:
        user = get_user(data, delete_session["accountNo"], delete_session["pin"])
        if user:
            st.markdown(
                """
                <div class="panel-card">
                  <h3>Confirm account removal</h3>
                  <p>This action permanently removes the account from the JSON datastore.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            render_details(format_account_details(user))
            confirm_col, cancel_col = st.columns(2)
            with confirm_col:
                if st.button("Confirm Delete", type="primary"):
                    data.remove(user)
                    save_data(data)
                    st.session_state.delete_account = None
                    st.success("Account deleted.")
            with cancel_col:
                if st.button("Cancel"):
                    st.session_state.delete_account = None
                    st.info("Deletion cancelled.")
        else:
            st.session_state.delete_account = None
            st.warning("The selected account is no longer available.")
