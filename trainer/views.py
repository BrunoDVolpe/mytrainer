from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from .models import ClientProfile, TrainingInstance, TrainerProfile, StartPeriod
from .forms import (TrainingInstanceUpdateForm, ClientProfileForm,
                    StartPeriodCreateForm)
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse

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

    context = {
        'queryset': queryset,
        'trains': objs,
    }

    # Validating access to client's info. If not Trainer, 404 error
    if request.user != queryset.user:
        if get_object_or_404(TrainerProfile, user=request.user) != queryset.personal_trainer:
            raise PermissionDenied()
    
    return render(request, 'client_detail.html',context)


@login_required
def clientTrain(request, client_id, pk_train, *args, **kwargs):
    queryset = get_object_or_404(ClientProfile, id=client_id)
    trains = TrainingInstance.objects.filter(client_id=client_id).order_by('-begins_at')
    obj = get_object_or_404(TrainingInstance, client_id=client_id, pk=pk_train)
    
    context = {
        'queryset': queryset,
        'obj': obj,
        'trains': trains,
    }

    # Validating access to client's info. If not Trainer, 404 error
    if request.user != queryset.user:
        if get_object_or_404(TrainerProfile, user=request.user) != queryset.personal_trainer:
            raise PermissionDenied()
    
    return render(request, 'client_train.html',context)


@permission_required('trainer.personal_trainer')
@login_required
def clientTrainUpdate(request, client_id, pk_train, *args, **kwargs):
    queryset = get_object_or_404(ClientProfile, id=client_id)
    # Validating access to client's info. If not Trainer, 404 error
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


@permission_required('trainer.personal_trainer')
@login_required
def clientTrainCreate(request, client_id, *args, **kwargs):
    # Getting the client profile
    client_instance = get_object_or_404(ClientProfile, id=client_id)

    # Validating personal_trainer is the client's personal trainer
    if get_object_or_404(TrainerProfile, user=request.user) != client_instance.personal_trainer:
        raise PermissionDenied()
   
    # Form to create a new StartPeriod in the modal
    form_period = StartPeriodCreateForm()


    # Get available dates
    dates = StartPeriod.objects.all().order_by('-initial')


    if request.method == 'POST':
        initial_date = request.POST.get('start_date_id')
        if initial_date in [str(date.pk) for date in dates]:
            period = get_object_or_404(StartPeriod, pk=int(request.POST.get('start_date_id')))
            train = TrainingInstance.create(client_instance, period)
            if train:
                # Redirect to the trains page.
                return redirect(reverse("client-train-update", args=[client_id, train.pk]))
            messages.error(request, 'This client has already a train in this month')
        else:
            messages.error(request, 'Error. Train not created.')


    context = {
        'client': client_instance,
        'form': form_period,
        'dates': dates,
    }
    return render(request, 'client_train_create.html', context)


@permission_required('trainer.personal_trainer')
@login_required
def startPeriodCreate(request, *args, **kwargs):
    form_period = StartPeriodCreateForm(request.POST or None)
    if request.method == 'POST':
        if form_period.is_valid():
            form_period.save()
            messages.success(request, 'New date created successfully')
            return redirect(request.GET.get('next'))
        else:
            messages.error(request, 'Date already exist')
            return redirect(request.GET.get('next'))
    return HttpResponse(status=405)