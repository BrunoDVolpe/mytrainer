from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from .models import ClientProfile, TrainingInstance, TrainerProfile
from .forms import TrainingInstanceUpdateForm, ClientProfileForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.urls import reverse

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
def clientDetail(request, client_id):
    queryset = get_object_or_404(ClientProfile, id=client_id)
    objs = TrainingInstance.objects.filter(client_id=client_id).order_by('-begins_at')
    
    # Validating access to client's info
    if get_object_or_404(TrainerProfile, user=request.user) != queryset.personal_trainer:
        raise PermissionDenied()

    context = {
        'queryset': queryset,
        'trains': objs,
    }
    return render(request, 'client_detail.html',context)


@login_required
def clientTrain(request, client_id, pk_train, *args, **kwargs):
    queryset = get_object_or_404(ClientProfile, id=client_id)
    # Validating access to client's info
    if get_object_or_404(TrainerProfile, user=request.user) != queryset.personal_trainer:
        raise PermissionDenied()
    trains = TrainingInstance.objects.filter(client_id=client_id).order_by('-begins_at')
    obj = get_object_or_404(TrainingInstance, client_id=client_id, pk=pk_train)
    
    context = {
        'queryset': queryset,
        'obj': obj,
        'trains': trains,
    }
    return render(request, 'client_train.html',context)


@permission_required('trainer.personal_trainer')
@login_required
def clientTrainUpdate(request, client_id, pk_train, *args, **kwargs):
    queryset = get_object_or_404(ClientProfile, id=client_id)
    # Validating access to client's info
    if get_object_or_404(TrainerProfile, user=request.user) != queryset.personal_trainer:
        raise PermissionDenied()
    obj = get_object_or_404(TrainingInstance, client_id=client_id, pk=pk_train)
    form = TrainingInstanceUpdateForm(request.POST or None, instance=obj)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # Redirect to a success page.
            return redirect(reverse("client-train", args=[client_id, pk_train]))
        else:
            print("form inválido") # Just validation

    context = {
        'queryset': queryset,
        'obj': obj,
        'form': form,
    }
    return render(request, 'client_train_update.html', context)


@permission_required('trainer.personal_trainer')
@login_required
def clientCreate(request):
    form = ClientProfileForm(request.POST or None)
    if request.method == 'POST':
        # Create a form instance with POST data.
        if form.is_valid():
            try:
                client = User.objects.get(email=form.cleaned_data['client_email'])
            except:
                client = None
            personal_trainer = TrainerProfile.objects.get(user=request.user)
            # Create, but don't save the new client instance.
            new_client = form.save(commit=False)
            new_client.user = client
            new_client.personal_trainer = personal_trainer
            # Save the new instance.
            new_client.save()
            # Save the many-to-many data for the form.
            form.save_m2m()
            return redirect('clients-list')
            
    context = {
        'form': form,
    }
    return render(request, 'create_client.html', context)