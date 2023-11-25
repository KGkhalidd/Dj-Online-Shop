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
        # store current applied coupon in cart
        self.coupon_id = self.session.get('coupon_id')


    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}
        #if the product does exist in cart and want to update its quantity
        #if u want a new quantity and skip previous quantity
        if override_quantity:
            self.cart[product_id]['quantity']= quantity
        #if u want to add a quantity to a previous one 
        else:
            self.cart[product_id]['quantity']+= quantity
        # save the cart to session
        self.save()

    # tells django that session is modified so save it
    def save(self):
            self.session.modified=True

    def remove(self,product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price']= Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        """
        remove cart from session
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()


