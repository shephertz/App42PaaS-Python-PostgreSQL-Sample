from django.shortcuts import render

# Create your views here.
from django.utils import simplejson
from django.template import RequestContext
from django.shortcuts import render_to_response
from sample.models import User

def index(request):
    
	return render_to_response("index.html",context_instance=RequestContext(request))
	
def save(request):

		user = User(name = request.POST['name'], description = request.POST['description'], email = request.POST['email'])
		user.save()
		results = User.objects.all()
		return render_to_response("home.html", {"results": results,},context_instance=RequestContext(request))	
	
