from task import add_task,view_tasks,update_task,delete_task,complete_task,search_task
while True:
    print("1.Add Task")
    print("2 View Task")
    print("3 Update Task")
    print("4 Delete Task")
    print("5 Complete Task")
    print("6 Show Task")
    print("7 exit")
    choice=int(str(input("Enter choice:")))
    if choice==1:
        add_task()
    elif choice==2:
        view_tasks()
    elif choice==3:
        update_task()
    elif choice==4:
        delete_task()
    elif choice==5:
        complete_task()
    elif choice==6:
        search_task()
    elif choice==7:
        break
