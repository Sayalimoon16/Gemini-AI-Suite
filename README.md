# 🧠 Gemini AI Suite — Multimodal AI Assistant

An interactive **multimodal Generative AI application** built using **Google Gemini API** and **Streamlit**, supporting text chat, image understanding, embeddings generation, and voice interaction in a unified dashboard.

---

## 🚀 Features

* 💬 **AI ChatBot** — Conversational assistant powered by Gemini
* 🖼️ **Image Captioning** — Describe uploaded images using vision AI
* 🔡 **Text Embeddings** — Generate semantic vectors from text
* ❓ **Ask Anything** — General AI Q&A interface
* 🎤 **Voice Assistant** — Speech-to-text + AI + text-to-speech
* 📊 **Embedding Inspector** — Vector preview and statistics

---

## 🧠 Tech Stack

* **LLM / Vision / Embeddings:** Google Gemini API
* **Frontend:** Streamlit
* **Speech Recognition:** SpeechRecognition
* **Text-to-Speech:** pyttsx3
* **Image Processing:** Pillow
* **UI Components:** streamlit-option-menu

---

## 📸 Screenshots

> Add screenshots after deployment

* Chat Interface
* Image Captioning
* Embeddings Dashboard
* Voice Assistant

---

## ⚙️ Installation

### 1️⃣ Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Gemini_chatbot-main.git
cd AI_Gemini_chatbot-main
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Create a **Google Gemini API key**:
https://aistudio.google.com/app/apikey

Create `config.json` in project root:

```json
{
  "GOOGLE_API_KEY": "YOUR_API_KEY"
}
```

> ⚠️ Never commit API keys to GitHub

---

## ▶️ Run App

```bash
streamlit run main.py
```

Open in browser:
http://localhost:8501

---

## 🧪 Example Use Cases

* Conversational AI assistant
* Image understanding demo
* Semantic search / RAG embeddings
* Voice-enabled chatbot
* Multimodal AI interface

---

## 📊 Embedding Details

Model: `models/gemini-embedding-001`
Vector dimension: **3072**
Task: semantic representation

---

## 🏗️ Project Structure

```
AI_Gemini_chatbot-main/
│
├── main.py
├── gemini_utility.py
├── config.json
├── requirements.txt
├── README.md
└── assets/
```

---

## 🌟 Future Improvements

* PDF Chat (RAG)
* Semantic similarity search
* Continuous voice conversation
* Deployment on Streamlit Cloud
* Dark theme UI

---

## 👩‍💻 Author

**Sayali Moon**
AI / ML Enthusiast

* GitHub: https://github.com/Sayalimoon16
* LinkedIn: https://www.linkedin.com/in/sayali-moon

---

## 📜 License

This project is for educational and portfolio purposes.
