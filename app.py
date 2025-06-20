import re
import sqlite3
import pandas as pd
from flask import Flask, request, jsonify,render_template
import openai

app = Flask(__name__)
openai.api_key = "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"
@app.route('/')
def home():
    return render_template("i.html")
@app.route('/generate_query', methods=['POST'])
def generate_query():
    user_input = request.json.get("natural_language")
    prompt = f"""
You are an expert SQL generator.

Given the following 4 tables in the database:

1. `Customer(customerid,firstname,lastname,company,address,city,state,country,postalcode,phone,fax, email)`
2. `playlist(playlistid,playlistname)`
3. 'PlaylistTrack(playlistid,trackid)'
3. `Purchase(invoiceid,trackid,customerid,unitprice)`
4. `Track(trackid,song,artist,album,media_type,genre,Bytes)`

Generate an SQL query that answers this user request:
\"{user_input}\"

Only return valid SQL code. Do not explain anything.
Use JOINs and aggregations when necessary.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    query_result = response["choices"][0]["message"]["content"].strip()
    print("Generated SQL query:", query_result)

    match = re.search(r"(SELECT[\s\S]*);?", query_result, re.IGNORECASE)
    if not match:
        return jsonify({
            "query": query_result,
            "error": "Only SELECT queries are supported.",
            "results": None
        })

    query_result = match.group(1)
    print("Executing query:", query_result)

    conn = sqlite3.connect("test2.db")
    try:
        df = pd.read_sql_query(query_result, conn)
        print(df)
        results_json = df.to_dict(orient="records")
    except Exception as e:
        print("SQL query error:", e)
        conn.close()
        return jsonify({
            "query": query_result,
            "error": str(e),
            "results": None
        })

    conn.close()

    return jsonify({
        "query": query_result,
        "results": results_json
    })

if __name__ == '__main__':
    app.run(debug=True)
