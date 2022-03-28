from django.shortcuts import render, redirect
from django.http import HttpResponse
from owner.models import Books
from django.views.generic import View,ListView
from customer.forms import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from customer.decorators import sign_in_required
from django.utils.decorators import method_decorator
from customer.models import Carts
from django.db.models import Sum

# Create your views here.
@method_decorator(sign_in_required,name='dispatch')
class ListallView(View):
    def get(self, req,*args,**kwargs):
        # if request.user.is_authenticated:
            print('here')
            qs = Books.objects.all()
            context = {'books': qs}
            return render(req, 'listallbooks.html', context)
class SignUpView(View):
    def get(self, req):
        form = UserRegistrationForm()
        context = {'form': form}
        return render(req, 'signup.html', context)

    def post(self, req):
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            print('user created')
            return render(req, 'signup.html')
        else:
            context = {'form': form}
            return render(req, 'signup.html', context)


class SignInView(View):
    def get(self, req):
        form = LoginForm()
        context = {'form': form}
        return render(req, 'signin.html', context)

    def post(self, req):
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(req, username=username, password=password)
            if user:
                login(req, user)
                if req.user.is_superuser:
                    return redirect('listbook')
                else:
                    return redirect('allbooks')
            else:
                context = {'form': form}
                return render(req, 'signin.html', context)
def Sign_Out(request):
    logout(request)
    return redirect('signin')

class AddToCartView(View):


    def get(self,req,*args,**kwargs):
        id=kwargs['id']
        book=Books.objects.get(id=id)
        user=req.user
        cart=Carts(user=user,item=book)
        cart.save()
        print('item has been added to cart')
        return redirect('allbooks')
class CartItems(ListView):
    model=Carts
    template_name='cart_items.html'
    context_object_name='items'
    def get(self,request,*args,**kwargs):
        qs= self.model.objects.filter(user=self.request.user).exclude(status='cancelled')
        total=qs.aggregate(Sum('item__price'))
        print(total)
        sum=total['item__price__sum']
        context={'items':qs,'sum':sum}
        return  render(request,self.template_name,context)

class RemoveCartItem(View):
    def get(self,req,*args,**kwargs):
        id=kwargs['id']
        cart=Carts.objects.get(id=id)
        cart.status='cancelled'
        cart.save()
        return redirect('allbooks')