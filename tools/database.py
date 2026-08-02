"""
====================================================
Enterprise AI Email Automation
Database Utilities
====================================================
"""

import sqlite3
from pathlib import Path

# =====================================================
# Database Configuration
# =====================================================

DB_DIR = Path("database")
DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "enterprise_ai.db"


# =====================================================
# Database Connection
# =====================================================

def get_connection():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    return conn


# =====================================================
# Initialize Database
# =====================================================

def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS email_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        sender TEXT,

        subject TEXT,

        email TEXT,

        summary TEXT,

        intent TEXT,

        category TEXT,

        priority TEXT,

        sentiment TEXT,

        knowledge TEXT,

        policy_result TEXT,

        final_email TEXT,

        approval_status TEXT,

        send_status TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()

    conn.close()


# =====================================================
# Save Email History
# =====================================================

def save_email(state):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO email_history(

        sender,

        subject,

        email,

        summary,

        intent,

        category,

        priority,

        sentiment,

        knowledge,

        policy_result,

        final_email,

        approval_status,

        send_status

    )

    VALUES(

        ?,?,?,?,?,?,?,?,?,?,?,?,?

    )

    """,

    (

        state.get("sender"),

        state.get("subject"),

        state.get("email"),

        state.get("summary"),

        state.get("intent"),

        state.get("category"),

        state.get("priority"),

        state.get("sentiment"),

        state.get("knowledge"),

        state.get("policy_result"),

        state.get("final_email"),

        state.get("approval_status"),

        state.get("send_status")

    )

    )

    conn.commit()

    conn.close()


# =====================================================
# Get All Emails
# =====================================================

def get_all_emails():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM email_history

    ORDER BY id DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# =====================================================
# Get Email Count
# =====================================================

def get_email_count():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT COUNT(*) FROM email_history"

    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


# =====================================================
# Delete History
# =====================================================

def clear_history():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM email_history"

    )

    conn.commit()

    conn.close()


# =====================================================
# Initialize Automatically
# =====================================================

initialize_database()
