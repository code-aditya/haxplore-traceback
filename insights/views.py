from django.shortcuts import render
from core.models import *
from .forms import StatUploadForm
# Create your views here.
def predictive(request):
    template_name='prediction.html'
    return render(request,template_name)

def trending (request):
    template_name='trending.html'
    context={
        # 'crops':Crop.objects.all(),
        'quantities':[(crop.name,crop.yields.filter(farmer__community=request.user.farmer.community).count()) for crop in Crop.objects.all()]
    }
    return render(request,template_name, context=context)

def stat_upload(request):
    template_name = 'stat_upload.html'
    context={
        'crops':Crop.objects.all(),
    }
    if request.method == "POST":
        post = request.POST
        data = dict(
            farmer=request.user.farmer,
            crop=post['crop'], yield_potential=post['expectation'],yield_effective=post['actual'],
            yield_wastage=post['wasted'],pesticides_used=post['pesticides'],investment=post['investment'],
            profit=post['profit']
        )
        form = StatUploadForm(data)
        if form.is_valid():
            form.save()
            redirect('trending')
        else:
            messages.warning(request,"Invalid form fields")
    return render(request,template_name)