from django.shortcuts import render,redirect
from basic_app.forms import ProductForm
from basic_app.models import Product
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.


def Index(request):
    
    return "Hello Index Page!!"



def validate_username(request):

    if request.is_ajax():
       name = request.POST['username']
       #name=request.GET.get('username', None)
      

       data = {}
       data['result'] = 'you made a request'
       data['result1'] = 'Nayeem'

       data['name'] =name
            

       return HttpResponse(json.dumps(data), content_type="application/json")


def show(request):
    products=Product.objects.all()

    return render(request,'show.html',{'products':products})

def insert(request):

    form=ProductForm(request.POST,request.FILES or None)
    if form.is_valid():
           form.save()

           return redirect('show')

    return render(request,'show.html')



def view(request,pk):

    product=Product.objects.get(pk=pk)
    
    return render(request,'view.html',{'product':product})


def create_product(request):

    form=ProductForm()

   
 
    return render(request,'product_form.html',{'form':form})

def update(request,pk):

    product=Product.objects.get(pk=pk)
    form=ProductForm(instance=product)
    return render(request,'product_view.html',{'product':product})

def edit(request,pk):
    product=Product.objects.get(pk=pk)
    form=ProductForm(request.POST,request.FILES or None,instance=product)
    if form.is_valid():
        form.save()
        return redirect('show')
    return render(request,'product_form.html',{'form':form})

def delete(request,pk):

    product=Product.objects.get(pk=pk)

    product.delete()

    return redirect('show')



    