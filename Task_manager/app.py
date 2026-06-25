from flask import Flask,jsonify
from db import cursor
app=Flask(__name__)
@app.route("/task")

def get_tasks():
    query="select * from task"
    cursor.execute(query)
    data=cursor.fetchall()
   
    return jsonify(data)
app.run(debug=True)