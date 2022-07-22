# InstaWork__Project_API
A POC for internship at Instawork Developed by Arjun Haridas email address: - arjunhari8098@gmail.com
#This project was developed using djang_rest_framework, python3, sqlLite.

<--------------Build and run application------------------>
1.prerequisite needed: - Python3 , django_rest_framework, python virtual environment.
2.Export project from git.
3.Run the command python -m venv django_env from inside your projects folder to create the virtual environment if not created. 
note: - virtual enivironment folder for windows has already been uploaded in git, so all dependencies used to develop will be there.
4.Then, run command for windows devices (<source path>\instaWork_rest\.venv\Scripts\activate) or (source ./django_env/bin/activate for mac ) to turn it on from employee root folder path.
5.Run python manage.py runserver command from terminal in virtual enivironment mode to get server up.
6.If not running, please do follow up steps to migrate and reconfigure project.
7.run python manage.py migrate
8.run python manage.py createsuperuser to attain admin privilages (optional steps)
9. Run python manage.py makemigrations and python manage.py migrate
10.Then run python manage.py runserver command.

<---------------------------Testing using Postman--------------------------------->
For testing from postman use follwoing url
1.Get method-  http://127.0.0.1:8000/getTeam  (for viewing team members)
2.Post method-  http://127.0.0.1:8000/getTeam/ (for inserting team member)
  post request body: -
   {
    "firstName": "govind",
    "lastName": "vijaya",
    "email": "pa@gmail.com",
    "role": "regular"
  }
 3.Put Method-  http://127.0.0.1:8000/delOrUpdate/<id> (for editing team member)
  put method body: -
   {
    "id": 1,
    "firstName": "arjun",
    "lastName": "haridas",
    "email": "arjungate2@gmail.com",
    "role": "admin"
  }
 4. Delete method-  http://127.0.0.1:8000/delOrUpdate/<id> (for deleting team member)
 
 Note: - Make sure django project is up when testing UI/ angular project
 
 


