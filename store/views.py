from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ProductForm
from django import forms



# Create your views here.
def home(request):
    #return HttpResponse("Hello world!")
    products = Product.objects.all( )
    return render(request, 'home.html',{'products': products})
    


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ("You Have Been Logged In!"))
			return redirect('home')
		else:
			messages.success(request, ("There was an error, please try again..."))
			return redirect('login')

	else:
		return render(request, 'login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, ("you have been logged out"))
    return redirect('home')
    
    
def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("You Have Registered Successfully!! Welcome!"))
			return redirect('home')
		else:
			messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})

##############################################3
def dashboard(request):
    products = Product.objects.all( )
    return render(request, 'dashboard.html', {'products': products})

def productdelete(request,product_id):
    products = Product.objects.get(pk=product_id)
    products.delete()
    return redirect('dashboard')

def addnewproduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = { 'form' : form}
    return render(request, 'addnewproduct.html', context)


def productedit(request, product_id):
    if request.method == "POST":
        pro_id = Product.objects.get(pk=product_id)
        productform = ProductForm(request.POST, instance=pro_id)
        if productform.is_valid():
            productform.save()
            return redirect('dashboard')
    else:
        pro_id = Product.objects.get(pk=product_id)
        productform = ProductForm(instance=pro_id) 
        
    context ={
        'pro_id' : productform,
    }
    return render(request, 'productedit.html', context)


#---------------------




# def add_to_cart(request, product_id):
#     if request.method == 'POST':
#         product = Product.objects.get(pk=product_id)
#         quantity = int(request.POST.get('quantity', 1))

#         # Check if the user is authenticated or use session-based cart for guests
#         if request.user.is_authenticated:
#             cart_item, created = CartItem.objects.get_or_create(
#                 user=request.user,
#                 product=product,
#             )
#             cart_item.quantity += quantity
#             cart_item.save()
#         else:
#             # For guests, store the cart in the session
#             cart = request.session.get('cart', {})
#             cart_item = cart.get(product_id, {'quantity': 0})
#             cart_item['quantity'] += quantity
#             cart[product_id] = cart_item
#             request.session['cart'] = cart

#         return redirect('product_list')  # Redirect to a product list view
#     else:
#         # Handle GET requests or render a product detail page
#         # Render a form to input the quantity and submit the POST request
#         product = Product.objects.get(pk=product_id)
#         #return render(request, 'product_detail.html', {'product': product}) 
#         return redirect('home')   

