from django.shortcuts import render
from django.views import View
from .forms import GalleryUploadForm
from django.http import HttpResponseRedirect



# Create your views here.

def storage_file(file):
    file_name = file.name
    with open(f'gallery_tmp/{file_name}.jpg', 'wb+') as new_file:
        for chunk in file.chunks():
            new_file.write(chunk)


class GalleryView(View):

    def get(self, request):
        form = GalleryUploadForm()
        return render(request, 'gallery/load_file.html', {'form': form})

    def post(self, request):
        form = GalleryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            storage_file(form.cleaned_data['image'])
            return HttpResponseRedirect('load_image')
        storage_file(request.FILES['image'])
        return render(request, 'gallery/load_file.html', {'form': form})
