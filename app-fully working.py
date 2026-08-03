"""
====================================================
Enterprise AI Email Automation
Professional Multi-Agent Dashboard

Author : Sugumar R
====================================================
"""

import time
import traceback
import gradio as gr

from graph.workflow import graph

css = """
.gradio-container{
    max-width:1500px !important;
    margin:auto;
    padding:20px;
}
"""

def dashboard_card(title, value, emoji="📌"):
    if not value:
        value = "-"
    return f"### {emoji} {title}\n\n**{value}**"

def workflow_status():
    return """✅ Reader
✅ Classification
✅ Priority
✅ Sentiment
✅ Knowledge
✅ Policy
✅ Responder
✅ Reviewer
✅ Formatter
✅ Approval
✅ Email Sender
✅ History Logger"""

def process_email(email):
    if not email.strip():
        raise gr.Error("Please enter a customer email.")

    start = time.time()

    state = {
        "email": email,
        "sender": "customer@example.com",
        "subject": "Customer Email",
    }

    result = graph.invoke(state)
    elapsed = round(time.time() - start, 2)

    knowledge = result.get("knowledge", "No knowledge found.")

    policy = result.get("policy_result", result.get("policy", ""))

    return (
        dashboard_card("Category", result.get("category"), "📂"),
        dashboard_card("Priority", result.get("priority"), "🚨"),
        dashboard_card("Sentiment", result.get("sentiment"), "😊"),
        dashboard_card("Approval", result.get("approval_status"), "✅"),
        dashboard_card("Send Status", result.get("send_status"), "📤"),
        knowledge,
        policy,
        result.get("final_email", ""),
        workflow_status(),
        f"Completed in {elapsed} seconds",
    )

with gr.Blocks(css=css, title="Enterprise AI Email Automation") as demo:

    gr.Markdown("# 📧 Enterprise AI Email Automation")
    gr.Markdown("### Multi-Agent AI Email Assistant using LangGraph • Groq • Gmail • Qdrant")

    email = gr.Textbox(label="📩 Customer Email", lines=10)

    with gr.Row():
        process_btn = gr.Button("🚀 Process Email", variant="primary")
        clear_btn = gr.Button("🧹 Clear")

    gr.Markdown("## 📊 Enterprise Dashboard")

    with gr.Row():
        category = gr.Markdown()
        priority = gr.Markdown()
        sentiment = gr.Markdown()
        approval = gr.Markdown()
        send_status = gr.Markdown()

    gr.Markdown("## 📚 Knowledge Agent (Qdrant RAG)")
    knowledge = gr.Markdown()

    gr.Markdown("## 📜 Company Policy")
    policy = gr.Markdown()

    gr.Markdown("## ✉️ AI Generated Email")
    final_email = gr.Markdown()

    gr.Markdown("## 🤖 Workflow Status")
    workflow = gr.Markdown(workflow_status())
    processing = gr.Markdown()

    process_btn.click(
        fn=process_email,
        inputs=email,
        outputs=[
            category,
            priority,
            sentiment,
            approval,
            send_status,
            knowledge,
            policy,
            final_email,
            workflow,
            processing,
        ],
    )

    clear_btn.click(
        lambda: ("","","","","","","","","", ""),
        outputs=[
            email,
            category,
            priority,
            sentiment,
            approval,
            send_status,
            knowledge,
            policy,
            final_email,
            processing,
        ],
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
