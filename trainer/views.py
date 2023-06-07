from django.shortcuts import render, get_object_or_404
from .models import ClientProfile
from .forms import TrainingInstanceForm

# Create your views here.
def clientsList(request, *args, **kwargs):
    queryset = ClientProfile.objects.all()
    context = {
        'clients': queryset
    }
    return render(request, 'clients_list.html', context)

def clientDetail(request, id=id, *args, **kwargs):
    form = TrainingInstanceForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'client_detail.html',context)