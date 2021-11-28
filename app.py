from flask import render_template, flash, redirect, url_for, session, g, request, Blueprint
from flask_login import login_required, login_user, logout_user, current_user

mod_auth = (__name__)

@mod_auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email = form.email.data, username = form.username.data, password = form.password.data)
		db.session.add(user)
		db.session.commit()
		flash("You have succesfully registered! You may now login")
		return redirect(url_for('mod_auth.login'))
	return render_template('mod_auth/register.html',form = form, title = "Register")

@mod_auth.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email = form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user)
			return redirect(url_for('mod_user.dashboard'))
		else:
			flash('Invalid email or password.')
	return render_template('app/login.html', form = form, title = 'Login')

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
	logout_user()
	flash('You have been succesfully logged out.')
	return redirect(url_for('app.login'))




    


if __name__=="__main":
    app.run(debub=True)

