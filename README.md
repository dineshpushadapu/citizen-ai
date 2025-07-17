
<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="60"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" width="60"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-plain.svg" width="60"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="60"/>
</div>

# 🚀 CitizenAI

> **Empowering citizens with AI-driven insights, feedback analytics, and a beautiful, interactive experience.**

---

## ✨ Features

✅ **AI Chat Assistant** — Ask questions and get intelligent, context-aware answers powered by IBM Granite or Gemini (configurable).

✅ **Feedback & Sentiment Analysis** — Submit feedback on responses; sentiment (positive, neutral, negative) is detected and stored in MongoDB.

✅ **Animated Dashboard Analytics** — View real-time, animated stats and sentiment percentages for all feedback.

✅ **Authentication** — Secure login and signup system (local auth).

✅ **Modern UI/UX** — Responsive design with Tailwind CSS, gradients, and Lottie animations for a delightful user experience.

---

## 🛠️ Tech Stack

| Layer      | Technology                                      |
|------------|-------------------------------------------------|
| Backend    | Python, Flask                                   |
| Frontend   | Tailwind CSS
| AI Models  | HuggingFace Transformers (IBM Granite) / Gemini |
| Database   | MongoDB                                         |

---

## ⚡ Quickstart

### 1. Clone the Repository
```powershell
git clone <your-repo-url>
cd citizen-ai
```

### 2. Create a Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Environment Variables

- For **Gemini**: Create a `.env` file in the root directory and add:
  ```env
  GEMINI_API_KEY=your_gemini_api_key
  ```
- For **IBM Granite**: No API key needed, but ensure you have access to the model via HuggingFace.

### 5. MongoDB Setup
- Make sure MongoDB is running locally or update the connection string in `database/db.py` to point to your MongoDB instance.

### 6. Run the App
```powershell
python app.py
```
- The app will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📁 File Structure

```text
citizen-ai/
│   app.py
│   config.py
│   requirements.txt
│
├── models/
│     chat_model.py
│     sentiment_model.py
│
├── routes/
│     auth_routes.py
│     chat_routes.py
│     dashboard_routes.py
│     main_routes.py
│     sentiment_routes.py
│
├── database/
│     db.py
│     user_model.py
│
├── static/
│     css/
│         styles.css
│
├── templates/
│     index.html
│     about.html
│     chat.html
│     dashboard.html
│     login.html
│     signup.html
│
└── utils/
      text_cleaning.py
```

---

## 🎨 Customization

- To switch between Gemini and IBM Granite, update the logic in `models/chat_model.py`.
- UI/UX can be further customized via Tailwind CSS and the templates in the `templates/` folder.

---

## 📜 License

MIT License

---

## 🙏 Credits

- Built with [Flask](https://flask.palletsprojects.com/), [Tailwind CSS](https://tailwindcss.com/), [LottieFiles](https://lottiefiles.com/), [HuggingFace Transformers](https://huggingface.co/docs/transformers/index), and [MongoDB](https://www.mongodb.com/).
