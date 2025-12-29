import streamlit as st
st.set_page_config(page_title="medibot2.0 beta version",layout="wide")

st.title("🩺Medibot- Medical Study Assistant(Beta Version)")

st.write("This is beta version.Features will be added step by step")

tab_chat,tab_notes,tab_uploads,tab_viva=st.tabs(["💬 Chat Assistant","📝Notes","📁Uploads","🎤Viva Mode"])

with tab_chat:
    st.subheader("💬 Chat Assistant")

    user_query=st.text_input("Ask a topic/concept(academic use only)")
    if st.button("Submit Query"):
        if user_query.strip()=="":
            st.warning("Please enter a question first.")
        else:
            st.info("AI responses will appear here (logic coming next)")
            st.write(f"**You asked:**{user_query}")
            st.write("Processing...(placeholder)_")