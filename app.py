"""
====================================================
Enterprise AI Email Automation
Professional Dashboard

Author : Sugumar R
====================================================
"""

# =====================================================
# Imports
# =====================================================

import time
import traceback

import gradio as gr

from graph.workflow import graph


# =====================================================
# Enterprise Theme
# =====================================================

css = """
.gradio-container{
    max-width:1500px !important;
    margin:auto;
    padding:20px;
    background:#F5F7FA;
}

.main-title{
    text-align:center;
    font-size:38px;
    font-weight:bold;
    color:#1565C0;
}

.sub-title{
    text-align:center;
    color:#666;
    font-size:18px;
    margin-bottom:20px;
}

.dashboard-card{
    border-radius:10px;
    border:1px solid #E0E0E0;
    background:white;
    padding:15px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:20px;
}
"""


# =====================================================
# Dashboard Card
# =====================================================

def dashboard_card(title, value, emoji="📌"):

    if value is None or value == "":
        value = "-"

    return f"""
### {emoji} {title}

**{value}**
"""


# =====================================================
# Workflow Status
# =====================================================

def workflow_status():

    return """
# 🤖 Multi-Agent Workflow

✅ Email Listener

✅ Reader Agent

✅ Classification Agent

✅ Priority Agent

✅ Sentiment Agent

✅ Knowledge Agent

✅ Policy Agent

✅ Response Agent

✅ Reviewer Agent

✅ Approval Agent

✅ Email Sender

✅ History Logger
"""


# =====================================================
# Example Emails
# =====================================================

examples = [

[
"""Hello,

I received my laptop yesterday.

Unfortunately the screen is damaged.

Please arrange a replacement.

Thanks,
John"""
],

[
"""Hello,

I have not received my order.

Please check the delivery status.

Regards,
David"""
],

[
"""Hello,

Please cancel my subscription immediately.

Thank you.

Sarah"""
],

[
"""Hello,

My product is under warranty.

It stopped working yesterday.

Please help.

Regards,
James"""
]

]


# =====================================================
# Clear All
# =====================================================

def clear_all():

    return (

        "",         # email

        "",         # summary
        "",         # intent

        "",         # category
        "",         # priority
        "",         # sentiment

        "No knowledge retrieved.",
        "No policy available.",

        "",         # approval
        "",         # send status

        "No email generated.",

        dashboard_card("Category","", "📂"),
        dashboard_card("Priority","", "🚨"),
        dashboard_card("Sentiment","", "😊"),
        dashboard_card("Approval","", "✅"),
        dashboard_card("Send Status","", "📧"),

        workflow_status(),

        ""
    )


# =====================================================
# Process Email
# =====================================================

def process_email(email):

    if not email.strip():
        raise gr.Error("Please enter customer email.")

    try:

        start = time.time()

        state = {

            "sender": "customer@example.com",
            "subject": "Customer Email",
            "email": email

        }

        result = graph.invoke(state)

        elapsed = round(time.time() - start, 2)

        return (

            result.get("summary",""),
            result.get("intent",""),

            result.get("category",""),
            result.get("priority",""),
            result.get("sentiment",""),

            result.get("knowledge","No knowledge found."),
            result.get("policy_result","No policy found."),

            result.get("approval_status","Pending"),
            result.get("send_status","Not Sent"),

            result.get("final_email",""),

            dashboard_card(
                "Category",
                result.get("category",""),
                "📂"
            ),

            dashboard_card(
                "Priority",
                result.get("priority",""),
                "🚨"
            ),

            dashboard_card(
                "Sentiment",
                result.get("sentiment",""),
                "😊"
            ),

            dashboard_card(
                "Approval",
                result.get("approval_status",""),
                "✅"
            ),

            dashboard_card(
                "Send Status",
                result.get("send_status",""),
                "📧"
            ),

            workflow_status(),

            f"⏱ Completed in {elapsed} seconds"

        )

    except Exception:

        traceback.print_exc()

        raise gr.Error("Workflow execution failed.")

# =====================================================
# Professional Gradio UI
# =====================================================

