"""
====================================================
Enterprise AI Email Automation
Workflow Test
====================================================
"""

from graph.workflow import graph


def test_workflow():

    state = {

        "sender": "customer@example.com",

        "subject": "Refund Request",

        "email": """
Hello,

I received my order yesterday.

Unfortunately the product arrived damaged.

I would like a refund.

Please help.

Thanks,
John
"""

    }

    print("=" * 80)
    print("Enterprise AI Email Automation")
    print("Complete Workflow Test")
    print("=" * 80)

    try:

        result = graph.invoke(state)

        print("\n✅ Workflow Executed Successfully")

    except Exception as e:

        print("\n❌ Workflow Failed")

        print(e)

        return

    print("\n" + "=" * 80)
    print("WORKFLOW OUTPUT")
    print("=" * 80)

    fields = [

        "summary",

        "intent",

        "category",

        "priority",

        "sentiment",

        "knowledge",

        "policy_result",

        "draft_reply",

        "reviewed_reply",

        "final_email",

        "approval_status",

        "send_status"

    ]

    for field in fields:

        print(f"\n{field}")

        print("-" * 80)

        print(result.get(field, "Not Available"))


if __name__ == "__main__":

    test_workflow()
