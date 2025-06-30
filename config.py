# --- Chatbot Configuration ---
CHATBOT_NAME = "Goodness Medical Center"
HOSPITAL_WEBSITE = "https://www.examplehospital.com" # Placeholder URL
HOSPITAL_PHONE = "123-456-7890" # Placeholder Phone Number

# --- Gemini Configuration ---
GEMINI_MODEL_NAME = "gemini-2.0-flash"
# The API key will be automatically provided by the Canvas environment if left empty.
GEMINI_API_KEY = "AIzaSyAufwJ4A5n3D5dKe-KQhqjfSId0F6S3uy4" # Leave empty for Canvas environment

# --- Knowledge Base (Simplified for demonstration) ---
# In a real application, this could be loaded from a database, CSV, or external API.
STATIC_KNOWLEDGE_BASE = {
    "visiting hours": "Our general visiting hours are from 9:00 AM to 8:00 PM daily. Specific department hours may vary. Which department are you interested in?",
    "appointment booking": f"To book a new appointment, please visit our online booking portal at {HOSPITAL_WEBSITE}/appointments or call our scheduling department at {HOSPITAL_PHONE} during business hours.",
    "reschedule appointment": f"To reschedule or cancel an existing appointment, please log in to your patient portal at {HOSPITAL_WEBSITE}/patient-portal or call {HOSPITAL_PHONE}.",
    "insurance": f"We accept a wide range of insurance plans. Please visit our website at {HOSPITAL_WEBSITE}/insurance or call our billing department at {HOSPITAL_PHONE} for a detailed list.",
    "emergency room": "The Emergency Room is located on the ground floor, accessible via the main hospital entrance. Please follow the signs for 'Emergency' once inside. *In a medical emergency, please call 911 immediately.*",
    "medical records": f"You can access your medical records through our secure patient portal at {HOSPITAL_WEBSITE}/patient-portal. If you need further assistance, please contact our Medical Records Department at {HOSPITAL_PHONE}.",
    "directions": f"You can find detailed directions to our hospital on our website: {HOSPITAL_WEBSITE}/directions. Our address is [Hospital Address, e.g., 123 Health St, Anytown, USA].",
    "services": f"We offer a comprehensive range of medical services including Cardiology, Pediatrics, Oncology, Orthopedics, and more. You can view a full list on our website: {HOSPITAL_WEBSITE}/services.",
    "feedback": f"We value your feedback. Please submit your comments or complaints through our feedback form on {HOSPITAL_WEBSITE}/feedback or by calling {HOSPITAL_PHONE}.",
    "parking": f"Parking is available in our multi-story parking garage located next to the main entrance. Fees apply. Please see {HOSPITAL_WEBSITE}/parking for rates.",
    "registration": f"Information on patient registration, including required documents, can be found on our website: {HOSPITAL_WEBSITE}/registration. You can also complete pre-registration online.",
    "doctor search": f"To find a doctor by specialty or name, please use our 'Find a Doctor' tool on our website: {HOSPITAL_WEBSITE}/find-a-doctor."
}

# --- Chatbot Persona and Instructions for LLM ---
# This prompt guides the LLM on how to behave as a hospital chatbot.
# It's crucial for ensuring the bot stays within its defined scope and limitations.
GEMINI_SYSTEM_INSTRUCTIONS = f"""
You are {CHATBOT_NAME}, a helpful and professional AI assistant for a hospital.
Your primary goal is to provide accurate, general information about hospital services,
visiting hours, appointments, insurance, directions, and common FAQs.

*Crucial Guidelines:*
1.  *DO NOT provide medical advice, diagnosis, or treatment.* If a user asks for medical advice or describes symptoms, always respond with a disclaimer like: "I am an AI chatbot and cannot provide medical advice, diagnosis, or treatment. If you are experiencing symptoms or have a medical concern, please consult a qualified healthcare provider. For emergencies, please call 911 immediately."
2.  *DO NOT ask for or store any sensitive personal health information (PHI) or personal identifiers.*
3.  *Prioritize factual information related to hospital operations.*
4.  If you cannot answer a question directly, politely suggest contacting the hospital directly at {HOSPITAL_PHONE} or visiting {HOSPITAL_WEBSITE}.
5.  Keep responses concise and clear.
6.  Maintain a reassuring and professional tone.
"""