###File based todo app
import os
import pathlib
import time
import glob

def display_tasks():
    file_path = get_file_path()
    task_list = next(os.walk(file_path+'/file_based_todo/tasks/'))[2]
    print('Tasks List:')
    print('Tasks   -------------------- File Name')
    for item in task_list:
        with open(file_path+'/file_based_todo/tasks/'+item,'r') as file:
            data = file.readline()
            print(data,'   --------------- ',item)

def ask_fuction():
    print('What you want to do?')
    print('1: Add new Task\n2: Edit a task\n3:Delete a task')
    ask = input('What you want to do: ')
    match ask:
        case '1':
            task = input('Add Your Task: ')
            add_task(task)
        case '3':
            file_name = input('Which file you want to delete? : ')
            if('.txt' in file_name):
                delete_task(file_name)
            else:
                print('Please specifify full name of the file including .txt in the end!')
                ask_fuction()

def get_file_path():
    file_path = str(pathlib.Path().resolve())
    return file_path

def add_task(task):
    if(task !='' and len(task)>5):
        file_name = task[:5].strip()
        file_path = get_file_path()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        full_path = str(file_path+'/file_based_todo/tasks/'+timestr+'-'+file_name+'.txt')
        
        with open(full_path,'w') as file:
            data = file.write(task)
            print('Task Created Successfully!')
            return True
    else:
        print('Please Provide a Valid Operation or make sure task is more than 5 chars long!')

def delete_task(task_name):
    sure = input('Are you sure you want to delete this task: yes/no').lower()
    if(sure == 'yes'):
        file_path = get_file_path()
        if os.path.exists(file_path+'/file_based_todo/tasks/'+task_name):
            os.remove(file_path+'/file_based_todo/tasks/'+task_name)
            print('File',task_name,'deleted successfully!')
        else:
            print("The file does not exist")
    else:
        print('No file Deleted!')
        ask_fuction()


def main():
    display_tasks()
    ask_fuction()

if __name__ == "__main__":
    main()