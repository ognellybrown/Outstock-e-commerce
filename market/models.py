from market import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable = False, unique=True)
    email_Address = db.Column(db.String(50), nullable = False, unique = True)
    password_harshed = db.Column(db.String(60), nullable = False) 
    items = db.relationship('Item', backref="owned_user", lazy = True)  #for the view Cart to know the goods the owner have in the view cart section   



class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer(), nullable = False)
    # image_file = db.Column(db.String(40))
    description = db.Column(db.String(1000), nullable = False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))  #the foriegn key is related to the other models primary key

    def __repr__(self):
        return f'Item {self.name}'