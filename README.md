# 🤖 Goodness Medical Center – AI-Powered Medical Chatbot

Welcome to the official repository for the **AI-Powered Medical Chatbot** developed for **Goodness Medical Center**. This chatbot assists patients with health-related questions, provides information about the hospital, and enables users to **book medical appointments** seamlessly.

## 🩺 Project Description

This chatbot is designed to improve patient engagement and streamline support services by offering:

- 💬 **Natural Conversations** on medical topics  
- 🏥 **Hospital Service Guidance**  
- 📅 **Appointment Booking System**  
- 🧠 Powered by **Google's Generative AI API**  
- 🌐 Deployed using **Streamlit** for a clean and interactive user interface  

## 🚀 Demo

You can launch and interact with the chatbot via the Streamlit interface locally or deploy it on a platform like Streamlit Cloud or Hugging Face Spaces.

## 🛠️ Tech Stack

- **Python 3.10+**
- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- Streamlit Form for appointment inputs
- Custom logic for appointment scheduling

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/goodness-medical-chatbot.git
   cd goodness-medical-chatbot
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set your API key (Google Generative AI):
Create a .env file and add:

env
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
📋 Features
✅ Health-related chatbot responses using LLMs

✅ Easy appointment booking with time and date input

✅ Real-time chatbot interaction with patients

✅ Clean and mobile-friendly UI using Streamlit

📁 Project Structure
bash
Copy
Edit
goodness-medical-chatbot/
│
├── app.py                  # Main Streamlit application
├── chatbot.py              # Handles chat logic with Generative AI
├── appointment.py          # Logic for booking appointments
├── requirements.txt        # Python dependencies
├── .env                    # API key configuration (not pushed)
└── README.md               # Project documentation
🔐 Environment Variables
Ensure your .env file contains the following:

env
Copy
Edit
GOOGLE_API_KEY=your_google_api_key
🙌 Acknowledgements
Google Generative AI

Streamlit

Medical experts at Goodness Medical Center for their valuable input
