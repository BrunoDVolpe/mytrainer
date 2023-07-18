from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

# Create your models here.
class UsersPlan(models.Model):
    """Model representing a possible user's contracted plan."""

    name = models.CharField(max_length=50)

    CONTRACTS = [
        ('M','Monthly'),
        ('T', 'Quaterly'),
        ('S', 'Biannually'),
        ('A', 'Yearly')
    ]
    contract_length = models.CharField(max_length=1, choices=CONTRACTS, default='M')
    package = models.ForeignKey('FrequencyPackage', on_delete=models.CASCADE)
    service = models.ForeignKey('ServicePlan', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class FrequencyPackage(models.Model):
    """Model representing the number of classes in a month."""

    title = models.CharField(max_length=50)
    month_frequency = models.SmallIntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class ServicePlan(models.Model):
    """Model representing the name of the service offered by the personal trainer."""
    title = models.CharField(max_length=50)

    def short(self):
        return self.title.split()[0].upper()
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title


class ClientProfile(models.Model):
    """Model representing the personal clients."""
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    name = models.CharField(max_length=100)
    client_email = models.EmailField(blank=True, null=True, default=None)
    plan = models.ForeignKey(UsersPlan, on_delete=models.SET_NULL, blank=True, null=True)
    personal_trainer = models.ForeignKey("TrainerProfile", on_delete=models.SET_NULL, blank=True, null=True)
    
    PAYMENT_DAY_OPTIONS = [
        (5, 'Dia 5'),
        (10, 'Dia 10'),
        (25, 'Dia 25'),
    ]
    payment_date = models.PositiveIntegerField(choices=PAYMENT_DAY_OPTIONS) #payment_day


    def get_absolute_url(self):
        """Return the url to access client details"""
        return reverse('client-detail', args=[str(self.id)])
        #"""Returns the url to access a detail record for this client and brings the first train of this client."""
        #return reverse('client-train', args=[str(self.id), '1'])
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class TrainerProfile(models.Model):
    """Model representing the personal trainer."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        permissions = [
            ("personal_trainer", "Can have access to personal trainer data")
        ]
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    

class StartPeriod(models.Model):
    """This class represents the beginning date of a period of 4 weeks training."""
    initial = models.DateField(unique=True)

    def get_weeks(self):
        dates = {
            'week_1_start': self.initial.strftime('%d/%m/%Y'),
            'week_1_end': (self.initial + datetime.timedelta(days=6)).strftime('%d/%m/%Y'),
            'week_2_start': (self.initial + datetime.timedelta(days=7)).strftime('%d/%m/%Y'),
            'week_2_end': (self.initial + datetime.timedelta(days=13)).strftime('%d/%m/%Y'),
            'week_3_start': (self.initial + datetime.timedelta(days=14)).strftime('%d/%m/%Y'),
            'week_3_end': (self.initial + datetime.timedelta(days=20)).strftime('%d/%m/%Y'),
            'week_4_start': (self.initial + datetime.timedelta(days=21)).strftime('%d/%m/%Y'),
            'week_4_end': (self.initial + datetime.timedelta(days=27)).strftime('%d/%m/%Y'),
            'week_5_start': (self.initial + datetime.timedelta(days=28)).strftime('%d/%m/%Y'),
            'week_5_end': (self.initial + datetime.timedelta(days=34)).strftime('%d/%m/%Y'),
        }
        return dates

    def get_month(self):
        port_months = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }
        return port_months[self.initial.month]

    def __str__(self):
        """Returns the month/year of the initial date.
        As initial can start and finish in another month, we add 1 week into the initial
         to get the right ones"""
        return f"{(self.initial + datetime.timedelta(days=7)).month}/{(self.initial + datetime.timedelta(days=7)).year}"

class TrainingInstance(models.Model):
    """This class represents a client's view classes and payment status for a monthly control."""
    begins_at = models.ForeignKey(StartPeriod, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)

    payment_status = models.BooleanField(default=False)

    CLASS_STATUS = (
        ('ok', 'Done!'),
        ('no', 'No'),
        ('gc', 'Given Class'),
        ('hd', 'Holiday'),
        ('na', '-')
    )

    MAX_LENGTH_STATUS = 2

    class1_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class2_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class3_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class4_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class5_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class6_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class7_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class8_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class9_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class10_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class11_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class12_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class13_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class14_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class15_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    class16_status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        choices=CLASS_STATUS,
        blank=True,
        help_text='Class status',
    )

    observations = models.TextField(max_length=1000, blank=True, help_text='Enter any observation about this month')

    @classmethod
    def create(cls, client_instance, period_instance):
        """Verify if there is a training instance with same month to user before creating"""
        queryset = TrainingInstance.objects.filter(client=client_instance)
        for instance in queryset:
            if instance.begins_at == period_instance:
                return None
        training_instance = cls(client=client_instance, begins_at=period_instance)
        training_instance.save()
        return training_instance

    def get_classes(self):
        return [self.class1_status, self.class2_status, self.class3_status, self.class4_status,
                self.class5_status, self.class6_status, self.class7_status, self.class8_status,
                self.class9_status, self.class10_status, self.class11_status, self.class12_status,
                self.class13_status, self.class14_status, self.class15_status, self.class16_status]
    

    def get_efficiency(self, classes):

        count = 0
        done = 0
        for class_status in classes:
            if class_status not in ['na', 'hd', '']:
                count += 1
            if class_status == 'ok' or class_status == 'gc':
                done += 1
    
        return {'done': done, 'count': count}


    def get_month_efficiency(self):
        
        data = self.get_efficiency(self.get_classes())
        done = data['done']
        count = data['count']

        if count:
            return f"{done} of {count} = {done/count*100:.2f}%"
        else:
            return "-"

    def get_week_efficiency(self):
        class_week_1 = self.get_classes()[:4]
        class_week_2 = self.get_classes()[4:8]
        class_week_3 = self.get_classes()[8:12]
        class_week_4 = self.get_classes()[12:16]
        class_week_5 = self.get_classes()[16:]

        data = {
            'week_1': f"{self.get_efficiency(class_week_1)['done']} / {self.get_efficiency(class_week_1)['count']}",
            'week_2': f"{self.get_efficiency(class_week_2)['done']} / {self.get_efficiency(class_week_2)['count']}",
            'week_3': f"{self.get_efficiency(class_week_3)['done']} / {self.get_efficiency(class_week_3)['count']}",
            'week_4': f"{self.get_efficiency(class_week_4)['done']} / {self.get_efficiency(class_week_4)['count']}",
            'week_5': f"{self.get_efficiency(class_week_5)['done']} / {self.get_efficiency(class_week_5)['count']}"
        }

        return data
    
    def get_absolute_url(self):
        """Return the url to access client's train"""
        return reverse('client-train', args=[str(self.client.id), str(self.id)])

    def __str__(self):
        return f"Month: {self.begins_at} | Client: {self.client}"