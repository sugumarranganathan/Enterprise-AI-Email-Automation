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
    border:1px solid #E5E5E5;
    border-radius:10px;
    padding:15px;
    text-align:center;
    background:white;
}

.footer{
    text-align:center;
    color:gray;
    font-size:13px;
    margin-top:20px;
}
"""


# =====================================================
# Dashboard Card
# =====================================================

def dashboard_card(title, value, emoji="📌"):

    if not value:
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

✅ Formatter Agent

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

I received my order yesterday.

Unfortunately the product arrived damaged.

I would like a refund.

Thanks,
John"""
],

[
"""Hello,

My parcel has not been delivered.

Please check the shipment.

Regards,
David"""
],

[
"""Hello,

Please cancel my order before shipping.

Thanks,
Sarah"""
],

[
"""Hello,

The laptop is still under warranty.

The screen stopped working.

Please help.

Regards,
James"""
]

]


# =====================================================
# Clear Function
# =====================================================

def clear_all():

    return (

        "",

        "",

        "",

        "",

        "",

        "",

        "",

        "",

        "",

        "",

        "",

        dashboard_card("Category",""),

        dashboard_card("Priority",""),

        dashboard_card("Sentiment",""),

        dashboard_card("Approval",""),

        dashboard_card("Send Status",""),

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

            "sender":"customer@example.com",

            "subject":"Customer Email",

            "email":email

        }

        result = graph.invoke(state)

        elapsed = round(time.time()-start,2)

        return (

            result.get("summary",""),

            result.get("intent",""),

            result.get("category",""),

            result.get("priority",""),

            result.get("sentiment",""),

            result.get("knowledge",""),

            result.get("policy_result",""),

            result.get("approval_status",""),

            result.get("send_status",""),

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

            f"⏱ Completed in {elapsed} sec"

        )

    except Exception:

        traceback.print_exc()

        raise gr.Error("Workflow execution failed.")


# =====================================================
# Professional UI
# =====================================================

with gr.Blocks(

    title="Enterprise AI Email Automation",

    theme=gr.themes.Soft(),

    css=css

) as demo:

    # =================================================
    # Header
    # =================================================

    gr.HTML(

        """
<div class="main-title">

📧 Enterprise AI Email Automation

</div>

<div class="sub-title">

Multi-Agent AI Email Assistant using
LangGraph • Groq • Gmail • Qdrant

</div>

"""
    )

    # =================================================
    # Statistics
    # =================================================

    with gr.Row():

        gr.Markdown(
"""
### 🤖 AI Agents

**12**
"""
)

        gr.Markdown(
"""
### 📚 Knowledge Base

**Qdrant**
"""
)

        gr.Markdown(
"""
### 🧠 LLM

**Groq**
"""
)

        gr.Markdown(
"""
### ⚡ Workflow

**LangGraph**
"""
)

    # =================================================
    # Customer Email
    # =================================================

    gr.Markdown("---")

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

                    variant="primary",

                    size="lg"

                )

                clear_btn = gr.Button(

                    "🧹 Clear",

                    size="lg"

                )

        with gr.Column(scale=4):

            summary = gr.Textbox(

                label="📝 Summary",

                interactive=False,

                lines=4

            )

            intent = gr.Textbox(

                label="🎯 Intent",

                interactive=False

            )

    # =================================================
    # Enterprise Dashboard
    # =================================================

    gr.Markdown("---")

    gr.Markdown("## 📊 Enterprise Dashboard")

    with gr.Row():

        category_card = gr.Markdown(

            value=dashboard_card(

                "Category",

                "",

                "📂"

            )

        )

        priority_card = gr.Markdown(

            value=dashboard_card(

                "Priority",

                "",

                "🚨"

            )

        )

        sentiment_card = gr.Markdown(

            value=dashboard_card(

                "Sentiment",

                "",

                "😊"

            )

        )

        approval_card = gr.Markdown(

            value=dashboard_card(

                "Approval",

                "",

                "✅"

            )

        )

        send_card = gr.Markdown(

            value=dashboard_card(

                "Send Status",

                "",

                "📧"

            )

        )

    # =================================================
    # Details
    # =================================================

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

            label="✅ Approval Status",

            interactive=False

        )

        send_status = gr.Textbox(

            label="📤 Send Status",

            interactive=False

        )

    # =================================================
    # Example Emails
    # =================================================

    gr.Examples(

        examples=examples,

        inputs=email,

        label="📄 Example Customer Emails"

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

    value="""
No email generated.
"""
)


# =====================================================
# Workflow Status
# =====================================================

gr.Markdown("---")

gr.Markdown("## 🤖 Workflow Status")

workflow = gr.Markdown(

    value=workflow_status()

)

processing_time = gr.Markdown(

    value=""

)


# =====================================================
# Human Approval
# =====================================================

gr.Markdown("---")

gr.Markdown("## 👤 Human Approval")

with gr.Row():

    approve_btn = gr.Button(

        "✅ Approve",

        variant="primary",

        size="lg"

    )

    reject_btn = gr.Button(

        "❌ Reject",

        variant="stop",

        size="lg"

    )


approval_result = gr.Markdown(

    value="Waiting for approval."

)


# =====================================================
# Approval Functions
# =====================================================

def approve_email():

    return """

# ✅ Email Approved

The email has been approved.

Ready to send.

"""


def reject_email():

    return """

# ❌ Email Rejected

Please regenerate or modify the email.

"""


approve_btn.click(

    fn=approve_email,

    outputs=approval_result

)


reject_btn.click(

    fn=reject_email,

    outputs=approval_result

)


# =====================================================
# Footer
# =====================================================

gr.Markdown(

"""
---

# 🚀 Enterprise AI Email Automation

### Intelligent Multi-Agent Email Assistant

### Technology Stack

🤖 LangGraph

🧠 Groq LLM

📚 Qdrant Vector Database

📧 Gmail API

🎨 Gradio

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

    inputs=[

        email

    ],

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


# =====================================================
# Human Approval
# =====================================================

approve_btn.click(

    fn=approve_email,

    outputs=[

        approval_result

    ]

)


reject_btn.click(

    fn=reject_email,

    outputs=[

        approval_result

    ]

)


# =====================================================
# Queue
# =====================================================

demo.queue(

    max_size=20

)


# =====================================================
# Queue
# =====================================================

demo.queue(max_size=20)

# =====================================================
# Render Deployment
# =====================================================

demo.queue(max_size=20)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )

