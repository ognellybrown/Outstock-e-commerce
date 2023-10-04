
from market import app
#flash is a built in function used to display messsages in the client side 
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm
from market import db

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/shop")
def shop_page():
    return render_template("shop.html")

# def product_page():
#     return render_template('product-details.html')



@app.route("/register", methods=["GET","POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                              email_address = form.email_address.data,
                              password_harshed = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
     
        return redirect (url_for('shop_page'))
    
        #form.errors is a built in function to check if our validation is going to fail
    if form.errors != {}:                                       #if there are no errors from the validation
        for err_msg in form.errors.values():                    #itetrating over the err
            flash(f'There was an error with creating a user: {err_msg}')



    return render_template("register.html", form=form)


# "{{ url_for('home_page)}}"

# @app.route("/Login")
# def login_page():
#     return render_template("login.html")

# @app.route('/blog')
# def blog_page():
#     return render_template("blog.html")

