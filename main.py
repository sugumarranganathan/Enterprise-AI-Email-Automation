"""
====================================================
Enterprise AI Email Automation
FastAPI Entry Point

Author : Sugumar R
====================================================
"""

from fastapi import FastAPI
import gradio as gr

from app import demo

# Routers
from health import router as health_router
from gmail.webhook import router as gmail_router
from gmail.auth import router as auth_router
from gmail.callback import router as callback_router

# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(
    title="Enterprise AI Email Automation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# =====================================================
# Register Routers
# =====================================================

app.include_router(health_router)

# Gmail OAuth
app.include_router(auth_router)
app.include_router(callback_router)

# Gmail Webhook
app.include_router(gmail_router)

# =====================================================
# Mount Gradio UI
# =====================================================

app = gr.mount_gradio_app(
    app,
    demo,
    path="/",
)

# =====================================================
# Root Endpoint
# =====================================================

@app.get("/api")
def api_status():
    return {
        "status": "running",
        "application": "Enterprise AI Email Automation",
        "version": "1.0.0",
    }
