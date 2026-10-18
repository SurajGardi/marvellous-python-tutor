# 🐍 Marvellous Python Tutor

```markdown

An AI-powered Python programming tutor built using **Python, Streamlit, Ollama, and Llama 3.2**.

Marvellous Python Tutor provides an interactive chat interface where users can ask questions related to Python programming and receive AI-generated explanations.

## 🚀 Features

- 🐍 AI-powered Python programming tutor
- 💬 Interactive chat-based interface
- 🤖 Powered by Llama 3.2 through Ollama
- 🌐 Built with Streamlit
- 📱 Mobile-friendly interface
- 🧠 Maintains conversation history during the session
- ⚡ Runs locally using Ollama

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Ollama**
- **Llama 3.2:1b**

## 📁 Project Structure

```text
marvellous-python-tutor/
│
├── marvellous_python_tutor.py
├── requirements.txt
└── README.md
```

## ⚙️ Prerequisites

Before running the project, make sure you have:

- Python installed
- Ollama installed
- `llama3.2:1b` model downloaded

Check Ollama installation:

```bash
ollama --version
```

Check available models:

```bash
ollama list
```

If the model is not available, download it using:

```bash
ollama pull llama3.2:1b
```

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/SurajGardi/marvellous-python-tutor.git
```

Move into the project directory:

```bash
cd marvellous-python-tutor
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Make sure Ollama is running and the `llama3.2:1b` model is available.

Start the Streamlit application:

```bash
streamlit run marvellous_python_tutor.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 💡 Example Questions

You can ask questions such as:

- What is inheritance in Python?
- Explain decorators in Python.
- What is the difference between a list and a tuple?
- Explain Python exception handling.
- How does a Python dictionary work?
- Write a Python program to check whether a number is prime.

## 🧠 How It Works

The application uses Streamlit to provide the web-based chat interface.

The user's question is added to the conversation history and sent to the Ollama-powered Llama 3.2 model.

```text
User
  ↓
Streamlit Chat Interface
  ↓
Conversation History
  ↓
Ollama
  ↓
Llama 3.2:1b
  ↓
AI Response
  ↓
Streamlit Interface
```

## 🔮 Future Improvements

- Add Python code execution
- Add syntax highlighting
- Add conversation export
- Add multiple AI models
- Add persistent chat history
- Deploy the application publicly

## 👨‍💻 Author

**Suraj Gardi**

GitHub: [@SurajGardi](https://github.com/SurajGardi)

---

⭐ If you find this project useful, consider giving it a star!
