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
from health import router as health_router

app = FastAPI(
    title="Enterprise AI Email Automation",
    version="1.0.0"
)

app.include_router(health_router)

app = gr.mount_gradio_app(
    app,
    demo,
    path="/app"
)
