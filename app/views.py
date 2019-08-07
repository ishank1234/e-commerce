from django.shortcuts import render
from .models import Cart,Product,Customer,Collection,Order
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

def home(request):
    m=Collection.objects.all()
    return render(request,'home.html',{'m':m})

def prod(request,collection_id):
    b=Collection.objects.get(pk=collection_id)
    a=b.product_set.all()
    w=collection_id
    return render(request,'item.html',{'a':a})
lk=0
def yoo(request,product_id):
    a=Product.objects.get(pk=product_id)
    global lk
    lk=product_id
    return render(request,'yoo.html',{'a':a})


def ishank(request):

    logout(request)
    m=Collection.objects.all()
    return HttpResponseRedirect('/home',{'m':m})

def log(request):

    if request.method=="POST":
        username=request.POST['t1']
        password=request.POST['t2']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            m=Collection.objects.all()
            return HttpResponseRedirect('/home',{'m':m})
        else:
            er="Invalid Credentials"
            return HttpResponseRedirect('/signup',{'er':er})
    return render(request,'sign.html')

def signup(request):
    a1=request.POST.get('t1')
    email=request.POST.get('t3')
    a3=int(request.POST.get('t4'))
    a4=int(request.POST.get('t5'))
    a5=request.POST.get('t6')
    a6=request.POST.get('t7')
    a7=request.POST.get('t8')
    a8=request.POST.get('t9')
    username=request.POST.get('t10')
    password=request.POST.get('t11')
    user=User.objects.create_user(username=username,password=password,email=email)
    user.save()
    cart=Cart.objects.create(cust=user);
    cart.save()
    cust=Customer(name=a1,mob=a3,pin=a4,address=a5,city=a6,state=a7,country=a8,user=user)
    cust.save()
    user=authenticate(username=username,password=password)
    login(request,user)
    m=Collection.objects.all()
    return HttpResponseRedirect('/home',{'m':m})

def top(request,product_id):

    if request.method=="POST":
        username=request.POST['t1']
        password=request.POST['t2']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            a=Product.objects.get(pk=product_id)
            return HttpResponseRedirect('./yoo',{'a':a})
        else:
            er="Invalid Credentials"
            return HttpResponseRedirect('/signup',{'er':er})
    return render(request,'sign.html')

def nope(request,product_id):
    a=Product.objects.get(pk=product_id)
    global lk
    lk = product_id
    return render(request,'cash.html',{'a':a})
def wifi(request):
    a1 = request.POST.get('t1')
    a3 = int(request.POST.get('t4'))
    a4 = int(request.POST.get('t5'))
    a5 = request.POST.get('t6')
    a6 = request.POST.get('t7')
    a7 = request.POST.get('t8')
    a8 = request.POST.get('t9')
    q=request.user.customer.id
    Customer.objects.filter(pk=q).update(name=a1,mob=a3,pin=a4,address=a5,city=a6,state=a7,country=a8)
    cart=request.user.cart
    return HttpResponseRedirect('/cust',{'q':cart})

def modify(request):
    a1 = request.POST.get('t1')
    a3 = int(request.POST.get('t4'))
    a4 = int(request.POST.get('t5'))
    a5 = request.POST.get('t6')
    a6 = request.POST.get('t7')
    a7 = request.POST.get('t8')
    a8 = request.POST.get('t9')
    q=request.user.customer.id
    Customer.objects.filter(pk=q).update(name=a1,mob=a3,pin=a4,address=a5,city=a6,state=a7,country=a8)
    a=Product.objects.get(pk=lk)
    return render(request,'cash.html',{'a':a})


from django.http import JsonResponse

