import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, Numeric
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from datetime import date

# Set your OpenAI API Key
os.environ["OPENAI_API_KEY"] = "sk-proj-XCXZIc1wE6l06ZlUaH_U4XxvQSNMTqJ88aT8juhAWRppZ96sQS178-YaqdpFKWtsWlY5Iwg9v5T3BlbkFJyJ6sRgh0eOlFg7MQc1KeIqlHmGi0TO05uofgBgnEr-Vhtc5AfDv8omjWpWoP3EsL_7t3vqejsASKS"  # replace with your key

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
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
#llm = ChatOpenAI(model="gpt-4", temperature=0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

# Ask a question
question = "List all failed trades for today"
response = agent_executor.run(question)

print("\n--- Result ---")
print(response)
