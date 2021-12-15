from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import uuid
from .models import Url
# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        n_url = Url(link = url, uuid = uid)
        n_url.save()
        return HttpResponse(uid)

def go(request,pk):
    urlDetails = Url.objects.get(uuid=pk)
    return redirect(urlDetails.link)