with gr.Blocks(
    title="Enterprise AI Email Automation"
) as demo:

    gr.HTML("""
    <div class="main-title">
        📧 Enterprise AI Email Automation
    </div>

    <div class="sub-title">
        Multi-Agent AI Email Assistant using
        <b>LangGraph • Groq • Gmail • Qdrant</b>
    </div>
    """)

    # =====================================================
    # Statistics
    # =====================================================

    with gr.Row():

        gr.Markdown("""
### 🤖 AI Agents

**12**
""")

        gr.Markdown("""
### 📚 Knowledge Base

**Qdrant**
""")

        gr.Markdown("""
### 🧠 LLM

**Groq**
""")

        gr.Markdown("""
### ⚡ Workflow

**LangGraph**
""")

    gr.Markdown("---")

    # =====================================================
    # Email Input
    # =====================================================

    with gr.Row():

        with gr.Column(scale=6):

            email = gr.Textbox(
                label="📩 Customer Email",
                lines=18,
                placeholder="Paste customer email here..."
            )

            with gr.Row():

                process_btn = gr.Button(
                    "🚀 Process Email",
                    variant="primary"
                )

                clear_btn = gr.Button(
                    "🧹 Clear"
                )

        with gr.Column(scale=4):

            summary = gr.Textbox(
                label="📝 Summary",
                lines=5,
                interactive=False
            )

            intent = gr.Textbox(
                label="🎯 Intent",
                interactive=False
            )

    # =====================================================
    # Dashboard
    # =====================================================

    gr.Markdown("---")
    gr.Markdown("## 📊 Enterprise Dashboard")

    with gr.Row():

        category_card = gr.Markdown(
            dashboard_card("Category","","📂")
        )

        priority_card = gr.Markdown(
            dashboard_card("Priority","","🚨")
        )

        sentiment_card = gr.Markdown(
            dashboard_card("Sentiment","","😊")
        )

        approval_card = gr.Markdown(
            dashboard_card("Approval","","✅")
        )

        send_card = gr.Markdown(
            dashboard_card("Send Status","","📧")
        )

    # =====================================================
    # Details
    # =====================================================

    with gr.Row():

        category = gr.Textbox(
            label="📂 Category",
            interactive=False
        )

        priority = gr.Textbox(
            label="🚨 Priority",
            interactive=False
        )

        sentiment = gr.Textbox(
            label="😊 Sentiment",
            interactive=False
        )

        approval = gr.Textbox(
            label="✅ Approval",
            interactive=False
        )

        send_status = gr.Textbox(
            label="📤 Send Status",
            interactive=False
        )

    # =====================================================
    # Examples
    # =====================================================

    gr.Examples(
        examples=examples,
        inputs=email,
        label="📄 Example Emails"
    )

    # =====================================================
    # Knowledge Base
    # =====================================================

    gr.Markdown("---")
    gr.Markdown("## 📚 Retrieved Knowledge")

    knowledge = gr.Markdown(
        value="No knowledge retrieved."
    )

    # =====================================================
    # Company Policy
    # =====================================================

    gr.Markdown("---")
    gr.Markdown("## 📜 Company Policy")

    policy = gr.Markdown(
        value="No policy available."
    )

    # =====================================================
    # AI Generated Email
    # =====================================================

    gr.Markdown("---")
    gr.Markdown("## ✉️ AI Generated Email")

    final_email = gr.Markdown(
        value="No email generated."
    )

    # =====================================================
    # Workflow Status
    # =====================================================

    gr.Markdown("---")
    gr.Markdown("## 🤖 Workflow Status")

    workflow = gr.Markdown(
        workflow_status()
    )

    processing_time = gr.Markdown("")

# =====================================================
# Human Approval
# =====================================================

    gr.Markdown("---")
    gr.Markdown("## 👤 Human Approval")

    with gr.Row():

        approve_btn = gr.Button(
            "✅ Approve",
            variant="primary"
        )

        reject_btn = gr.Button(
            "❌ Reject",
            variant="stop"
        )

    approval_result = gr.Markdown(
        value="Waiting for approval..."
    )


# =====================================================
# Approval Functions
# =====================================================

    def approve_email():

        return """
## ✅ Email Approved

The AI generated email has been approved.

Ready to send.
"""

    def reject_email():

        return """
## ❌ Email Rejected

Please modify the response and regenerate.
"""


# =====================================================
# Footer
# =====================================================

    gr.Markdown(
"""
---

# 🚀 Enterprise AI Email Automation

### Intelligent Multi-Agent Email Assistant

### Technology Stack

- 🤖 LangGraph
- 🧠 Groq LLM
- 📚 Qdrant Vector Database
- 📧 Gmail API
- 🎨 Gradio

---

Developed by **Sugumar R**

© 2026
"""
    )


# =====================================================
# Button Events
# =====================================================

    process_btn.click(

        fn=process_email,

        inputs=[email],

        outputs=[

            summary,
            intent,

            category,
            priority,
            sentiment,

            knowledge,
            policy,

            approval,
            send_status,

            final_email,

            category_card,
            priority_card,
            sentiment_card,
            approval_card,
            send_card,

            workflow,
            processing_time

        ],

        show_progress="full"

    )


    clear_btn.click(

        fn=clear_all,

        outputs=[

            email,

            summary,
            intent,

            category,
            priority,
            sentiment,

            knowledge,
            policy,

            approval,
            send_status,

            final_email,

            category_card,
            priority_card,
            sentiment_card,
            approval_card,
            send_card,

            workflow,
            processing_time

        ]

    )


    approve_btn.click(

        fn=approve_email,

        outputs=approval_result

    )


    reject_btn.click(

        fn=reject_email,

        outputs=approval_result

    )


# =====================================================
# Queue
# =====================================================

demo.queue(max_size=20)


# =====================================================
# Launch
# =====================================================

if __name__ == "__main__":

    demo.launch(

        server_name="0.0.0.0",

        server_port=7860,

        share=True,

        show_error=True,

        debug=True

    )
