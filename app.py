
"""
Enterprise AI Email Automation
Professional Dashboard with Human Approval
Author: Sugumar R
"""

import time
import gradio as gr
from graph.workflow import graph

CSS="""
.gradio-container{max-width:1500px!important;margin:auto;padding:20px;background:#f5f7fa}
"""

def card(title,value,emoji):
    return f"### {emoji} {title}\n\n**{value or '-'}**"

def workflow():
    return "📩 Email ➜ 📖 Reader ➜ 🏷 Classification ➜ 🚨 Priority ➜ 😊 Sentiment ➜ 📚 Knowledge ➜ 📜 Policy ➜ ✉️ Response ➜ 📝 Reviewer ➜ 📤 Sender"

def summarize(text):
    if not text:
        return "No knowledge retrieved."
    lines=[x.strip() for x in text.splitlines() if x.strip()]
    out=[]
    for l in lines:
        if l not in out:
            out.append(l)
        if len(out)>=5:
            break
    return "### Retrieved Knowledge\n\n" + "\n".join(f"• {x}" for x in out)

def process(email):
    start=time.time()
    result=graph.invoke({
        "email":email,
        "sender":"customer@example.com",
        "subject":"Customer Email"
    })
    t=round(time.time()-start,2)
    return (
        card("Category",result.get("category"),"📂"),
        card("Priority",result.get("priority"),"🚨"),
        card("Sentiment",result.get("sentiment"),"😊"),
        card("Approval",result.get("approval_status"),"✅"),
        card("Send Status",result.get("send_status"),"📤"),
        summarize(result.get("knowledge","")),
        result.get("policy_result") or result.get("policy",""),
        result.get("final_email",""),
        "### ⏳ Waiting for Human Approval",
        workflow(),
        f"⏱ Completed in {t} seconds"
    )

def approve():
    return (
        card("Approval","Approved","✅"),
        card("Send Status","Ready to Send","📤"),
        "## ✅ Email Approved\n\nThe AI generated email has been approved.\n\n**Status:** Ready to Send."
    )

def reject():
    return (
        card("Approval","Rejected","❌"),
        card("Send Status","Rejected","📤"),
        "## ❌ Email Rejected\n\nPlease review or regenerate the email before sending."
    )

with gr.Blocks(css=CSS,title="Enterprise AI Email Automation") as demo:
    gr.Markdown("# 📧 Enterprise AI Email Automation")
    gr.Markdown("### Multi-Agent AI Email Assistant using **LangGraph • Groq • Gmail • Qdrant**")
    email=gr.Textbox(label="📩 Customer Email",lines=8)
    with gr.Row():
        run=gr.Button("🚀 Process Email",variant="primary")
        clear=gr.Button("🧹 Clear")
    gr.Markdown("## 📊 Enterprise Dashboard")
    with gr.Row():
        category=gr.Markdown()
        priority=gr.Markdown()
        sentiment=gr.Markdown()
        approval=gr.Markdown()
        send=gr.Markdown()
    gr.Markdown("## 📚 Knowledge Agent (Qdrant RAG)")
    knowledge=gr.Markdown()
    gr.Markdown("## 📜 Company Policy")
    policy=gr.Markdown()
    gr.Markdown("## ✉️ AI Generated Email")
    final=gr.Markdown()

    gr.Markdown("## 👤 Human Approval")
    with gr.Row():
        approve_btn=gr.Button("✅ Approve",variant="primary")
        reject_btn=gr.Button("❌ Reject",variant="stop")
    approval_msg=gr.Markdown("### ⏳ Waiting for Human Approval")

    gr.Markdown("## 🤖 Workflow Status")
    wf=gr.Markdown(workflow())
    tm=gr.Markdown()

    run.click(process,email,[category,priority,sentiment,approval,send,knowledge,policy,final,approval_msg,wf,tm])
    approve_btn.click(approve,outputs=[approval,send,approval_msg])
    reject_btn.click(reject,outputs=[approval,send,approval_msg])

    clear.click(lambda:("","","","","","","","","","",""),
                outputs=[email,category,priority,sentiment,approval,send,knowledge,policy,final,approval_msg,tm])

if __name__=="__main__":
    demo.launch(server_name="0.0.0.0",server_port=7860,share=True)
