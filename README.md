# E-Assignment

Online Assignment Application for Student and Faculty

# 1. Download Requirements using the following command:

```
pip install -r requirements.txt
```

# 2.Make Migrations using the following command:

```
python manage.py makemigrations


python manage.py migrate
```

# 3.Run the Application using followind command:

```
python manage.py runserver
```

# About Application:

<p>Register and login using the credentials.</p>
<p>Faculty can create new assignments.</p>
<p>Students can submit assignments using different page.</p>
<p>Staff cannot submit student's assignments.</p>
<p>Student cannot create assignments.</p>

Admin permissions can be created using following command:

```
python manage.py createsuperuser
```

<b>
"username"
<br></br>
"mailid"
<br></br>
"password"
</b>
<br></br>
Once the Admin created we can view Admin page using the following url:
127.0.0.1:8000/admin
