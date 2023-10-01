import streamlit
from hack3 import run_llm
from streamlit_chat import message

if "user_prompt_history" not in streamlit.session_state:
    streamlit.session_state["user_prompt_history"]=[]
    
if "chat_answer_history" not in streamlit.session_state:
    streamlit.session_state["chat_answer_history"]=[]
    
if "chat_history" not in streamlit.session_state:
    streamlit.session_state["chat_history"]=[]

streamlit.title("Moveworks Website ChatBot")
streamlit.header("Ask anything related to Moveworks!")
promptshown=streamlit.text_input("Prompt", placeholder="Enter your prompt here...")



if promptshown:
    with streamlit.spinner('Generating reply'):
        generated_response=run_llm(query=promptshown)
        formatted_response=f"{generated_response['result']}"
        streamlit.session_state["user_prompt_history"].append(promptshown)
        streamlit.session_state["chat_answer_history"].append(formatted_response)
        streamlit.session_state["chat_history"].append((promptshown, generated_response['result']))
        
        
if streamlit.session_state["chat_answer_history"]:
    for given_response, user_query in zip(streamlit.session_state["chat_answer_history"], streamlit.session_state["user_prompt_history"]):
        message(user_query, is_user=True)
        message(given_response)
        