/*
====================================================
Enterprise AI Email Automation
Database Schema
====================================================
*/

-- =====================================================
-- Email History
-- =====================================================

CREATE TABLE IF NOT EXISTS email_history (

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

    draft_reply TEXT,

    reviewed_reply TEXT,

    final_email TEXT,

    approval_status TEXT,

    send_status TEXT,

    message_id TEXT,

    thread_id TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- =====================================================
-- Workflow Logs
-- =====================================================

CREATE TABLE IF NOT EXISTS workflow_logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    email_id INTEGER,

    agent_name TEXT,

    status TEXT,

    execution_time REAL,

    log_message TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(email_id)
        REFERENCES email_history(id)

);

-- =====================================================
-- Company Knowledge Metadata
-- =====================================================

CREATE TABLE IF NOT EXISTS knowledge_documents (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    document_name TEXT,

    source TEXT,

    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- =====================================================
-- User Approval History
-- =====================================================

CREATE TABLE IF NOT EXISTS approval_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    email_id INTEGER,

    approved_by TEXT,

    approval_status TEXT,

    approval_reason TEXT,

    approval_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(email_id)
        REFERENCES email_history(id)

);

-- =====================================================
-- Indexes
-- =====================================================

CREATE INDEX IF NOT EXISTS idx_email_sender
ON email_history(sender);

CREATE INDEX IF NOT EXISTS idx_email_category
ON email_history(category);

CREATE INDEX IF NOT EXISTS idx_email_priority
ON email_history(priority);

CREATE INDEX IF NOT EXISTS idx_email_status
ON email_history(send_status);
