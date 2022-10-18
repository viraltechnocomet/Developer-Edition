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

<<<<<<< HEAD
=======
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

>>>>>>> origin/viral-dev
def save_temp_profile_image_from_base64String(imageString, user):
	INCORRECT_PADDING_EXCEPTION = "Incorrect padding"
	try:
		if not os.path.exists(settings.TEMP):
			os.mkdir(settings.TEMP)
<<<<<<< HEAD
		if not os.path.exists(settings.TEMP + "/" + str(user.pk)):
			os.mkdir(settings.TEMP + "/" + str(user.pk))
		url = os.path.join(settings.TEMP + "/" + str(user.pk),TEMP_PROFILE_IMAGE_NAME)
		storage = FileSystemStorage(location=url)
		image = base64.b64decode(imageString)
		with storage.open('', 'wb+') as destination:
=======
		if not os.path.exists(os.path.join(settings.TEMP, str(user.pk))):
			os.mkdir(os.path.join(settings.TEMP, str(user.pk)))
		url = os.path.join(settings.TEMP,str(user.pk),TEMP_PROFILE_IMAGE_NAME)
		print(url)
		storage = FileSystemStorage(location=url)
		
		image = base64.b64decode(imageString)

		with storage.open('', 'wb+') as destination:
			
>>>>>>> origin/viral-dev
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
<<<<<<< HEAD
	if request.POST and user.is_authenticated:
		try:
			imageString = request.POST.get("image")
			url = save_temp_profile_image_from_base64String(imageString, user)
			img = cv2.imread(url)

=======
	
	if request.POST and user.is_authenticated:
		
		try:
			imageString = request.POST.get("image")
			url = save_temp_profile_image_from_base64String(imageString, user)
			
			img = cv2.imread(url)

		
>>>>>>> origin/viral-dev
			cropX = int(float(str(request.POST.get("cropX"))))
			cropY = int(float(str(request.POST.get("cropY"))))
			cropWidth = int(float(str(request.POST.get("cropWidth"))))
			cropHeight = int(float(str(request.POST.get("cropHeight"))))
<<<<<<< HEAD
=======
   
>>>>>>> origin/viral-dev
			if cropX < 0:
				cropX = 0
			if cropY < 0: # There is a bug with cropperjs. y can be negative.
				cropY = 0
<<<<<<< HEAD
			crop_img = img[cropY:cropY+cropHeight, cropX:cropX+cropWidth]

			cv2.imwrite(url, crop_img)

			# delete the old image
			user.profile_image.delet
			# Save the cropped image to user model
			user.profile_image.save("profile_image.png", files.File(open(url, 'rb')))
			user.save()

			payload['result'] = "success"
			payload['cropped_profile_image'] = user.profile_image.url
=======
    
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
>>>>>>> origin/viral-dev

			# delete temp file
			os.remove(url)
			
		except Exception as e:
			print("exception: " + str(e))
			payload['result'] = "error"
			payload['exception'] = str(e)
<<<<<<< HEAD
	return HttpResponse(json.dumps(payload), content_type="application/json")


class AddManagerView(View):

    def get(self,request):
        form = AddManagerForm()(request.POST or None)
        return render(request, "core/add-manager.html", {"form": form })

    def post(self, request):
        msg     = None
        success = False

        if request.method == "POST":
            form = AddManagerForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # group = Group.objects.get(name='client')
                username = form.cleaned_data.get("email")
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=username, password=raw_password)
                # user.groups.add(group)

                msg     = messages.add_message(request, messages.SUCCESS,'User created Successfully, Please Login!')
                success = True
                
                return redirect("/core/dashboard/")

            else:
                context['form'] = form
                msg = ('Form is not valid',)
                form.add_error(None,'Form is not valid')
        else:
            context['form'] = form
            form = AddManagerForm()
            context['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE

        # return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
        return render(request,'core/add-manager.html', {"form": form, "msg" : msg, "success" : success , "context": context})
=======
   
	return HttpResponse(json.dumps(payload), content_type="application/json")
>>>>>>> origin/viral-dev
