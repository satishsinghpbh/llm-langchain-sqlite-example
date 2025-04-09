# llm-langchain-sqlite-example

Let's build a fully working natural language to SQL GenAI assistant using an in-memory database — so you can test everything locally without needing a DB2 instance yet.

We'll use:

🧠 OpenAI (GPT-4 or 3.5)

🛢️ SQLite in-memory DB

🧱 LangChain

🖥️ Streamlit (optional UI)

✅ What You’ll Get:
Ask questions like:

“Show all failed trades for today”

And get answers like:

“Here are 2 failed trades today: Trade ID 1001 from client ABC for $1.5M…”

📦 Step 1: Install Dependencies
bash
Copy
Edit
pip install openai langchain sqlalchemy streamlit
🧠 Step 2: Python Code (In-Memory Trade Assistant)
Save this as nl_sql_assistant.py:

python
Copy
Edit
import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, Numeric
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from datetime import date

# Set your OpenAI API Key
os.environ["OPENAI_API_KEY"] = "sk-..."  # replace with your key

# Create in-memory SQLite DB
engine = create_engine("sqlite:///:memory:")
metadata = MetaData()

# Define trade_instructions table
trade_instructions = Table(
    "trade_instructions", metadata,
    Column("trade_id", Integer, primary_key=True),
    Column("client_name", String),
    Column("trade_status", String),
    Column("instruction_type", String),
    Column("settlement_date", Date),
    Column("amount", Numeric)
)

metadata.create_all(engine)

# Insert dummy trades
with engine.begin() as conn:
    conn.execute(trade_instructions.insert(), [
        {"trade_id": 1001, "client_name": "Citi", "trade_status": "FAILED", "instruction_type": "SELL", "settlement_date": date.today(), "amount": 1500000.00},
        {"trade_id": 1002, "client_name": "JPMorgan", "trade_status": "PENDING", "instruction_type": "BUY", "settlement_date": date.today(), "amount": 3000000.00},
        {"trade_id": 1003, "client_name": "Goldman Sachs", "trade_status": "COMPLETED", "instruction_type": "SELL", "settlement_date": date.today(), "amount": 500000.00},
    ])

# Connect to LangChain DB wrapper
db = SQLDatabase(engine=engine)

# LLM setup
llm = ChatOpenAI(model="gpt-4", temperature=0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

# Ask a question
question = "List all failed trades for today"
response = agent_executor.run(question)

print("\n--- Result ---")
print(response)
▶️ Run the App
bash
Copy
Edit
python nl_sql_assistant.py
You’ll see GPT convert your question into SQL, execute it on the in-memory DB, and return readable results.

💻 Optional Streamlit UI
Add this to app.py:

python
Copy
Edit
import streamlit as st

st.title("GenAI Trade Query Assistant")

user_input = st.text_input("Ask a trade-related question")

if user_input:
    response = agent_executor.run(user_input)
    st.write(response)
Then run:

bash
Copy
Edit
streamlit run app.py
🔧 What Next?
Replace in-memory SQLite with DB2 connection

Add more tables and relationships

Restrict destructive queries (UPDATE/DELETE)

Add a query approval layer
