from flask import Flask, request, redirect, url_for, render_template,flash
from forms import RegistrationForm
app = Flask (__name__)
app.secret_key = '1234$' 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

@app.route('/register_check', methods=['GET','POST'])
def register_check():
    form = RegistrationForm()
    if request.method== 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        comfirm_password = form.comfirm_password.data
        return redirect(url_for('home',  username= username))
    return render_template('register.html', form=form)

@app.route('/home')
def home():
    flash("Welcome",'success')
    username = request.args.get('username')
    return render_template('home.html',username=username)

@app.errorhandler(Exception)
def page_not_found(e):
    if hasattr(e, 'code'):
        status_code = e.code
        error_message = {
            400: "Bad request.",
            401: "Authorization required.",
            403: "Access to this resource is forbidden.",
            404: "Ops! Page not found.",
            500: "An internal server error has occurred."
        }.get(status_code, "An unexpected error has occurred.")
    else:
        status_code = 500
        error_message = "An unexpected error has occurred."
    return render_template('error.html', error_message=error_message,status_code=e.code)

if __name__ == '__main__':
    app.run(debug = True)