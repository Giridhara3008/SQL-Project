## NL2SQL Generator
A Natural Language to SQL generator that converts human language questions into executable SQL queries using OpenAI's language models. Designed to work with multiple relational database tables (e.g., `Customer`, `Track`, `Purchase`, `Playlist`).

##  Features
Converts plain English queries into valid SQL
Supports multi-table JOINs and complex filtering
Powered by OpenAI GPT (gpt-3.5-turbo / gpt-4)
Works with SQLite databases out of the box
Simple Flask web interface or API for testing

##  Tech Stack

- **Backend:** Python, Flask
- **LLM Integration:** OpenAI API
- **Database:** SQLite
- **Frontend (optional):** HTML + JS (or Postman for API)

##  Project Structure
nl2sql-generator/
app.py # Main Flask app
database/ # Folder containing SQLite .db file
      test.db and test2.db
data/ # Optional CSVs for table import
templates/ # HTML templates (if UI included)
README.md
## Steps to do the project
Install all requirements.txt and set up python virtual environment using venv. Built all required codes in app.py and run in the localhost.

##  How It Works

1. User submits a natural language question (e.g., "Show customers who purchased rock songs").
2. Backend formats the prompt with table schema and sends it to OpenAI's API.
3. Model returns the corresponding SQL query.
4. SQL is optionally executed on the SQLite database, and results are returned.

##  Setup Instructions

### 1. Clone the Repository
git clone https://github.com/yourusername/nl2sql-generator.git
cd nl2sql-generator

# For running use the link
http://127.0.0.1:5000

## Conclusion
The NL2SQL Generator bridges the gap between non-technical users and databases by allowing natural language queries to be translated into SQL seamlessly. Whether you're analyzing customer data, tracking purchases, or exploring playlists, this tool empowers users to access insights without writing a single line of SQL.

Built with extensibility in mind, it’s easy to integrate with new databases, fine-tune prompts, and expand functionality. This project is a strong foundation for future development in AI-powered data querying, BI tools, or low-code platforms.

## Knowledge Gained
Working on the Natural Language to SQL Generator project provided valuable hands-on experience in several key areas of software development, AI integration, and data management.
Language Models & Prompt Engineering:
Learned how to design effective prompts for LLMs (like GPT-3.5/4) to reliably convert natural language into valid SQL queries.
Understood the importance of context, schema injection, and constraint-based instructions in prompt design.
Backend Development:
Built a robust Flask API to receive NL inputs, send them to OpenAI, and execute the returned SQL safely.
Implemented database connectivity with SQLite and used pandas for easy data previewing and validation.




