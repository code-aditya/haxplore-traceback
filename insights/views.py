from django.shortcuts import render
from core.models import *
# Create your views here.
def predictive(request):
    template_name='prediction.html'
    return render(request,template_name)

def trending (request):
    template_name='trending.html'
    context={
        # 'crops':Crop.objects.all(),
        'quantities':[(crop.name,crop.farmercropyield_set.filter(farmer__community=request.user.farmer.community).count()) for crop in Crop.objects.all()]
    }
    return render(request,template_name, context=context)