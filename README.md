# HyperionDev Chatbot: Flask Random Response App

This is a beginner-friendly Flask web application that acts as a simple chatbot. Users can type a message, and the app responds with a random sentence from a predefined list or dynamically generated sentences using the **Wonderwords** library.

---

## 📜 **Project Overview**

The project demonstrates how to:
1. Build a **Flask-based backend** for handling user input.
2. Use a modular approach to manage random sentence generation in `sentence_selector.py`.
3. Use the **Wonderwords library** to dynamically generate sentences.
4. Create a responsive and clean web interface using **Bootstrap**.

---

## 💻 **Technologies Used**
- **Python (Flask)** – For backend logic and routing.
- **Wonderwords** – For generating random sentences dynamically.
- **HTML/CSS/Bootstrap** – For the frontend user interface.

---

## 🚀 **Getting Started**

Follow the steps below to set up and run the project on your local machine.

### 1️⃣ **Prerequisites**

Make sure you have the following installed:
- Python (version 3.6 or higher)
- pip (Python package manager)

---

### 2️⃣ **Project Setup**

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/hyperiondev-chatbot.git
   cd hyperiondev-chatbot
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install flask wonderwords
   ```

---

### 3️⃣ **Running the Application**

1. Run the Flask app:
   ```bash
   python app.py
   ```

2. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

3. Type a message in the **"Say something"** input field and click **Submit**. The app will respond with a random sentence.

---

## 🛠️ **Project Structure**

```
flask_chatbot_app/
│
├── static/
│   └── styles.css         # Custom CSS styles
│
├── templates/
│   └── index.html         # Frontend HTML file with Bootstrap
│
├── __init__.py            # Flask app initialization (optional for modularization)
├── app.py                 # Main backend Flask app
└── sentence_selector.py   # Logic for random sentence generation
```

---

## 🎨 **Screenshot**

![Chatbot Screenshot](screenshot.png)

---

## 📦 **Dependencies**

- **Flask**: Web framework for Python.
- **Wonderwords**: Library for generating random sentences.
- **Bootstrap**: Frontend library for responsive UI.

---

## 🧩 **About `sentence_selector.py`**

The file `sentence_selector.py` is responsible for handling the logic of random sentence generation. It makes the project more modular by separating core logic from the Flask app.

**Example content of `sentence_selector.py`:**
```python
import random
from wonderwords import RandomSentence

random_sentence_generator = RandomSentence()

def get_random_sentence():
    predefined_sentences = ["Hello", "How are you?", "I am HD"]
    generated_sentence = random_sentence_generator.sentence()
    all_sentences = predefined_sentences + [generated_sentence]
    return random.choice(all_sentences)
```

---

## 🧑‍💻 **Contributing**

Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch:  
   ```bash
   git checkout -b my-new-feature
   ```
3. Make your changes and test them.
4. Commit and push to your branch:  
   ```bash
   git commit -m "Add some feature"
   git push origin my-new-feature
   ```
5. Open a Pull Request.

---

## 📄 **License**

This project is licensed under the MIT License.

---

## 🌟 **Acknowledgments**

Thanks to **HyperionDev** for inspiring this beginner-friendly project idea! 🎉