def search(request):
    a=request.POST.get('t1')
    if (a=='T-shirts' or a=='t-shirts' or a== 'T-SHIRTS' or a=='t-shirt' or a=='tshirts' or a=='t shirts' or a=='TSHIRTS'):
        w=Collection.objects.get(p_name='T-shirts')
    elif(a=='mobiles' or a=='MOBILES' or a=='Mobiles'):
        w=Collection.objects.get(p_name='Mobiles')
    elif (a == 'JEANS' or a == 'jeans' or a == 'Jeans' or a == "Denim Jeans" or a == 'denim jeans' or a == 'pants'):
        w = Collection.objects.get(p_name='Jeans')
    elif(a=='school bags' or a=='School Bags' or a=='School bags' or a=='bags' or a=='carry bags'):
        w=Collection.objects.get(p_name='Bags')
    elif(a=='earphones' or a=='Earphones' or a=='EARPHONS' or a=='ear-phones' or a=='ear phones' or a=='Headphones' or a=='HEADPHONES' or a=='headphones' or a=='headphone'):
        w=Collection.objects.get(p_name='Earphones')
    elif(a=='shoes' or a=='Shoes' or a=='SHOES' or a=='Sleepars' or a=='sleepar' or a=='SLEEPAR' or a=='Sleepar'):
        w=Collection.objects.get(p_name='footwear')
    elif(a=='Laptops' or a=='laptops' or a=='LAPTOPS' or a=='lappy' or a=='dell' or a=='DELL' or a=='laptop'):
        w=Collection.objects.get(p_name='Laptops')
    elif(a=='TV' or a=='tv' or a=='Television' or a=='television' or a=='electric cattle' or a=='Electric cattle' or a=='Cattle' or a=='cattle' or a=='Trimmer' or a=='trimmer' or a=='Philips trimmer'):
        w=Collection.objects.get(p_name='Electronics')
    elif(a=='furniture' or a=='Furniture' or a=='Sofa set' or a=='sofa set' or a=='sofa' or a=='chair' or a=='Chair'):
        w=Collection.objects.get(p_name='Furniture')
    
    a=w.product_set.all()
    return render(request,'item.html',{'a':a})
def usernamevarify(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists(),
    }
    return JsonResponse(data)
def cust(request):
    cart=request.user.cart

    return render(request,'coo.html',{'q':cart})
def sumi(request):
    a = Product.objects.get(pk=lk)
    cart=request.user.cart
    cart.products.add(a)
    cart.save()
    msg = "Product is added to your cart"
    return render(request,'yoo.html',{'a':a,'msg':msg})

def dele(request,product_id):
    cart=request.user.cart
    cart.products.remove(product_id)
    cart.save()
    return redirect('/cust',{'q':cart})

def deepak(request):
    cart=request.user.cart
    a=cart.products.all()
    print(a)
    b=request.user.customer.id
    c=Customer.objects.get(pk=b)
    ord=Order.objects.create(cust=c)

    for i in a:
        ord.products.add(i)
        ord.save()
        cart.products.remove(i)
        cart.save()

    ord.save()
    return redirect('/cust')

def thanks(request):
    a = Product.objects.get(pk=lk)
    b = a.collect.id
    c = request.user.customer.id
    w = Customer.objects.get(pk=c)
    ord = Order.objects.create(cust=w)
    ord.products.add(a)
    ord.save()
    c = Collection.objects.get(pk=b)

    return render(request,'thanks.html',{'a':a,'c':c})

def orders(request):
    a=Order.objects.all()
    return render(request,'order.html',{'a':a})
def soonn(request,order_id):
    Order.objects.get(pk=order_id).delete()
    a = Order.objects.all()
    return redirect('/orders',{'a':a})

# def sumi(request):
#     a=Product.objects.get(pk=lk)
#     b=request.user.customer.id
#     b1=Customer.objects.get(pk=b)
#     c=Cart(cust=b1,img=a.img.url,item_name=a.name,item_brand=a.brand,item_price=a.price)
#     c.save()
#     msg="Product is added to your cart"
#     return render(request,'yoo.html',{'a':a,'msg':msg})
