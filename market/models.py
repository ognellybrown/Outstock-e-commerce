from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable = False, unique=True)
    email_address = db.Column(db.String(50), nullable = False, unique = True)
    password_harshed = db.Column(db.String(60), nullable = False) 
    items = db.relationship('Item', backref="owned_user", lazy = True)  #for the view Cart to know the goods the owner have in the view cart section   

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_harshed = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)  #excute this function and return the check_password_correction value back.
            

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer(), nullable = False)
    # image_file = db.Column(db.String(40))
    description = db.Column(db.String(1000), nullable = False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))  #the foriegn key is related to the other models primary key

    def __repr__(self):
        return f'Item {self.name}'