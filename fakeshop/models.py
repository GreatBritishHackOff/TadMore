from fakeshop import db, admin
from flask_admin.contrib.sqla import ModelView

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    items = db.relationship('Item', backref='category', lazy=True) # reference to Item class

    def __repr__(self):
        return f"Category('{self.name}')"

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(20), unique=False, nullable=True)
    price_old = db.Column(db.Float, nullable=False)
    price_new = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    cat_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False) # reference to table column

    def __repr__(self):
        return f"Item('{self.name}', '{self.category}', '{self.price_old}', '{self.price_new}','{self.image}')"


class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_1 = db.Column(db.Integer, nullable=True)
    item_2 = db.Column(db.Integer, nullable=True)
    item_3 = db.Column(db.Integer, nullable=True)
    item_4 = db.Column(db.Integer, nullable=True)
    postcodes = db.relationship('Postcode', backref='basket', lazy=True)

    def __repr__(self):
        return f"Basket('{self.item_1}, {self.item_2}, {self.item_3}, {self.item_4}')"


class Postcode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postcode = db.Column(db.String(10), unique=True, nullable=False)
    basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'), nullable=True)

    def __repr__(self):
        return f"Postcode('{self.postcode}, {self.basket_id}')"


# admin
admin.add_view(ModelView(Item, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Basket, db.session))
admin.add_view(ModelView(Postcode, db.session))
