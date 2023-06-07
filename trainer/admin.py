from django.contrib import admin
from .models import (UsersPlan,
                     FrequencyPackage,
                     ServicePlan,
                     ClientProfile,
                     TrainerProfile,
                     StartPeriod,
                     TrainingInstance)

# Register your models here.
admin.site.register(UsersPlan)
admin.site.register(FrequencyPackage)
admin.site.register(ServicePlan)
admin.site.register(ClientProfile)
admin.site.register(TrainerProfile)
admin.site.register(StartPeriod)
admin.site.register(TrainingInstance)