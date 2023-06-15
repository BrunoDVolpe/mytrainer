from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import ClientProfile, TrainingInstance, TrainerProfile
from .forms import TrainingInstanceUpdateForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@permission_required('trainer.personal_trainer')
@login_required
def clientsList(request, *args, **kwargs):
    queryset = ClientProfile.objects.filter(personal_trainer__user=request.user)
    context = {
        'clients': queryset,
    }
    return render(request, 'clients_list.html', context)

@login_required
def clientDetail(request, id=id, pk_train=None, *args, **kwargs):
    queryset = get_object_or_404(ClientProfile, id=id)
    objs = TrainingInstance.objects.filter(client_id=id).order_by('-begins_at')
    # Pagination
    paginator = Paginator(objs, 1)
    page_number = request.GET.get("train", objs.count())
    page_obj = paginator.get_page(page_number)
    
    context = {
        'queryset': queryset,
        'page_obj': page_obj
    }
    return render(request, 'client_detail.html',context)

@login_required
def clientTrainUpdate(request, id, pk_train, *args, **kwargs):
    queryset = get_object_or_404(ClientProfile, id=id)
    obj = get_object_or_404(TrainingInstance, client_id=id, pk=pk_train)
    form = TrainingInstanceUpdateForm(request.POST or None, instance=obj)

    if form.is_valid():
        print("form válido")
    else:
        print("form inválido")
        form = TrainingInstanceUpdateForm(None, instance=obj)

    context = {
        'queryset': queryset,
        'obj': obj,
        'form': form,
    }
    return render(request, 'client_train_update.html', context)