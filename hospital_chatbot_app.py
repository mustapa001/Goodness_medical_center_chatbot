import streamlit as st
import config # Import the configuration
import chatbot_logic # Import the chatbot logic

# --- Streamlit App Layout ---
st.set_page_config(page_title=f"{config.CHATBOT_NAME} - Hospital Chatbot", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    body {
        font-family: 'Inter', sans-serif;
    }
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-family: 'Inter', sans-serif;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 1px solid #ccc;
        padding: 10px;
    }
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        font-size: 16px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .chat-message {
        background-color: #e6e6e6;
        padding: 10px 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        max-width: 80%;
        word-wrap: break-word; /* Ensure long words wrap */
    }
    .user-message {
        background-color: #d4edda; /* Light green */
        align-self: flex-end;
        margin-left: auto;
    }
    .bot-message {
        background-color: #e0f2f7; /* Light blue */
        align-self: flex-start;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        max-height: 400px;
        overflow-y: auto;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 10px;
        margin-bottom: 20px;
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title(f"🏥 Welcome to {config.CHATBOT_NAME}!")
st.markdown("Your friendly AI assistant for hospital information.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "bot", "content": f"Hello! I'm {config.CHATBOT_NAME}. How can I assist you today?"})

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-message user-message">*You:* {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message bot-message">{config.CHATBOT_NAME}:** {message["content"]}</div>', unsafe_allow_html=True)

# User input
user_input = st.text_input("Type your message here...", key="user_input")

if st.button("Send", key="send_button"):
    if user_input:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get bot response using the logic from chatbot_logic.py
        with st.spinner("Thinking..."): # Add a loading indicator
            bot_response = chatbot_logic.get_chatbot_response(user_input)
        st.session_state.messages.append({"role": "bot", "content": bot_response})

        # Clear the input box and rerun to update chat history
        st.rerun() # Changed from st.experimental_rerun()

# Optional: Provide some common queries as buttons
st.markdown("---")
st.markdown("### Quick Questions:")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Visiting Hours", key="btn_visiting_hours"):
        st.session_state.messages.append({"role": "user", "content": "What are the visiting hours?"})
        with st.spinner("Thinking..."):
            st.session_state.messages.append({"role": "bot", "content": chatbot_logic.get_chatbot_response("What are the visiting hours?")})
        st.rerun() # Changed from st.experimental_rerun()
with col2:
    if st.button("Book Appointment", key="btn_book_appointment"):
        st.session_state.messages.append({"role": "user", "content": "How do I book an appointment?"})
        with st.spinner("Thinking..."):
            st.session_state.messages.append({"role": "bot", "content": chatbot_logic.get_chatbot_response("How do I book an appointment?")})
        st.rerun() # Changed from st.experimental_rerun()
with col3:
    if st.button("Emergency Info", key="btn_emergency_info"):
        st.session_state.messages.append({"role": "user", "content": "Where is the emergency room?"})
        with st.spinner("Thinking..."):
            st.session_state.messages.append({"role": "bot", "content": chatbot_logic.get_chatbot_response("Where is the emergency room?")})
        st.rerun() # Changed from st.experimental_rerun()

st.markdown("---")
st.markdown(
    f"""
    *Disclaimer:* This chatbot provides general information only and is not a substitute for professional medical advice, diagnosis, or treatment.
    Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
    For emergencies, please call 911 immediately.
    """
)