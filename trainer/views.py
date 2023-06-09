from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import ClientProfile, TrainingInstance
from .forms import TrainingInstanceForm

# Create your views here.
def clientsList(request, *args, **kwargs):
    queryset = ClientProfile.objects.all()
    context = {
        'clients': queryset
    }
    return render(request, 'clients_list.html', context)

def clientDetail(request, id=id, *args, **kwargs):
    #queryset = ClientProfile.objects.get(id=id)
    queryset = get_object_or_404(ClientProfile, id=id)
    #obj = TrainingInstance.objects.get(id=id)
    objs = TrainingInstance.objects.filter(client_id=id).order_by('-begins_at')
    #obj = objs[int(request.GET.get('train', objs.count() - 1))] #substituir esse por get_object usando um filtro no objs
    #print('last: ', objs.last())
    #print('first:', objs.first())
    #print('order by date:', objs.order_by('begins_at'))
    #print('order by -date:', objs.order_by('-begins_at'))
    
    # Pagination
    paginator = Paginator(objs, 1)
    page_number = request.GET.get("train")
    page_obj = paginator.get_page(page_number)    

    #form = TrainingInstanceForm(request.POST or None, instance=obj)
    context = {
        'queryset': queryset,
        'page_obj': page_obj
    }
    return render(request, 'client_detail.html',context)