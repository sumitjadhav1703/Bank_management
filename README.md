# 🏦 Bank Management System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> A dual-interface banking project that shows the same core account workflow through a Python CLI and a polished Streamlit dashboard.

---

## 📑 Table of Contents

- [Why This Project Stands Out](#-why-this-project-stands-out)
- [Project Overview](#-project-overview)
- [Experience Modes](#-experience-modes)
- [Core Features](#-core-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Data Storage](#-data-storage)
- [What Recruiters Can Notice](#-what-recruiters-can-notice)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [Support](#-support)

---

## 🌟 Why This Project Stands Out

| Strength | What it shows |
| --- | --- |
| **Dual interface design** | The same banking workflow can be presented in both terminal-first and recruiter-friendly UI form. |
| **JSON persistence** | Practical use of lightweight local storage without adding unnecessary complexity. |
| **Real account operations** | Account creation, deposits, withdrawals, detail lookup, updates, and deletion. |
| **Validation and UX thinking** | Input checks, formatted feedback, and cleaner flow for demos. |

## 📖 Project Overview

This project simulates a lightweight bank management system for learning and portfolio use. It keeps the data model simple with `data.json`, while showing two ways to interact with the same banking logic:

- `CLI experience` for direct Python workflow practice
- `Streamlit dashboard` for a more visual, recruiter-friendly demo

## 💻 Experience Modes

### 1. CLI Banking Workflow

The CLI version in `main.py` highlights:

- Python control flow
- File handling with JSON
- Account validation logic
- CRUD-style account management

It is useful for showing the raw logic of the application without hiding the workflow behind UI layers.

### 2. Streamlit Banking Dashboard

The Streamlit version in `bank_app.py` highlights:

- A portfolio-style dashboard layout
- Account summary metrics
- Structured action flows
- Cleaner feedback and formatted account details

It is designed to make the project easier to demo on GitHub or during interviews.

## ✨ Core Features

- **Create a new account** with age and PIN validation.
- **Deposit money** into an existing account.
- **Withdraw money** with balance checks.
- **View formatted account details**.
- **Update** customer name, email, and PIN.
- **Delete** an account with a confirmation flow.
- **Persist all records** locally in `data.json`.

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Streamlit
- **Data Storage:** JSON
- **Testing:** Pytest

## 📂 Project Structure

```text
Bank_management/
├── bank_app.py              # Streamlit dashboard interface
├── bank_ui_helpers.py       # Reusable formatting and validation helpers
├── data.json                # Local JSON datastore
├── main.py                  # CLI banking workflow
├── README.md                # Project documentation
└── tests/
    ├── conftest.py
    └── test_bank_ui_helpers.py
```

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed, then install the required dependencies:

```bash
pip install streamlit pytest
```

### Installation & Run

Clone the repository:

```bash
git clone https://github.com/sumitjadhav1703/Bank_management.git
cd Bank_management
```

Run the **CLI version**:

```bash
python main.py
```

Run the **Streamlit dashboard**:

```bash
streamlit run bank_app.py
```

## 💾 Data Storage

All account records are stored locally in `data.json`. This keeps the project easy to understand and portable, while still demonstrating persistent state across runs.

## 👀 What Recruiters Can Notice

- The project solves one problem through two different interfaces.
- Helper functions are separated from presentation code.
- The Streamlit app adds polish without replacing the underlying Python workflow.
- Tests cover validation and display helper behavior.

## 🔮 Future Improvements

- [ ] Add transaction history records
- [ ] Add database-backed persistence with SQLite or MySQL
- [ ] Add authentication for account access
- [ ] Add analytics or charts for account activity
- [ ] Add exportable reporting

## 👨‍💻 Author

**Sumit Jadhav**  
AI & Data Science Student  
[GitHub](https://github.com/sumitjadhav1703)

## 💖 Support

If you like the project, consider starring the repository. ⭐
