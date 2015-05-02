
# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

# create the application object
app = Flask(__name__)


# config
app.secret_key = "gollum gimli"

# login required decorator

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('YOU NEED TO LOGIN FIRST')
			return redirect(url_for('login'))
	return wrap

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
	return render_template("index.html") # renders a template
    #return 'this is the home page!' # returns a string

@app.route('/welcome')
def welcome():
    return render_template("welcome.html") # renders a template




@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'INVALID Creds..Please try again.'
		else:
			session['logged_in'] = True
			flash('YOU ARE LOGGED IN !!')
			return redirect(url_for('home'))

        return render_template('login.html',error=error)


@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('YOU ARE LOGGED OUT!!')
	return redirect(url_for('welcome'))
















#START THE SERVER WITH THE RUN METHOD

if __name__ == '__main__':
    app.run(debug=True)