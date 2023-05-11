from django.shortcuts import render
from .models import *

from django.http import JsonResponse
import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.http import JsonResponse
from store.models import Product
# Create your views here.

def my_api_view(request):
    data = Product.objects.all().values()
    return JsonResponse(list(data), safe=False)



def submit_output(request):
    if request.method == 'POST':
        output = request.POST.get("tv")
        print(output)
        output = int(output)  # convert output to integer
        if output <= 10:
            tag = 1
        elif output > 10 and output <= 20:
            tag = 2
        elif output > 20 and output <= 30:
            tag = 3
        elif output > 30 and output <= 40:
            tag = 4
        else:
            tag = 5
            # handle the case when output is outside the range
            # pass
        # get the products with the corresponding tag from the database
        products = Product.objects.filter(tag=(tag or 0))
        # return a JSON response with the products
        product_list = []
        for product in products:
            product_list.append({'name': product.name, 'price': product.price})
        return JsonResponse({'products': product_list})
        # return response ()->json (['message' => 'task was successful']);
    else:
        # handle the case when the page is loaded for the first time
        return render(request, 'store.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # user = authenticate(request, username=username, password=password)
        user = authenticate(username=username, password=password)
        if user is not None:
            # login(request,user)
            login(request, user)
            return redirect('store')
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'store/login.html')


def log_out(request):
    logout(request)
    return render(request,'store/store.html')

def sign_up(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('store')
	else:
		form = UserCreationForm()
	return render(request, 'store/signup.html', {'form': form})



def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']
    
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('Item ws added', safe=False)

# class CustomLoginView(login_View):
#     def get_success_url(self):
#         return '/'


# def login(request):
#     # user = authenticate(username=username, password=password)
#     # if request.user.is_authenticated():
#     #     return redirect('admin_page')

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             # correct username and password login the user
#             login(request, user= user)
#             return redirect('admin_page')

#         else:
#             messages.error(request, 'Error wrong username/password')

#     return render(request, 'store/login.html')


# def logout(request):
#     logout(request)
#     return render(request,'store/logout.html')


# def admin_page(request):
#     if not request.user.is_authenticated():
#         return redirect('store/login.html')

#     return render(request, 'store.html')