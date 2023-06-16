from django import forms
from .models import (UsersPlan,
                     FrequencyPackage,
                     ServicePlan,
                     ClientProfile,
                     TrainerProfile,
                     StartPeriod,
                     TrainingInstance)
from django.core.exceptions import ValidationError

"""
class TrainingInstanceForm(forms.ModelForm):
    class Meta:
        model = TrainingInstance
        fields = [
            'begins_at',
            'client_id',
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
"""

class TrainingInstanceUpdateForm(forms.ModelForm):
    class Meta:
        model = TrainingInstance
        fields = [
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

    def clean(self):
        cleaned_data = super().clean()

        for data_key in cleaned_data:
            if not (any(cleaned_data[data_key] in class_status for class_status in TrainingInstance.CLASS_STATUS)) and cleaned_data[data_key] != '':
                print("erro")
                #Esse raise não está funcionando.
                raise forms.ValidationError("This is not a valid class status")
        return cleaned_data
    

class ClientProfileForm(forms.ModelForm):
    client_email = forms.EmailField(required=False)
    # Associar o email com user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    
    class Meta:
        model = ClientProfile
        exclude = ['user', 'personal_trainer']