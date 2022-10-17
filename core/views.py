import os
import cv2
import json
import base64


from django.core import files
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

from django.conf import settings

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
)
from django.shortcuts import (
    render
)

from core.forms import CreateUserCustomForm, AddManagerForm


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

def save_temp_profile_image_from_base64String(imageString, user):
	INCORRECT_PADDING_EXCEPTION = "Incorrect padding"
	try:
		if not os.path.exists(settings.TEMP):
			os.mkdir(settings.TEMP)
		if not os.path.exists(settings.TEMP + "/" + str(user.pk)):
			os.mkdir(settings.TEMP + "/" + str(user.pk))
		url = os.path.join(settings.TEMP + "/" + str(user.pk),TEMP_PROFILE_IMAGE_NAME)
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

			# delete the old image
			user.profile_image.delet
			# Save the cropped image to user model
			user.profile_image.save("profile_image.png", files.File(open(url, 'rb')))
			user.save()

			payload['result'] = "success"
			payload['cropped_profile_image'] = user.profile_image.url

			# delete temp file
			os.remove(url)
			
		except Exception as e:
			print("exception: " + str(e))
			payload['result'] = "error"
			payload['exception'] = str(e)
	return HttpResponse(json.dumps(payload), content_type="application/json")


class AddManagerView(View):
    def get(self,request):
        form = AddManagerForm()(request.POST or None)
        return render(request, "core/add-manager.html", {"form": form })

    def post(self, request):
        msg     = None
        success = False

        if request.method == "POST":
            form = SignUpForm(request.POST)
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
                msg = ('Form is not valid',)
                form.add_error(None,'Form is not valid')
        else:
            form = SignUpForm()

        # return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
        return render(request,'core/add-manager.html', {"form": form, "msg" : msg, "success" : success })
