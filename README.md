# Registration-Form-with-Validation
This project implements a registration form using Flask and Flask-WTF with validation. The form collects a username, email, password, and password confirmation. The form is designed to ensure that all inputs meet specific validation criteria, and it displays appropriate error messages if the validation fails.

```
flask_project/
│  
│
├── templates/             # HTML template for the registration form
│   └── base.html      
│   └── footer.html      
│   └── header.html     
│   └── index.html      
│   └── register.html     
│
├── static/
│   └── styles.css         # Optional folder for static files (CSS, JS)
                        
│
└── app.py                 # Entry point to run the Flask application

```

## Features

Form Validation:
  
* Username: Must be at least 3 characters long.
* Email: Must be a valid email address.
* Password: Must be at least 8 characters long.
* Confirm Password: Must match the password.


CSRF Protection: 

* The form includes CSRF protection for security.    



## How to Run

Install the required dependencies:


```
pip install Flask Flask-WTF       
```

Run the application:
```
python app.py
```

Visit http://127.0.0.1:5000/ in your browser to access the registration form.