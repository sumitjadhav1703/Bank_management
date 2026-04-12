def build_dashboard_stats(data):
    balances = [user.get("balance", 0) for user in data]
    total_balance = sum(balances)
    total_accounts = len(data)
    average_balance = total_balance / total_accounts if total_accounts else 0
    highest_balance = max(balances) if balances else 0
    return {
        "total_accounts": total_accounts,
        "total_balance": total_balance,
        "average_balance": average_balance,
        "highest_balance": highest_balance,
    }


def validate_account_input(name, age, email, pin):
    """Validate account form input and return a user-facing error message."""

    if not name.strip() or not email.strip():
        return "Name and email are required."
    normalized_pin = str(pin).strip()
    if age < 18 or len(normalized_pin) != 4 or not normalized_pin.isdigit():
        return "Applicants must be at least 18 years old and use a 4-digit PIN."
    return ""
