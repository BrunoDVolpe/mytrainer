from django import forms
from .models import (UsersPlan,
                     FrequencyPackage,
                     ServicePlan,
                     ClientProfile,
                     TrainerProfile,
                     StartPeriod,
                     TrainingInstance)

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