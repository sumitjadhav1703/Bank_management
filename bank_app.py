import json
import random
import string
import streamlit as st
from pathlib import Path

DATABASE = Path(__file__).parent / "data.json"

# Load Data
def load_data():
    if DATABASE.exists():
        with open(DATABASE, "r") as f:
            return json.load(f)
    return []

# Save Data
def save_data(data):
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)

# Generate Unique Account Number
def generate_account_no(data):
    while True:
        acc = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if not any(user["accountNo"] == acc for user in data):
            return acc

# Get User
def get_user(data, acc, pin):
    for user in data:
        if user["accountNo"] == acc and user["pin"] == pin:
            return user
    return None

# Load DB
data = load_data()

# UI
st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account",
    ],
)

# CREATE ACCOUNT
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=0, max_value=100)
    email = st.text_input("Email")
    pin = st.text_input("4-Digit PIN", type="password")

    if st.button("Create Account"):
        if age < 18:
            st.error("Must be 18+")
        elif len(pin) != 4 or not pin.isdigit():
            st.error("PIN must be 4 digits")
        else:
            acc_no = generate_account_no(data)
            new_user = {
                "name": name,
                "age": age,
                "email": email,
                "pin": int(pin),
                "accountNo": acc_no,
                "balance": 0
            }
            data.append(new_user)
            save_data(data)

            st.success("Account Created Successfully!")
            st.write("🆔 Account Number:", acc_no)

# DEPOSIT MONEY
elif menu == "Deposit Money":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Deposit Amount", min_value=1, max_value=10000)

    if st.button("Deposit"):
        user = get_user(data, acc, int(pin) if pin.isdigit() else None)

        if not user:
            st.error("Invalid Account or PIN")
        else:
            user["balance"] += amount
            save_data(data)
            st.success("Money Deposited")
            st.write("New Balance:", user["balance"])

# WITHDRAW MONEY
elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Withdraw Amount", min_value=1)

    if st.button("Withdraw"):
        user = get_user(data, acc, int(pin) if pin.isdigit() else None)

        if not user:
            st.error("Invalid Account or PIN")
        elif user["balance"] < amount:
            st.error("Insufficient Balance")
        else:
            user["balance"] -= amount
            save_data(data)
            st.success("Money Withdrawn")
            st.write("New Balance:", user["balance"])

# SHOW DETAILS
elif menu == "Show Details":
    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        user = get_user(data, acc, int(pin) if pin.isdigit() else None)

        if not user:
            st.error("Invalid Account or PIN")
        else:
            st.json(user)

# UPDATE DETAILS
elif menu == "Update Details":
    st.subheader("Update Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Load Account"):
        user = get_user(data, acc, int(pin) if pin.isdigit() else None)

        if not user:
            st.error("Invalid Account or PIN")
        else:
            name = st.text_input("New Name", value=user["name"])
            email = st.text_input("New Email", value=user["email"])
            new_pin = st.text_input("New PIN (4 digits)", type="password")

            if st.button("Update"):
                if new_pin and (len(new_pin) != 4 or not new_pin.isdigit()):
                    st.error("PIN must be 4 digits")
                else:
                    user["name"] = name
                    user["email"] = email
                    if new_pin:
                        user["pin"] = int(new_pin)

                    save_data(data)
                    st.success("Details Updated")

# DELETE ACCOUNT
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        user = get_user(data, acc, int(pin) if pin.isdigit() else None)

        if not user:
            st.error("Invalid Account or PIN")
        else:
            data.remove(user)
            save_data(data)
            st.success("Account Deleted")
