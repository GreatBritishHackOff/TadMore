import requests
from flask import render_template, url_for, flash, redirect, request
from fakeshop import app
from fakeshop.models import Category, Item, Basket, Postcode
from fakeshop.forms import PostcodeHouseholdForm

def read_cookies():
  #Read variables from cookie
  flash(f'{requests.cookie}')

# home page
@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def home():
    form = PostcodeHouseholdForm()
    if form.validate_on_submit():
        #pc = Postcode.query.filter_by(postcode=form.postcode.data).first()
        pc = form.postcode.data
        hh = form.household.data
        if pc and hh in range(0,10):
            return redirect(url_for('basket', pc=[pc], hh=[hh]))
        else:
            flash(f'Postcode {form.postcode.data} does not exist in our database', 'danger')
    return render_template('home.html', title='Home', form=form )

# basket by poscode page
@app.route("/basket",  methods=['POST', 'GET'])
def basket():
    #querystring
    pc = request.args.get('pc')
    hh = request.args.get('hh')
    basketForPC = Postcode.query.filter_by(postcode=pc).first()
    print("Basket ID is = " + str(basketForPC.basket_id))
    #Try and get basket items
    shoppingbasket = Basket.query.filter_by(id=basketForPC.basket_id).first()
    print("First Item is = " + str(shoppingbasket.item_1))
    print("Second Item is = " + str(shoppingbasket.item_2))
    print("Third Item is = " + str(shoppingbasket.item_3))
    print("Fourth Item is = " + str(shoppingbasket.item_4))

    return render_template('basket.html', title='Basket', pc=pc, hh=hh)

