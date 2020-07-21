from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import json
import boto3
from django.http import JsonResponse
from botocore.client import Config


# from django.contrib.auth.decorators import login_required
# from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator

# from .models import Document, PrivateDocument


def home(request):
    return render(request, 'home.html')

def upload(request):
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        image_type = request.POST['image_type']
        if settings.USE_S3:
            if image_type == 'private':
                pass
                # Public Upload Functionality
            else:
                pass
                # Private Upload functionality
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
            context = {
                "media_type": image_type,
                "image_url":image_url
            }
        return render(request, 'home.html',context)
    return render(request, 'home.html')

def fetch_url(request):
    # if request.method == 'POST':
    #     return HttpResponse("POST")
    # if request.method == 'GET':
    #     return HttpResponse('GET')
    return render(request, 'upload.html')

def get_upload_pre_sign_url(request):
    if request.method == 'GET':
        file_name = request.GET['file-name']
        file_type = request.GET['file-type']
        image_type = 'public'
        if settings.USE_S3:
            if image_type == 'private':
                pass
                # Public Upload Functionality
            else:
                # endpoint_url = settings.AWS_S3_ENDPOINT_URL,aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
                                    # aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY
                s3 = boto3.client('s3',aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
                                    aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
                                    region_name='ap-south-1')
                # settings.AWS_PUBLIC_MEDIA_LOCATION+"/"+
                
                presigned_post = s3.generate_presigned_post(
                    Bucket = settings.AWS_STORAGE_BUCKET_NAME,
                    Key = settings.AWS_PUBLIC_MEDIA_LOCATION+"/"+file_name,
                    Fields = {"acl": "public-read", "Content-Type": file_type},
                    # Fields = {"acl": "public-read"},
                    Conditions = [
                    {"acl": "public-read"},
                    {"Content-Type": file_type}
                    ],
                    ExpiresIn = 3600
                )
                # print(presigned_post)
                data ={
                    'data': presigned_post
                    # 'url': 'https://%s.s3.amazonaws.com/%s' % (settings.AWS_STORAGE_BUCKET_NAME, settings.AWS_PUBLIC_MEDIA_LOCATION)
                }
                # dump = json.dumps(data)
                # return HttpResponse(dump, content_type='application/json')
                # Public Upload functionality
                return JsonResponse(data)
        else:
            pass



# class DocumentCreateView(CreateView):
#     model = Document
#     fields = ['upload', ]
#     success_url = reverse_lazy('home')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         documents = Document.objects.all()
#         context['documents'] = documents
#         return context


# @method_decorator(login_required, name='dispatch')
# class PrivateDocumentCreateView(CreateView):
#     model = PrivateDocument
#     fields = ['upload', ]
#     success_url = reverse_lazy('profile')

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return super().form_valid(form)