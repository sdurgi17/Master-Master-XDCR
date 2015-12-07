from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from couchbase.bucket import Bucket


def update_profile(request):
	try:
		user_dict = request.GET
		b = Bucket('couchbase://localhost/beer-sample')
		b.upsert(request.GET.get('uid'), user_dict)
		return HttpResponse("successfully updated user profile")
	
	except Exception, e:
		return HttpResponseServerError("internal server error. Error : {e}".format(e=str(e)))
	