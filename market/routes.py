
from market import app
#flash is a built in function used to display messsages in the client side 
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError

@app.route("/home")
def home_page():
    return render_template("index.html")

@app.route("/shop")
@login_required                     #this linne is responsible to take our users automatically to the login page 
def shop_page():
    return render_template("shop.html")

# def product_page():
#     return render_template('product-details.html')





@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user_to_create = User(
                username=form.username.data,
                email_address=form.email_address.data,
                password=form.password1.data
            )
            db.session.add(user_to_create)
            db.session.commit()
            login_user(user_to_create)
            flash(f'Account created, you are now logged in as {user_to_create.username}', category='success')
            return redirect(url_for('shop_page'))
        except IntegrityError as e:
            db.session.rollback()  # Rollback the transaction
            if "UNIQUE constraint failed: user.email_address" in str(e):
                flash('Email address already exists. Please choose a different one.', 'danger')
            if "UNIQUE constraint failed: user.username" in str(e):
                flash('Username already exists. Please choose a different one.', 'danger')

    return render_template("register.html", form=form)



@app.route("/login", methods = ['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'You have been logged in as: {attempted_user.username}', category= 'success')
            return redirect(url_for('shop_page'))

        else:
            flash("Username and password are not matched, please try again", category='danger')

    return render_template("login.html", form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash (f'You have been logged out!', category='info')
    return render_template(url_for('login_page'))


@app.route('/account')
def account_page():
    return render_template('account.html')



@app.route('/product-details')
def product_page():
    return render_template('product-details.html')


