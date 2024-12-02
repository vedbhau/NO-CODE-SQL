#  No-Code SQL Project 🛠️🖥️

Welcome to the **No-Code SQL Project**! 🚀 This project allows users to interact with a database and retrieve meaningful answers by simply typing a description of what they want—no need to write SQL queries! 🎉

---

## Features ✨

- **Natural Language Queries:** Just describe what you need in plain English! 📝  
- **Flask-Powered Backend:** Seamlessly handles API calls and user queries. 🌐  
- **LangChain Integration:** Utilizes LangChain for intelligent SQL generation and query execution. 🧠  
- **Groq LPU:** Employs Groq's specialized processors for efficient computation. ⚡  
- **Interactive Web Interface:** User-friendly design built with Flask and HTML. 🎨  
- **SQLite Database:** Comes with a preconfigured SQLite database of students and their details. 🎓

---

## Technology Stack 🛠️

- **Programming Language:** Python 🐍  
- **Frameworks & Libraries:**  
  - Flask (Backend server) 🌐  
  - LangChain (SQL query generation) 🔗  
  - SQLAlchemy (Database interaction) 🗄️  
- **Database:** SQLite 🗂️  
- **API & Models:** Groq API with Llama3-8b 🤖  

---

## Prerequisites 📋

1. Python 3.8+ must be installed.  
2. Required dependencies (listed in `requirements.txt`).  
3. Groq API Key for utilizing Llama3-8b model. 🔑  

---

## Setup Instructions 🛠️

1. **Clone the Repository**  
   ```bash
   git clone <repository-link>
   cd no-code-sql
   ```

2. **Install Dependencies**  
   Use the provided `requirements.txt` file:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database**  
   Run the `sqlite.py` file to create and populate the SQLite database:  
   ```bash
   python sqlite.py
   ```

4. **Run the Flask Application**  
   Launch the Flask server:  
   ```bash
   python app.py
   ```

5. **Access the Web Interface**  
   Open your browser and navigate to:  
   ```
   http://127.0.0.1:5000
   ```

---

## How It Works 💡

1. **Input:** Users enter a natural language description of the query they want to execute (e.g., *"Show me all students in Data Science with marks above 80."*).  
2. **Processing:**  
   - The description is sent to the Flask backend.  
   - LangChain uses the Groq API to convert the description into a valid SQL query.  
3. **Execution:** The generated SQL query is executed on the SQLite database.  
4. **Output:** The results are displayed back to the user on the web interface.

---

## SQLite Database Schema 📋

**Table Name:** `STUDENT`  
| Column Name | Data Type | Description            |  
|-------------|-----------|------------------------|  
| NAME        | VARCHAR   | Name of the student    |  
| CLASS       | VARCHAR   | Class of the student   |  
| SECTION     | VARCHAR   | Section of the student |  
| MARKS       | INT       | Marks obtained         |  

---

## Example Queries 🧑‍💻

1. **Input:**  
   > "List all students in section A."  
   **Output:**  
   ```  
   Krish, Mukesh, Jacob, Dipesh  
   ```

2. **Input:**  
   > "Who scored the highest marks?"  
   **Output:**  
   ```  
   John (100 marks)  
   ```

---

## Dependencies 📦

Refer to the `requirements.txt` file for all dependencies:
- Flask
- LangChain
- SQLAlchemy
- LangChain-Groq
- SQLite  

Install them using:  
```bash
pip install -r requirements.txt
```

---

## Contribution 🤝

Feel free to fork this repository, raise issues, and submit pull requests. Let's make this project even better! ✨

---

## Contact 📧

For queries or feedback, reach out at: **vedmalegaonkar7236@gmail.com**  

Happy querying! 🎉
