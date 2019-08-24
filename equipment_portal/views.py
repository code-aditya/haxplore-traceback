from django.shortcuts import render
from core.models import *
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
# Create your views here.

def equipments_list(request):
    equipments = Equipment.objects.filter(end_dt__gte = now() ).order_by('-timestamp')
    context = {
        'equipments':equipments,
    }
    return render(request, 'equipment_list.html', context=context)

def equipment_new(request):
    return render(request, 'equipment_upload.html')

def equipment_detail(request, pk):
    template_name = 'equipment_detail.html'
    context={
        'equipment':get_object_or_404(Equipment,pk=pk),
    }
    return render(request, template_name, context=context)