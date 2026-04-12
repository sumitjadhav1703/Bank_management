from bank_ui_helpers import (
    build_dashboard_stats,
    format_account_details,
    format_currency,
    validate_account_input,
)


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


def test_build_dashboard_stats_returns_zeros_for_empty_data():
    assert build_dashboard_stats([]) == {
        "total_accounts": 0,
        "total_balance": 0,
        "average_balance": 0,
        "highest_balance": 0,
    }


def test_build_dashboard_stats_treats_missing_balance_as_zero():
    data = [
        {"name": "Asha", "accountNo": "ACC001", "pin": 1234, "age": 23, "email": "a@example.com"},
        {"name": "Rohan", "balance": 3500, "accountNo": "ACC002", "pin": 4321, "age": 31, "email": "r@example.com"},
    ]

    stats = build_dashboard_stats(data)

    assert stats == {
        "total_accounts": 2,
        "total_balance": 3500,
        "average_balance": 1750,
        "highest_balance": 3500,
    }


def test_validate_account_input_rejects_missing_required_fields():
    message = validate_account_input(name=" ", age=23, email="", pin="1234")

    assert message == "Name and email are required."


def test_validate_account_input_accepts_valid_input():
    message = validate_account_input(name="Sumit", age=23, email="sumit@example.com", pin="1234")

    assert message == ""


def test_validate_account_input_accepts_age_eighteen():
    message = validate_account_input(name="Sumit", age=18, email="sumit@example.com", pin="1234")

    assert message == ""


def test_validate_account_input_rejects_underage_and_bad_pin():
    message = validate_account_input(name="Sumit", age=17, email="sumit@example.com", pin="12")

    assert message == "Applicants must be at least 18 years old and use a 4-digit PIN."


def test_validate_account_input_rejects_four_character_non_digit_pin():
    message = validate_account_input(name="Sumit", age=23, email="sumit@example.com", pin="12ab")

    assert message == "Applicants must be at least 18 years old and use a 4-digit PIN."


def test_validate_account_input_handles_integer_pin_safely():
    message = validate_account_input(name="Sumit", age=23, email="sumit@example.com", pin=1234)

    assert message == ""


def test_format_currency_uses_rupee_style_output():
    assert format_currency(42000) == "Rs 42,000"


def test_format_account_details_returns_label_value_pairs():
    user = {
        "name": "Sumit",
        "age": 20,
        "email": "sumit@example.com",
        "accountNo": "AB12CD34",
        "balance": 42000,
    }

    details = format_account_details(user)

    assert details["Account Number"] == "AB12CD34"
    assert details["Balance"] == "Rs 42,000"
