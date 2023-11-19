from django.shortcuts import render, redirect
from app.models import ProductModel, CategoryModel, CommentModel, OrderModel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
@permission_required('app.view_productmodel', login_url='login')
def to_home(request):
    return redirect('/app/list/')

def list(request):
    products = ProductModel.objects.all().order_by('-created_at')
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html',{'products':page_obj})

def search_by(request):
    search = request.GET.get('search')

    if search:
        products = ProductModel.objects.filter(
            Q(name__icontains=search)
        )
        return render(request, 'list.html', {'products': products})
    else:
        products = ProductModel.objects.all().order_by('-created_at')
        return render(request, 'list.html', {'products': products})

def detail(request, product_id): 
    products = ProductModel.objects.get(id=product_id)  
    categorys = CategoryModel.objects.all() 
    cmts = CommentModel.objects.filter(product_id=product_id)
    return render(request, 'detail.html',{'products':products, 'categorys':categorys, 'cmts':cmts})

def orderpage(request, product_id):
    products = ProductModel.objects.get(id=product_id)
    return render(request, 'order.html', {'products':products})

def order(request, product_id): 
    products = ProductModel.objects.get(id=product_id)
    orders = OrderModel.objects.create(
        quantity = request.POST.get('quantity'),
        address = request.POST.get('address'),
        city = request.POST.get('city'),
        state = request.POST.get('state'),
        phone = request.POST.get('phone'),
        user_id = request.user.id,
        product_id = products.id,
        created_at = datetime.now()
    )
    orders.save()
    messages.success(request, "The order has been sent successfully.")
    return redirect('/app/list/')

def order_list(request, user_id):
    orders = OrderModel.objects.filter(user_id=user_id)
    paginator = Paginator(orders, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'orderlist.html',{'orders':page_obj})

def order_detail(request, order_id): 
    orders = OrderModel.objects.get(id=order_id) 
    products = ProductModel.objects.all()  
    categorys = CategoryModel.objects.all() 
    users = User.objects.all() 
    return render(request, 'orderdetail.html',{'products':products, 'categorys':categorys, 'orders':orders, 'users':users})

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        user = request.POST.get('username')
        paswd = request.POST.get('password')
        user = authenticate(username = user, password = paswd)

        if user is not None:
            login(request, user)
            messages.success(request, "login success!")
            return redirect('/app/list/')
        else:
            messages.error(request,"Username or Password is incorrect!")
            return redirect('/login/')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('/app/list/')
    else:
        return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')

def cmt_create(request, product_id):
    comment = CommentModel.objects.create(
        content = request.POST.get('content'),
        user_id = request.user.id,
        product_id = product_id
    )

    comment.save()
    messages.success(request,"Your Comment has been updated successfully!")
    return redirect(f'/app/detail/{product_id}/#comment')

def cmt_delete(request, product_id, cmt_id):
    comment = CommentModel.objects.get(id=cmt_id)
    comment.delete()
    messages.error(request,"Your Comment Is Deleted!")
    return redirect(f'/app/detail/{product_id}/#comment')

def cmt_update(request, product_id, cmt_id):
    if request.method == "GET":
        comment = CommentModel.objects.get(id=cmt_id)
        return render(request, 'cmtUpdate.html',{'cmt':comment})

    if request.method == "POST":
        comment = CommentModel.objects.get(id=cmt_id)
        comment.content = request.POST.get('content')
        comment.save()
        messages.info(request,"Your Comment Is Updated Successfully!")
        return redirect(f'/app/detail/{product_id}/#comment')

def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)
