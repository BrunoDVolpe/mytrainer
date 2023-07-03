from django import forms
from .models import (UsersPlan,
                     FrequencyPackage,
                     ServicePlan,
                     ClientProfile,
                     TrainerProfile,
                     StartPeriod,
                     TrainingInstance)
from django.core.exceptions import ValidationError


class TrainingInstanceUpdateForm(forms.ModelForm):
    class Meta:
        model = TrainingInstance
        widgets = {
          'observations': forms.Textarea(attrs={'rows':4, 'cols':100}),
        }
        fields = [
            'payment_status',
            'observations',
            'class1_status',
            'class2_status',
            'class3_status',
            'class4_status',
            'class5_status',
            'class6_status',
            'class7_status',
            'class8_status',
            'class9_status',
            'class10_status',
            'class11_status',
            'class12_status',
            'class13_status',
            'class14_status',
            'class15_status',
            'class16_status'
        ]
    

class ClientProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = 'Name'
        self.fields["name"].widget.attrs.update({'class': 'form-control',
                                        'placeholder': "Client's name",
                                        'autofocus': True})
        self.fields["client_email"].label = 'E-mail'
        self.fields["client_email"].widget.attrs.update({'class': 'form-control',
                                        'placeholder': "Client's email"})
        self.fields["plan"].widget.attrs.update({'class': 'form-control',
                                        'placeholder': "Client's plan"})
        self.fields["payment_date"].widget.attrs.update({'class': 'form-control',
                                        'placeholder': "Client's payment date"})

    class Meta:
        model = ClientProfile
        exclude = ['user', 'personal_trainer']


class StartPeriodCreateForm(forms.ModelForm):
    initial = forms.DateField(
        widget=forms.DateInput(format=('%d-%m-%Y'),
                               attrs={'class': 'startPeriodClass',
                                      'placeholder': 'Select a date',
                                      'type': 'date',
                                      }),
        label='Start of week 1',
        help_text='Select the date which starts the desired period.')
   
    class Meta:
        model = StartPeriod
        fields = ['initial']
