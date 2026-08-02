"""
====================================================
Enterprise AI Email Automation
Agent Test
====================================================
"""

from agents.classification_agent import classification_agent
from agents.priority_agent import priority_agent
from agents.sentiment_agent import sentiment_agent
from agents.reader_agent import reader_agent
from agents.knowledge_agent import knowledge_agent
from agents.policy_agent import policy_agent
from agents.responder_agent import responder_agent
from agents.reviewer_agent import reviewer_agent
from agents.formatter_agent import formatter_agent
from agents.approval_agent import approval_agent


def test_agents():

    state = {

        "sender": "customer@example.com",

        "subject": "Refund Request",

        "email": """
Hello,

I received my order yesterday.

Unfortunately the product arrived damaged.

I would like a refund.

Thanks,
John
"""

    }

    print("=" * 80)
    print("Enterprise AI Email Automation")
    print("=" * 80)

    agents = [

        ("Reader Agent", reader_agent),

        ("Classification Agent", classification_agent),

        ("Priority Agent", priority_agent),

        ("Sentiment Agent", sentiment_agent),

        ("Knowledge Agent", knowledge_agent),

        ("Policy Agent", policy_agent),

        ("Response Agent", responder_agent),

        ("Reviewer Agent", reviewer_agent),

        ("Formatter Agent", formatter_agent),

        ("Approval Agent", approval_agent)

    ]

    for name, agent in agents:

        print("\n" + "=" * 80)
        print(name)
        print("=" * 80)

        try:

            state = agent(state)

            print("✅ PASS")

        except Exception as e:

            print("❌ FAIL")
            print(e)

            break

    print("\n" + "=" * 80)
    print("FINAL STATE")
    print("=" * 80)

    for key, value in state.items():

        print(f"\n{key}")

        print("-" * 80)

        print(value)


if __name__ == "__main__":

    test_agents()
