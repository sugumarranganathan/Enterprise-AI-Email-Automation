
"""
Enterprise AI Email Automation
Improved Professional Dashboard
Author: Sugumar R
"""

import time
import gradio as gr
from graph.workflow import graph

CSS = """
.gradio-container{max-width:1500px!important;margin:auto;padding:20px;background:#f5f7fa}
.card{border:1px solid #ddd;border-radius:10px;padding:12px;background:white;text-align:center}
"""

def card(title,value,emoji):
    value=value or "-"
    return f"### {emoji} {title}\n\n**{value}**"

def workflow():
    return """
📩 Email
⬇
📖 Reader
⬇
🏷 Classification
⬇
🚨 Priority
⬇
😊 Sentiment
⬇
📚 Knowledge
⬇
📜 Policy
⬇
✉️ Response
⬇
📝 Reviewer
⬇
📤 Sender
"""

def summarize_knowledge(text:str)->str:
    if not text:
        return "No knowledge retrieved."
    lines=[l.strip() for l in text.splitlines() if l.strip()]
    bullets=[]
    seen=set()
    for l in lines:
        if l not in seen:
            seen.add(l)
            bullets.append(f"• {l}")
        if len(bullets)>=6:
            break
    return "Retrieved Knowledge\n\n"+"\n".join(bullets)

def process(email):
    start=time.time()
    state={"email":email,"sender":"customer@example.com","subject":"Customer Email"}
    r=graph.invoke(state)
    elapsed=round(time.time()-start,2)
    return (
        card("Category",r.get("category"),"📂"),
        card("Priority",r.get("priority"),"🚨"),
        card("Sentiment",r.get("sentiment"),"😊"),
        card("Approval",r.get("approval_status"),"✅"),
        card("Send Status",r.get("send_status"),"📤"),
        summarize_knowledge(r.get("knowledge","")),
        r.get("policy_result") or r.get("policy","No policy."),
        r.get("final_email",""),
        workflow(),
        f"⏱ Completed in {elapsed} seconds"
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
        c=gr.Markdown()
        p=gr.Markdown()
        s=gr.Markdown()
        a=gr.Markdown()
        snd=gr.Markdown()

    gr.Markdown("## 📚 Knowledge Agent (Qdrant RAG)")
    knowledge=gr.Markdown()

    gr.Markdown("## 📜 Company Policy")
    policy=gr.Markdown()

    gr.Markdown("## ✉️ AI Generated Email")
    final=gr.Markdown()

    gr.Markdown("## 🤖 Workflow Status")
    wf=gr.Markdown(workflow())
    tm=gr.Markdown()

    run.click(process,email,[c,p,s,a,snd,knowledge,policy,final,wf,tm])
    clear.click(lambda:("","","","","","","","","",""),
                outputs=[email,c,p,s,a,snd,knowledge,policy,final,tm])

if __name__=="__main__":
    demo.launch(server_name="0.0.0.0",server_port=7860,share=True)
