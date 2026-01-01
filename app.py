from core.chat_engine import handle_chat_query
import streamlit as st

st.set_page_config(page_title="medibot2.0 beta version",layout="wide")

st.title("🩺Medibot- Medical Study Assistant(Beta Version)")

st.write("This is beta version.Features will be added step by step")

with st.sidebar:
    st.title("🩺 Medibot Tools")
    mode=st.radio(
        "Select Feature",
        ["Chat","Notes","Uploads","Viva"]
    )
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

else:
    st.session_state.chat_history=[
        m for m in st.session_state.chat_history
        if isinstance(m, dict)
        and "role" in m
        and "content" in m
    ]
if mode == "Chat":
    st.subheader("💬 Chat Assistant")

    # ---------- CLEAR CHAT BUTTON ----------
    if st.button("🧹 Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

    st.markdown("---")

    # ---------- SHOW CHAT HISTORY ----------
    for message in st.session_state.chat_history:
        role = message.get("role", "")
        text = message.get("content", "")

        if role == "user":
            st.markdown(
                f"""
<div style='padding:10px; border-radius:10px; background:#grey; margin-bottom:10px'>
<b>🧑‍🎓 You</b><br>{text}
</div>
""",
                unsafe_allow_html=True
            )

        elif role == "bot":
            st.markdown(
                f"""
<div style='padding:10px; border-radius:10px; background:#black; margin-bottom:10px'>
<b>🤖 MediBot</b><br>{text}
</div>
""",
                unsafe_allow_html=True
            )

    st.markdown("---")

    # ---------- CHAT INPUT AT BOTTOM ----------
    user_query = st.text_input("Type your question here...")

    if st.button("Send"):
        if user_query.strip():

            # store user message
            st.session_state.chat_history.append({
                "role": "user",
                "content": user_query
            })

            # generate bot reply
            response = handle_chat_query(user_query)

            st.session_state.chat_history.append({
                "role": "bot",
                "content": response
            })

            st.rerun()
