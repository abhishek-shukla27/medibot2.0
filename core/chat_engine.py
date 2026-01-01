from services.llm_client import generate_llm_response

def build_chat_prompt(query: str) -> str:
    domain = detect_topic_domain(query)

    if domain == "medical":
        closing = (
            "If you'd like, I can also generate viva questions, "
            "clinical recall points, or short exam-mode notes."
        )

    elif domain == "biology":
        closing = (
            "If you'd like, I can also give NCERT-style key points, "
            "diagram-based explanation, or quick revision notes."
        )

    else:
        closing = (
            "If you'd like, I can simplify this further, "
            "give real-world examples, or convert it into quick notes."
        )

    return f"""
You are MediBot — a friendly, natural, human-like tutor.
Explain concepts clearly in a teacher-style tone, not robotic.

Write in:
- clean, readable explanations
- meaningful bullet points where helpful
- light emoji highlights only when useful
- engaging and clear — not overly formal

Avoid:
- rigid templates
- generic headings
- repetitive phrasing
- chatbot-style questions in the middle

Explain the concept smoothly first.
Then at the END, add this closing line:

"{closing}"

Now explain this topic:

{query}
"""

def handle_chat_query(query: str) -> str:
    prompt = build_chat_prompt(query)
    response = generate_llm_response(prompt)
    return response

def detect_topic_domain(query: str)-> str:
      query_lower=query.lower()
      medical_keywords=[
           "syndrome","disease","lession","pathalogy",
           "neuron","axon","nerve","muscle","physiology",
           "anatomy","mbbs","clinical","diagnosis"
      ]

      biology_keywords=[
           "kingdom","taxonomy","cell","ncert",
           "classification","protista","monera","plantae"
      ]

      if any(k in query_lower for k in medical_keywords):
           return "medical"
      
      if any(k in query_lower for k in biology_keywords):
           return "biology"
      
      return "general"