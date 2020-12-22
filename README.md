# E-Assignment

Online Assignment Application for Student and Faculty
#under-construction

1. Download Requirements using the following command:
'''
<p> pip install -r requirements.txt </p>
 '''
 2.Make Migrations using the following command:
 '''
 <p>python manage.py makemigrations </p>
 '''
 '''
 <p>python manage.py migrate </p>
 '''
 3.Run the Application using followind command:
 '''
  <p> python manage.py runserver </p>
 '''

# About Application:

<p>Register and login using the credentials.</p>
<p>Faculty can create new assignments.</p>
<p>Students can submit assignments using different page.</p>
<p>Staff cannot submit student's assignments.</p>
<p>Student cannot create assignments.</p>

Admin permissions can be created using following command:
'''

<p>  python manage.py createsuperuser </p>
'''
"username"
"mailid"
"password"

Once the Admin created we can view Admin page using the following url:
127.0.0.1:8000/admin
