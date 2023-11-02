from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart:
    def __init__(self, request):
        #hold the session of the user or visitor
        self.session = request.session
        #try to get the cart from the session
        cart = self.session.get(settings.CART_SESSION_ID)
        #if there is no cart
        if not cart:
            #create one 'by setting an empty dict' in the session
            cart = self.session[settings.CART_SESSION_ID]= {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}
        #if the product does exist in cart and want to update its quantity
        #if u want a new quantity and skip previous quantity
        if override_quantity:
            self.cart[product_id][quantity]= quantity
        #if u want to add a quantity to a previous one 
        else:
            self.cart[product_id][quantity]+= quantity
        # save the cart to session
        self.save()

    # tells django that session is modified so save it
    def save(self):
            self.session.modified=True
