import streamlit as st
from gpt import gpt_chat
from database import add_to_db, get_next_question_document, update_next_review_time_based_on_difficulty

#True if you want to add new questions to your db. The new questions must be inside some txt file
add_to_db(False)

col1, col2 = st.columns([7,2])

if "study_mode" not in st.session_state:
    st.session_state["study_mode"] = False

if "free_chat_mode" not in st.session_state:
    st.session_state["free_chat_mode"] = False

if "text_box_content" not in st.session_state:
    st.session_state["text_box_content"] = ""
    
if "mode_selected" not in st.session_state:
    st.session_state["mode_selected"] = False

st.markdown("<h1 style='text-align: center; color: white;'>StudyGPT</h1>", unsafe_allow_html=True)

if not st.session_state["mode_selected"]:
    st.markdown("<div style='text-align: center; color: white;'>Welcome to StudyGPT, your personalized learning and knowledge exploration tool! StudyGPT is a unique platform that harnesses the power of GPT-3.5, OpenAI's cutting-edge large language model, to facilitate effective learning through a carefully crafted spaced repetition algorithm. This algorithm strategically calculates the optimal time for your next review, ensuring long-term retention and efficient learning. In addition to this, the platform's 'Free Chat Mode' gives you direct access to interact with the GPT-3.5 model for general knowledge queries or complex discussions. Select your mode and dive into the future of personalized learning with StudyGPT, where mastering new materials is just as easy as chatting!</div>", unsafe_allow_html=True)
    st.write(" ")
    st.image('../resources/logo1.png',width=700)
    
with col1: 
    if st.button("Start Study Mode") or st.session_state["study_mode"]:
        st.session_state["study_mode"] = True
        st.session_state["free_chat_mode"] = False
        
with col2: 
    if st.button("Free Chat Mode") or st.session_state["free_chat_mode"]:
        st.session_state["free_chat_mode"] = True
        st.session_state["study_mode"] = False

st.session_state["mode_selected"] = True

if st.session_state["study_mode"]:
    
    st.write("Study Mode Activated")

    question_document = get_next_question_document()
    
    question_text = question_document["text"]
    
    st.write(question_text)
    
    st.session_state["text_box_content"] = st.text_input("Enter your answer: ", value=st.session_state["text_box_content"])
    enter_button = st.button("Enter")
    
    if enter_button and st.session_state["text_box_content"]:
        gpt_response = gpt_chat(question_text + " " + "This is my answer, please tell me if its correct and give me the most consice answer: " + st.session_state["text_box_content"])
        st.write(f"GPT's Response: {gpt_response}")
        st.session_state["text_box_content"] = ""
        
        difficulty = st.selectbox("Choose difficulty", ["easy", "medium", "hard"])
        if difficulty:
            update_next_review_time_based_on_difficulty(question_document["_id"], difficulty)

elif st.session_state["free_chat_mode"]:
    text_box = st.text_input("Enter your chat:")
    enter_button = st.button("Enter")
    if enter_button and text_box:
        st.write(f"GPT's Response: {gpt_chat(text_box)}")



