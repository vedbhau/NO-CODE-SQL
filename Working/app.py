from flask import Flask, request, jsonify, render_template
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from sqlalchemy import create_engine
import sqlite3
from pathlib import Path
from langchain_groq import ChatGroq

app = Flask(__name__)

# Path to SQLite database
DB_FILEPATH = (Path(__file__).parent / "student.db").absolute()

# Function to configure SQLite3 database
def configure_db():
    creator = lambda: sqlite3.connect(f"file:{DB_FILEPATH}?mode=ro", uri=True)
    return SQLDatabase(create_engine("sqlite:///", creator=creator))

# Initialize the SQLite database
db = configure_db()

# Initialize LangChain toolkit and agent
def initialize_agent(api_key):
    llm = ChatGroq(groq_api_key="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", model_name="Llama3-8b-8192", streaming=False)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    return create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
    )

@app.route("/")
def home():
    return render_template("index.html")  # Ensure you have an `index.html` for the UI

@app.route("/query", methods=["POST"])
def query_db():
    try:
        api_key = request.json.get("api_key")
        user_query = request.json.get("query")

        if not api_key:
            return jsonify({"error": "API key is required"}), 400
        if not user_query:
            return jsonify({"error": "Query is required"}), 400

        agent = initialize_agent(api_key)
        response = agent.run(user_query)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
