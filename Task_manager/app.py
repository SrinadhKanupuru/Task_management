from flask import Flask,jsonify,request
from flask_cors import CORS
from db import cursor,mydb
app=Flask(__name__)
CORS(app)
@app.route("/task")


def get_tasks():
    query="select * from task"
    cursor.execute(query)
    data=cursor.fetchall()
   
    return jsonify(data)


@app.route("/update-task/<int:id>",methods=["PUT"])
def update_task(id):
    data=request.get_json()
    new_task=data.get("task_name")
    query="update task set task_name=%s where id=%s"
    values=(new_task,id)
    cursor.execute(query,values)
    mydb.commit()
    
    return jsonify({"message":"Task update successfully"})

app.run(debug=True)

