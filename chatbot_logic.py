import google.generativeai as genai
import config # Import the config file

# Configure the Gemini API
# The API key is automatically provided by the Canvas environment if left empty in config.py
genai.configure(api_key=config.GEMINI_API_KEY)

# Initialize the Gemini model
# Using 'gemini-2.0-flash' as specified in the instructions.
# The system_instruction is crucial for guiding the model's behavior.
model = genai.GenerativeModel(
    model_name=config.GEMINI_MODEL_NAME,
    system_instruction=config.GEMINI_SYSTEM_INSTRUCTIONS
)

# --- Function to get response from Gemini ---
def get_gemini_response(query):
    """
    Sends a query to the Gemini model and returns its response.
    Includes error handling for API calls.
    """
    try:
        # For a simple Q&A, we can use generate_content directly.
        # For multi-turn conversations, you'd use model.start_chat().
        response = model.generate_content(query)
        # Access the text from the first part of the first candidate
        if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
            return response.candidates[0].content.parts[0].text
        else:
            return "I couldn't generate a response at this moment. Please try again."
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return (
            "I'm currently experiencing technical difficulties and cannot provide an intelligent response. "
            "Please try again later or contact the hospital directly."
        )

# --- Main Chatbot Response Logic ---
def get_chatbot_response(user_query):
    """
    Determines the chatbot's response based on the user query.
    Prioritizes hardcoded rules, then medical disclaimers, then Gemini.
    """
    user_query_lower = user_query.lower().strip()

    # 1. --- Emergency Information (Highest Priority) ---
    emergency_keywords = ["emergency", "urgent", "911", "ambulance", "critical"]
    if any(keyword in user_query_lower for keyword in emergency_keywords):
        return config.STATIC_KNOWLEDGE_BASE["emergency room"]

    # 2. --- Symptom Checker / Medical Advice Disclaimer ---
    # Keywords indicating a potential medical advice query
    medical_keywords = ["symptom", "pain", "fever", "cough", "sick", "diagnose", "treatment", "what should i do", "my head hurts", "i feel unwell"]
    if any(keyword in user_query_lower for keyword in medical_keywords):
        return (
            "I am an AI chatbot and *cannot provide medical advice, diagnosis, or treatment*. "
            "If you are experiencing symptoms or have a medical concern, please consult a qualified healthcare provider. "
            "For emergencies, please call 911 immediately."
        )

    # 3. --- General Information Lookup (from static knowledge base) ---
    # Check for direct matches in our predefined knowledge base first
    for keyword, response in config.STATIC_KNOWLEDGE_BASE.items():
        if keyword in user_query_lower:
            return response

    # 4. --- Fallback to Gemini for Intelligent Responses ---
    # If no specific rule or static knowledge base entry matches, use Gemini.
    # Add a loading indicator in the Streamlit app when calling this.
    return get_gemini_response(user_query)