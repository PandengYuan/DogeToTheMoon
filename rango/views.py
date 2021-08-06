from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from rango.models import Category, Product, Cart
from rango.forms import CategoryForm, UserForm, UserProfileForm, ProductForm, CartForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime


#index view 
def index(request):
    category_list = Category.objects.order_by('-sales')[:5]
    product_list = Product.objects.order_by('-sales')[:5]

    #context 
    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['products'] = product_list

    visitor_cookie_handler(request)
    # context_dict['visits'] = request.session['visits']
    response = render(request, 'rango/index.html', context=context_dict)
    return response

#the view which show the choosen category
def show_category(request, category_name_slug):

    context_dict = {}
    #context
    category_list = Category.objects.all()

    try:#slug problem
        category = Category.objects.get(slug=category_name_slug)

        products = Product.objects.filter(category=category)

        context_dict['products'] = products
        context_dict['category'] = category
        context_dict['categories'] = category_list
    except Category.DoesNotExist:
        #exception process
        context_dict['category'] = None
        context_dict['products'] = None
        context_dict['categories'] = None

    return render(request, 'rango/category.html', context=context_dict)


#the view which show the detail of a product 
def show_product(request, product_name_slug):

    context_dict = {}

    product_list = Product.objects.all()

    try:
        product = Product.objects.get(slug=product_name_slug)

        # products = Product.objects.filter(category=category)

        # context_dict['products'] = products
        context_dict['product'] = product
        # context_dict['products'] = category_list
    except Category.DoesNotExist:

        context_dict['product'] = None
        # context_dict['produucts'] = None
        # context_dict['categories'] = None

    return render(request, 'rango/product.html', context=context_dict)


#add category view 
@login_required
def add_category(request):

    form = CategoryForm()
    # A HTTP POST
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():

            form.save(commit=True)
            #redirect to homepage
            return redirect(reverse('rango:index'))
        else:

            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})


#the view used to upload product
@login_required
def upload_product(request):
   
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():

            product = form.save(commit=True)
            product.save()

            return redirect(reverse('rango:seller_my_account'))
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'rango/upload_product.html', context=context_dict)

#register view 
def register(request):
    registered = False
    #http post 
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            # deal with picture attribute 
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'rango/register.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

# login in page 
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #determine whether the user is allowed
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/login.html')

#restricted view
@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')

# log out  view 
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))

#help method about cookie
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

#the view used to deal with visitor cookie
def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    #define cookie +1 time 
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    
    request.session['visits'] = visits

#the my account view of 'buyer' user
@login_required
def buyer_my_account(request):
    return render(request, 'rango/buyer_my_account.html')

# the my account view of 'seller' user
@login_required
def seller_my_account(request):
    return render(request, 'rango/seller_my_account.html')

# the cart view 
@login_required
def cart(request):

    context_dict = {}
    # dealwith the parameter of context
    products = Product.objects.all()
    carts = Cart.objects.all()
    username = request.user.username
    product_list = []
    for item in carts:
        if item.buyer_name == username:
            for p in products:
                if item.product_name == p.name:
                    product_list.append(p)
    #context
    context_dict['products'] = product_list
    return render(request, 'rango/cart.html',context=context_dict)



# the payment view belongs to 'buyer' user 
@login_required
def payment(request):
    context_dict = {'user': request.user}
    return render(request, 'rango/payment.html', context=context_dict)

# the remove product page whic belonngs to 'seller' user
@login_required
def remove_product (request):
    context_dict = {}
    context_dict['products'] = Product.objects.all()
    return render(request, 'rango/remove_product.html',context=context_dict)






def product_search(request):
   
    if request.method == 'POST':
        content = request.POST.get('content').lower()
        products = Product.objects.all()
        categories = Category.objects.all()
        product_list = []
        for p in products:
            if content == p.name.lower():
                product_list.append(p)
            if content == p.category.name.lower():
                product_list.append(p)

        context_dict = {'products':product_list}
        return render(request, 'rango/product_search.html', context=context_dict)














