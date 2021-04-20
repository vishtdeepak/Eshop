from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

class Index(View):

	def post(self, request):
		product = request.POST.get('product')
		remove = request.POST.get('remove')
		cart = request.session.get('cart')
		if cart:
			quantity = cart.get(product)
			if quantity:
				if remove:
					if quantity<=1:
						cart.pop(product)
					else:
						cart[product] = quantity-1
				else:
					cart[product] = quantity+1
			else:				
				cart[product] = 1
		else :
			cart[product] = 1
		request.session['cart'] = cart
		print(request.session['cart'])
		return redirect('homepage')


	
	def get(self, request):
		cart = request.session.get('cart')
		if not cart:
			request.session['cart'] =  {}
		products = None
		categories = Category.get_all_categories()
		categoryID = request.GET.get('category')
		if categoryID:
			products = Product.get_all_products_by_categoryid(categoryID)
		else:
			products = Product.get_all_products()
		data = {}
		data['products'] = products
		data['categories'] = categories
		return render(request, 'index.html', data)


def listing(request, listing_id):
	listing = get_object_or_404(Product, pk=listing_id)
	context = {
		'listing': listing
	}
	return render(request, 'listing.html', context)




def search(request):
	products = Product.objects.all()
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		print('Find>>>>>>>>>>>>>>>>>>', keywords)
		if keywords:
			products = products.filter(name__icontains=keywords)
			print('Find>>>>>>>>>>>>>>>>>>', products)
		else:
			return HttpResponse('Not found')
			
	return render(request, 'search.html', {'products': products})

	






# def login(request):
# 	if request.method == 'GET':
# 		return render(request, 'login.html')
# 	else:
# 		email = request.POST.get('email')
# 		password = request.POST.get('password')
# 		customer = Customer.get_customer_by_email(email)
# 		print(customer)
# 		error_message = None
# 		if customer:
# 			flag = check_password(password, customer.password)
# 			print(flag)
# 			if flag:
# 				return redirect('homepage')
# 			else:
# 				error_message = 'Email or Password invalid!!!!'
# 		else:
# 			error_message = 'Email or Password invalid!!!!'
# 		print(email, password)
# 		return render(request, 'login.html', {'error': error_message})


















