from flask import Flask, request, redirect, url_for, render_template
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
    username = request.args.get('username')
    return f"Hello{username}"

if __name__ == '__main__':
    app.run(debug = True)