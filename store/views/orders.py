from django.views import View
from django.shortcuts import redirect, render
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator

class OrderView(View):
	
	# @method_decorator(auth_middleware)
	def get(self, request):
		customer = request.session.get('customer')
		orders = Order.get_orders_by_customer(customer)
		return render(request, 'orders.html', {'orders': orders})


			


		