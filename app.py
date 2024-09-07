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
        return redirect(url_for('home'))
    return render_template('register.html', form=form)



@app.route('/home')
def home():
    return "HELLO"

if __name__ == '__main__':
    app.run(debug = True)