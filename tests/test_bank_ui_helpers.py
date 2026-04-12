from bank_ui_helpers import build_dashboard_stats, validate_account_input


def test_build_dashboard_stats_returns_expected_summary():
    data = [
        {"name": "Asha", "balance": 1500, "accountNo": "ACC001", "pin": 1234, "age": 23, "email": "a@example.com"},
        {"name": "Rohan", "balance": 3500, "accountNo": "ACC002", "pin": 4321, "age": 31, "email": "r@example.com"},
    ]

    stats = build_dashboard_stats(data)

    assert stats == {
        "total_accounts": 2,
        "total_balance": 5000,
        "average_balance": 2500,
        "highest_balance": 3500,
    }


def test_validate_account_input_rejects_underage_and_bad_pin():
    message = validate_account_input(name="Sumit", age=17, email="sumit@example.com", pin="12")

    assert message == "Applicants must be at least 18 years old and use a 4-digit PIN."
