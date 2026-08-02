"""
====================================================
Enterprise AI Email Automation
Dashboard UI
====================================================
"""

import gradio as gr


def create_dashboard():

    with gr.Blocks(
        theme=gr.themes.Soft(),
        title="Enterprise AI Email Automation"
    ) as demo:

        # =====================================================
        # Header
        # =====================================================

        gr.Markdown(
        """
# 📧 Enterprise AI Email Automation

### Multi-Agent AI Email Assistant
"""
        )

        # =====================================================
        # Email
        # =====================================================

        with gr.Row():

            with gr.Column(scale=6):

                email = gr.Textbox(
                    label="📩 Customer Email",
                    lines=15,
                    placeholder="Paste customer email..."
                )

                process_btn = gr.Button(
                    "🚀 Process Email",
                    variant="primary"
                )

            with gr.Column(scale=4):

                summary = gr.Textbox(
                    label="Summary",
                    interactive=False
                )

                intent = gr.Textbox(
                    label="Intent",
                    interactive=False
                )

                category = gr.Textbox(
                    label="Category",
                    interactive=False
                )

                priority = gr.Textbox(
                    label="Priority",
                    interactive=False
                )

                sentiment = gr.Textbox(
                    label="Sentiment",
                    interactive=False
                )

        # =====================================================
        # Knowledge
        # =====================================================

        gr.Markdown("## 📚 Retrieved Knowledge")

        knowledge = gr.Textbox(
            lines=8,
            interactive=False
        )

        # =====================================================
        # Policy
        # =====================================================

        gr.Markdown("## 📜 Company Policy")

        policy = gr.Textbox(
            lines=6,
            interactive=False
        )

        # =====================================================
        # Final Email
        # =====================================================

        gr.Markdown("## ✉️ Final Email")

        final_email = gr.Textbox(
            lines=12,
            interactive=False
        )

        # =====================================================
        # Human Approval
        # =====================================================

        with gr.Row():

            approve_btn = gr.Button(
                "✅ Approve",
                variant="primary"
            )

            reject_btn = gr.Button(
                "❌ Reject",
                variant="stop"
            )

        approval_status = gr.Textbox(
            label="Approval Status",
            interactive=False
        )

        send_status = gr.Textbox(
            label="Send Status",
            interactive=False
        )

    return (
        demo,
        email,
        process_btn,
        summary,
        intent,
        category,
        priority,
        sentiment,
        knowledge,
        policy,
        final_email,
        approve_btn,
        reject_btn,
        approval_status,
        send_status
    )
