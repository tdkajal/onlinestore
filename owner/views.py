from django.shortcuts import render,redirect
from django.http import HttpResponse
from owner.forms import BookForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from owner.models import  Books
from django.urls import reverse_lazy
from customer.decorators import owner_permission_required
from django.utils.decorators import method_decorator
from django.contrib import messages
# from django.contrib import messages

@method_decorator(owner_permission_required,name='dispatch')
class AddBookView(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'addbook.html'
    success_url = reverse_lazy('listbook')
    # def get(self,request,*args,**kwargs):
    #     form=BookForm()
    #     context={'form':form}
    #     return render(request,'addbook.html',context)
    #
    #
    # def post(self,request,*args,**kwargs):
    #     form=BookForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #
    #         # print(form.cleaned_data)
    #         # book_name=form.cleaned_data.get('book_name')
    #         # author=form.cleaned_data.get('author_name')
    #         # price=form.cleaned_data.get('price')
    #         # copies=form.cleaned_data.get('copies')
    #         # qs=Books(
    #         #     book_name=book_name,
    #         #     author=author,
    #         #     price=price,
    #         #     copies=copies
    #         # )
    #         # qs.save()
    #         print('saved')
    #         return render(request,'addbook.html')
    #     else:
    #         context={'form':form}
    #         return render(request,'addbook.html',context)
@method_decorator(owner_permission_required,name='dispatch')
class BookListView(ListView):
    model = Books
    context_object_name = 'books'
    template_name = 'list.html'

    # def get(self,request):
    #     qs=Books.objects.all()
    #     context={'books':qs}
    #     return render(request,'list.html',context)
@method_decorator(owner_permission_required,name='dispatch')
class BookDetailView(DetailView):
    model = Books
    context_object_name = 'book'
    template_name ='bookdetail.html'
    pk_url_kwarg = 'id'
    # def get(self,request,**kwargs):
    #     print(kwargs)
    #     id=kwargs.get('id')
    #     qs=Books.objects.get(id=id)
    #     context={'book':qs}
    #     return render(request,'bookdetail.html',context)
@method_decorator(owner_permission_required,name='dispatch')
class BookEditView(UpdateView):
    model=Books
    template_name='bookedit.html'
    form_class = BookForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listbook')
    # def get(self,request,**kwargs):
    #     id=kwargs.get('id')
    #     qs=Books.objects.get(id=id)
    #     form =BookForm(instance=qs)
    #     context={'form':form}
    #     return render(request,'bookedit.html',context)
    # def post(self,request,**kwargs):
    #     id=kwargs.get('id')
    #     qs=Books.objects.get(id=id)
    #     form=BookForm(request.POST,files=request.FILES,instance=qs)
    #     if form.is_valid():
    #         # print('inside save')
    #         form.save()
    #         return render(request,'bookedit.html')
    #     else:
    #         # print('form error')
    #         context={'form':form}
    #         return render(request,'bookedit.html',context)
@method_decorator(owner_permission_required,name='dispatch')
class BookDeleteView(DeleteView):
    model = Books
    context_object_name = 'book'
    template_name ='book_delete.html'
    pk_url_kwarg = 'id'
    success_url=reverse_lazy('listbook')

    # def get(self,request,**kwargs):
    #     id=kwargs.get('id')
    #     qs=Books.objects.get(id=id)
    #     qs.delete()
    #     books=Books.objects.all()
    #     context={'book':qs,'books':books}
    #     return render(request,'list.html',context)
        # return redirect('listbook')

# Create your views here.
# from owner.models import books





# class based views,function based
# def owner_home(request):
#     return render(request,"index.html")
#
#
# def add_book(request):
#     if request.method=="GET":
#         print("inside get")
#         return render(request,"addbook.html")
#     else:
#         print(request.method)
#     return render(request,"addbook.html")
#
#
# def list_book(request):
#     context={"books":books}
#     return render(request,"list.html",context)
#
#
#
#     # owner/books/100
# def book_detail(request,id):
#     book=[ book for book in books if book["id"]==id]
#     context={"book":book}
#     return render(request,"bookdetail.html",context)
#


