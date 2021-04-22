from django.shortcuts import render


from django.http import HttpResponse 

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args) #requests are passed through *args. You can also
				# excplicitly take request as argument
	print(request)
	print(request.user) 
	return HttpResponse("<h1>Hello World</h1>")

def contact_view(request, *args, **kwargs):

	my_context = {
		"my_text": "This is about me",
		"my_number": 123452,
		"my_list": [1,2,4,2,3,4,5,1],
		"my_html":"<h1> hello world! </h1>"
	}

	# isEven = 

	return render(request,"home.html",my_context)



