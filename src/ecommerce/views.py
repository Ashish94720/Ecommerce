from django.http import HttpResponse 
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model # here login is pre defined mthod of django.contrib.auth 
# from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie

def home_page(request):
	# print(request.session.get("first_name","Unknown"))
	# request.session['first_name']
	context = {
	  "title" : "Hello world!",
	  "contact1" : "ashish kumar",
	}
	if request.user.is_authenticated:
		context["premium_content"] = "YEAHHHHH"

	return render(request,"home_page.html", context)
	# return HttpResponse("<h1><a href="">Hello ashish</a></h1>")

def about_page(request):
	content = {
	"title" : "About page",
	"content1" : " hai my name is about_page" 
	}
	return render(request,"home_page.html", content)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)  #instance of ContactForm
	content = {
	"title" : "Contact Page",
	"content1" : "hai my name is contact_page",
	"form" : contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	# if request.method == "POST":
	# 	print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request,"contact/view.html", content)

def login_page(request):  
	form = LoginForm(request.POST or None)
	context = {
	    "form" : form
	}
	print("User log in :",end=" ")
	# print(request.user.is_authenticated)
	print(request.user)
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password =  form.cleaned_data.get("password")
		user = authenticate(request,username=username,password=password)
		# print(request.user.is_authenticated)
		if user is not None:
			# print(request.user.is_authenticated)
			login(request, user)
			# context['form'] = LoginForm()
			return redirect("/")
		else:
			print("Error")
	
	return render(request,"auth/login.html",context)


User = get_user_model()
@ensure_csrf_cookie
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
	"form" : form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create_user(username,email,password)
		print(new_user)
	return render(request,"auth/register.html",context)





def home_page_old(request):
	html_="""
		<!doctype html>
	<html lang="en">
	  <head>
	    <!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

	    <title>Hello, world!</title>
	  </head>
	  <body>
	  <div class='text-center'>
	    <h1>Hello, world!</h1>
	    </div>

	    <!-- Optional JavaScript -->
	    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
	    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
	  </body>
	</html>
	"""
	return HttpResponse(html_)