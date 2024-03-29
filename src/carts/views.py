from django.shortcuts import render, redirect

# Create your views here
from products.models import Product
from .models import Cart

# def cart_create(user=None):
# 	cart_obj = Cart.objects.create(user=None)
# 	print("New Cart Created")
# 	return cart_obj


def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	products = cart_obj.products.all()
	total = 0
	for x in products:
		total += x.price
	print(total)
	cart_obj.total = total
	cart_obj.save()
	# print(request.session) # session object store in database details
	# # del request.session["cart_id"]
	# # print(dir(request.session))
	# #key=request.session.session_key
	# # print(key)
	# #request.session['first_name']='ashish'
	# #request.session['card_id'] = "12"
	# cart_id = request.session.get("card_id", None)
	# qs = Cart.objects.filter(id=cart_id)
	# if qs.count() == 1:
	# 	print("cart ID exits")
	# 	cart_obj = qs.first()
	# 	if request.user.authenticated() and cart_obj.user is None:
	# 		cart_obj.user=request.user
	# 		cart_obj.save()
	# else:
	# 	cart_obj = Cart.objects.new(user=request.user)
	# 	request.session['cart_id'] = cart_obj.id
	return render(request,'carts/home.html',{})

def cart_update(request):
	product_id = 1
	product_obj = Product.objects.get(id=product_id)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	if product_obj in cart_obj.products.all():
		cart_obj.products.remove(product_obj)

	else:
	    cart_obj.products.add(product_obj) #cart_obj.products.add(product_id)
	# return redirect(product_obj.get_absolute_url())
	return redirect("cart:home")

