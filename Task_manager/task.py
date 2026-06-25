from db import mydb,cursor
import datetime
def add_task():

    task=input("enter task:")
    status="pending"
    today=datetime.date.today()
    query="insert into task(task_name,status,created_at) values(%s,%s,%s)"
    values=(task,status,today)
    cursor.execute(query,values)
    mydb.commit()
    print("task added successfully")
add_task()

def view_tasks():
    query="select * from task"
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print(i)
view_tasks()

def update_task():
    task_id=int(input("Enter the id:"))
    new_task=input("Enter new task:")
    query="update task set task_name=%s where id=%s"
    value=(new_task,task_id)
    cursor.execute(query,value)
    mydb.commit()
    print("task update successfully")
update_task()

def delete_task():
    task_id=int(input("Enter task id:"))
    query="delete from task where id=%s"
    values=(task_id,)
    mydb.commit()
    cursor.execute(query,values)
    print("deleted task successfully")
delete_task()

def complete_task():
    task_id=int(input("Enter task id:"))
    query="update task set status=%s where id=%s"
    values=("completed",task_id)
    cursor.execute(query,values)
    mydb.commit()
    print("completed successfully")
complete_task()
 
def search_task():
    task_id=int(input("Enter task id:"))
    query="select * from task where id=%s"
    values=(task_id,)
    cursor.execute(query,values)
    data=cursor.fetchone()
    print(data)
search_task()