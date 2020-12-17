# E-Assignment
Online Assignment Application for Student and Faculty
#under-construction

1. Download Requirements using the following command:
pip install -r requirements.txt

2.Make Migrations using the following command:
python manage.py makemigrationss
python  manage.py migrate

3.Run the Application using followind command:
python manage.py runserver


About Application:

=>Register and login using the credentials
=>Faculty can create new assignments
=>Students can submit assignments using different page
=>Staff cannot submit student's assignments.
=>Student cannot create assignments.


Admin permissions can be created using following command:
python manage.py createsuperuser
"username"
"mailid"
"password"

Once the Admin created we can view Admin page using the following url:
127.0.0.1:8000/admin
