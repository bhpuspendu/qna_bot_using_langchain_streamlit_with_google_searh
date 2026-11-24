from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
import streamlit as st


load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b", streaming=True)
serper = GoogleSerperAPIWrapper()
memory = MemorySaver()


st.subheader("🤖 Ask, I am here to answer")
st.markdown("This is a simple QnA Chatbot that has the ability to google search.")

if "histories" not in st.session_state:
    st.session_state.histories = []
    st.session_state.memory = memory
    
agent = create_agent(
    model=model,
    tools=[serper.run],
    system_prompt="You are an expert agent to answer any query with the help of google search.",
    checkpointer=st.session_state.memory
)

for history in st.session_state.histories:
    st.chat_message(history['role']).markdown(history['content'])


query = st.chat_input("Ask me anything...")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.histories.append({"role": "user", "content": query})
    resp = agent.stream({"messages": [{"role": "user", "content": query}]}, {"configurable": {"thread_id": "pbh786"}}, stream_mode="messages")
    
    ai_container = st.chat_message("ai")
    with ai_container:
        space = st.empty()
        message = ''
        for chunk in resp:
            message += chunk[0].content # pyright: ignore[reportArgumentType]
            space.write(message)
        
        st.session_state.histories.append({"role": "ai", "content": message})
    
    