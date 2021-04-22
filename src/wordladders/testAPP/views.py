from django.shortcuts import render, get_object_or_404, redirect

from.forms import ProductForm
from .models import Product

def product_form_view(request):
	init_data = {
	'title': "Default title",
	}
	form = ProductForm(request.POST or None,initial = init_data)
	if form.is_valid():
		form.save()

	context = {
		'form':form
	}
	return  render(request, "product/createForm.html",context)

# Create your views here.
def product_detail_view(request, my_id):
	# obj = Product.objects.get(id=my_id)
	obj = get_object_or_404(Product,id=my_id)
	context = {
	'object': obj,
	}
	return render(request,"product/detail.html",context)

def product_delete_view(request,id):
	obj  = get_object_or_404(Product,id=id)
	print("DAFUCK")
	if request.method == "POST":
		print(obj,"DETELINGNNGGG")
		obj.delete()
		return redirect('../../')
	context =  {
		"object":obj
	}
	return render(request,"product/product_delete.html",context)

def prod_list_view(request):
	queryset = Product.objects.all()
	context = {
	"object_list": queryset
	}
	return render(request,"product/product_list.html",context)