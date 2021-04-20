from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class Signup(View):
	def get(self, request):
		return render(request, 'signup.html')

	def post(self, request):
		postData = request.POST
		first_name = postData.get('firstname')
		last_name = postData.get('lastname')
		phone = postData.get('phone')
		email = postData.get('email')
		password = postData.get('password')
		# print(first_name, last_name, phone, email, password)

		value = {
			'first_name': first_name,
			'last_name': last_name,
			'phone': phone,
			'email': email
		}

		error_message = None
		customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
		error_message = self.validateCustomer(customer)
		#saving 
		if not error_message:
			print(first_name, last_name, phone, email, password)
			customer.password = make_password(customer.password)
			customer.register()
			return redirect('homepage')
		else:
			data = {
				'error': error_message,
				'values': value
			}
			return render(request, 'signup.html', data)

	def validateCustomer(self, customer):
		error_message = None
		if(not customer.first_name):
			error_message = 'First Name Required !!!!'
		elif len(customer.first_name) < 4:
			error_message = 'Atleast 4 digits of Name Required !!!'
		elif customer.isExists():
			error_message = 'Email @ already registered!!!!!'
		return error_message
