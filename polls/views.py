# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the poll index")
	
def detail(request, poll_id):
	return HttpResponse("you're looking at poll %s" % (poll_id))

def results(request, poll_id):
	return HttpResponse("you're looking at the results of poll <strong>%s</strong>" % (poll_id))

def vote(request, poll_id):
	return HttpResponse("you're voting on poll %s" % (poll_id))