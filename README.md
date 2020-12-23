# E-Assignment

Online Assignment Application for Student and Faculty

## 1. Download Requirements using the following command:

```
pip install -r requirements.txt
```

## 2.Make Migrations using the following command:

```
python manage.py makemigrations


python manage.py migrate
```

## 3.Run the Application using the followind command:

```
python manage.py runserver
```

## Admin user can be created using the following command:

```
python manage.py createsuperuser
```

Once the Admin created we can view Admin page using the following url:
<b>127.0.0.1:8000/admin</b>

## About Application:

- <p>Register and login using the credentials.</p>
- <p>Faculty can create new assignments.</p>
- <p>Students can submit assignments using different page.</p>
- <p>Staff cannot submit student's assignments and Student cannot create assignments.</p>
- <p>You can Reset your password if you forget it</p>

<b>
"username"
<br></br>
"mailid"
<br></br>
"password"
</b>
<br></br>

## Screenshots

### Signup Page

<img src="Screenshots/signuppage.jpg">

### Login Page

<img src="Screenshots/loginpage.jpg">

### Student Home Page

<img src="Screenshots/studentpage1.jpg">

### Student ASsignment Submission Page

<img src="Screenshots/studentpage2.jpg">

### Faculty Home Page

<img src="Screenshots/facultypage1.jpg">

### Faculty Assignment Creation and Update Page

<img src="Screenshots/facultypage2.jpg">

### Faculty Assignment Delete Page

<img src="Screenshots/facultypage3.jpg">
