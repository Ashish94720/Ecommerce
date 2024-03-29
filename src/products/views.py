from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404

from carts.models import Cart

from .models import Product

# Create your views here.
# class ProductListView and def product_list_view are same listView representation.Output of both is same

class ProductFeaturedListView(ListView):
	template_name = "products/list.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
	# queryset = Product.objects.all()
	queryset = Product.objects.all().featured()
	template_name = "products/featured-detail.html"

	# def get_queryset(self, *args, **kwargs):
	# 	request = self.request
	# 	return Product.objects.featured()



class ProductListView(ListView):
	# queryset = Product.objects.all()
	template_name = "products/list.html"

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	print(context)				
	# 	return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all()

	# def get_queryset(self, *args, **kwargs):
	# 	request = self.request
	# 	pk = self.kwargs.get('pk')
	# 	instance = Product.objects.filter(pk=pk)
	# 	if instance is None:
	# 		raise Http404("item not found")
	# 	return Product.objects.filter(pk=pk)
		

def product_list_view(request):
	query = Product.objects.all()
	context = {
	'object_list' : query
	}
	print(context)
	return render(request,"products/list.html",context)


class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self,*args,**kwargs):
		context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context


	def get_object(self, *args, ** kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		# instance = get_object_or_404(Product,slug=slug,active=True)
		try:
			instance = Product.objects.get(slug=slug, active=True)
		except Product.DoesNotExist:
			raise Http404("Item not found...")
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug=slug,active=True)
			instance = qs.first()
		except:
			raise Http404("Uhhmmm")
		return instance

			


class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		# context['abc'] = 123    # we add data in context dictonary data type
		print(context)				
		return context

	def get_object(self, *args, ** kwargs):
		request = self.request
		# print("request is : ",request)
		# print("kwargs : ",kwargs)
		pk = self.kwargs.get('pk')
		# print("primary : ",pk)
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Product doesn't Exist")
		return instance

	# def get_queryset(self, *args, **kwargs):
	# 	request = self.request
	# 	pk = self.kwargs.get('pk')
	# 	return Product.objects.filter(pk=pk)

	# def get_queryset(self):
	# 	return Product.objects.all()



		

def product_detail_view(request, pk=None, *args, **kwargs):
	##### all doing same thing
	# instance = Product.objects.get(pk=pk, featured =True)
	# print(instance)
	# instance = get_object_or_404(Product,pk=pk,featured = True)
	########################
	# try:
	# 	instance = Product.objects.get(id=pk)
	# except Product.DoesNotExist:
	# 	print('product not found')
	# 	raise Http404("Product doesn't Exit")
	# except:
	# 	print("hubbb")
	############################

	instance = Product.objects.get_by_id(pk)
	# print(instance)
	if instance is None:
		raise Http404("Product doesn't Exist")
	############################
	# qs = Product.objects.filter(id=pk)
	# # print(qs)
	# if qs.exists() and qs.count() == 1:
	# 	instance = qs.first()
	# else:
	# 	raise Http404("Product doesn't Exist")

	context = {
	'object' : instance
	}
	return render(request,"products/detail.html",context)
