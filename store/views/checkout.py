from django.views import View
from django.shortcuts import redirect, render
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order

class CheckOut(View):
	def post(self, request):
		address = request.POST.get('address')
		phone = request.POST.get('phone')
		customer = request.session.get('customer')
		cart = request.session.get('cart')
		products = Product.get_products_by_id(list(cart.keys()))
		# print(address, phone, customer, cart ,products)
		

		for product in products:
			order = Order( customer = Customer(id=customer), product=product,
							quantity = cart.get(str(product.id)), price = product.price,
							address = address, phone = phone)
			order.save()

		request.session['cart'] = {}
		
		return redirect('cart')

			


		