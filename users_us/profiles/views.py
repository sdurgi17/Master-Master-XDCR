from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest 
from couchbase.bucket import Bucket


def update_profile(request):
	try:
		user_dict = request.GET
		users_bucket = Bucket('couchbase://localhost/users_us')
		if 'uid' in user_dict:
			users_bucket.upsert(request.GET.get('uid'), user_dict)
			return HttpResponse("successfully updated user profile")
		else:
			return HttpResponseBadRequest('uid not found')
	
	except Exception, e:
		return HttpResponseServerError("internal server error. Error : {e}".format(e=str(e)))
	