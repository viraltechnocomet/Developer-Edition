from http.client import HTTPResponse
from django.views.generic import (
    TemplateView,
    DetailView,
    View,
    ListView,
    DetailView,
)

from django.http import (
    JsonResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
    HttpResponse
)
from django.shortcuts import (
    render,redirect
)

from core.forms import CreateUserCustomForm, AddManagerForm
from accounts.models import CustomUser
from django.conf import settings
from core.forms import AddManagerForm
import os
import cv2
import json
import base64
from django.core import files
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage


TEMP_PROFILE_IMAGE_NAME = "temp_profile_image.png"

class DashboardView(View):
    template_name = './core/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {"demo":"value"}
        return render(request, self.template_name,context=context)

    def post(self, request, *args, **kwargs):
        ...
        
def AddManager(request):
    context={}
    context['form'] = AddManagerForm
    return render(request,'core/add-manager.html',context)

# def AddManager(request, args, *kwargs):
# 	if not request.user.is_authenticated:
# 		return redirect("login")
# 	user_id = kwargs.get("user_id")
# 	account = CustomUser.objects.get(pk=user_id)
# 	if account.pk != request.user.pk:
# 		return HTTPResponse("You cannot edit someone elses profile.")
# 	context = {}
# 	if request.POST:
# 		form = AddManagerForm(request.POST, request.FILES, instance=request.user)
# 		if form.is_valid():
# 			form.save()
# 			return redirect("core:view", user_id=account.pk)
# 		else:
# 			form = AddManagerForm(request.POST, instance=request.user,
# 				initial={
# 					"id": account.pk,
# 					"email": account.email, 
# 					"username": account.username,
# 					"profile_image": account.profile_image,
# 				}
# 			)
# 			context['form'] = form
# 	else:
# 		form = AddManagerForm(
# 			initial={
# 					"id": account.pk,
# 					"email": account.email, 
# 					"username": account.username,
# 					"profile_image": account.profile_image,
# 				}
# 			)
# 		context['form'] = form
# 	context['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
# 	return render(request, "core/add-manager.html", context)

def save_temp_profile_image_from_base64String(imageString, user):
	INCORRECT_PADDING_EXCEPTION = "Incorrect padding"
	try:
		if not os.path.exists(settings.TEMP):
			os.mkdir(settings.TEMP)
		if not os.path.exists(os.path.join(settings.TEMP, str(user.pk))):
			os.mkdir(os.path.join(settings.TEMP, str(user.pk)))
		url = os.path.join(settings.TEMP,str(user.pk),TEMP_PROFILE_IMAGE_NAME)
		print(url)
		storage = FileSystemStorage(location=url)
		
		image = base64.b64decode(imageString)

		with storage.open('', 'wb+') as destination:
			
			destination.write(image)
			destination.close()
		return url
	except Exception as e:
		print("exception: " + str(e))
		# workaround for an issue I found
		if str(e) == INCORRECT_PADDING_EXCEPTION:
			imageString += "=" * ((4 - len(imageString) % 4) % 4)
			return save_temp_profile_image_from_base64String(imageString, user)
	return None

def crop_image(request, *args, **kwargs):
	payload = {}
	user = request.user
	
	if request.POST and user.is_authenticated:
		
		try:
			imageString = request.POST.get("image")
			url = save_temp_profile_image_from_base64String(imageString, user)
			
			img = cv2.imread(url)

		
			cropX = int(float(str(request.POST.get("cropX"))))
			cropY = int(float(str(request.POST.get("cropY"))))
			cropWidth = int(float(str(request.POST.get("cropWidth"))))
			cropHeight = int(float(str(request.POST.get("cropHeight"))))
   
			if cropX < 0:
				cropX = 0
			if cropY < 0: # There is a bug with cropperjs. y can be negative.
				cropY = 0
    
			crop_img = img[cropY:cropY+cropHeight, cropX:cropX+cropWidth]
			cv2.imwrite(url, crop_img)
			print("abcd")

			# delete the old image
			# check this first for profile picture related error
			# if user.profile_pic:
			user.profile_pic.delete()

			# Save the cropped image to user model
			print("before")
			user.profile_pic.save("profile_pic.png", files.File(open(url, 'rb')))
			print("after")
			user.save()
			print("check this ->")
			payload['result'] = "success"
			payload['cropped_profile_image'] = user.profile_pic.url

			# delete temp file
			os.remove(url)
			
		except Exception as e:
			print("exception: " + str(e))
			payload['result'] = "error"
			payload['exception'] = str(e)
   
	return HttpResponse(json.dumps(payload), content_type="application/json")
