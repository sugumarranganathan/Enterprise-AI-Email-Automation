"""
====================================================
Enterprise AI Email Automation
FastAPI Entry Point for Render
Author : Sugumar R
====================================================
"""

from fastapi import FastAPI
import gradio as gr

from app import demo

app = FastAPI(
    title="Enterprise AI Email Automation",
    version="1.0"
)

app = gr.mount_gradio_app(
    app,
    demo,
    path="/"
)
