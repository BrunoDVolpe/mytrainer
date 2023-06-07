from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

# Create your models here.
class UsersPlan(models.Model):
    """Model representing a possible user's contracted plan."""

    name = models.CharField(max_length=50)

    CONTRACTS = [
        ('M','Mensal'),
        ('T', 'Trimestral'),
        ('S', 'Semestral'),
        ('A', 'Anual')
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

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
class ClientProfile(models.Model):
    """Model representing the personal clients."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    plan_id = models.ForeignKey(UsersPlan, on_delete=models.SET_NULL, blank=True, null=True)
    trainer_id = models.ForeignKey("TrainerProfile", on_delete=models.SET_NULL, blank=True, null=True)
    PAYMENT_DATE_OPTIONS = [
        (5, 'Dia 5'),
        (10, 'Dia 10'),
        (25, 'Dia 25'),
    ]
    payment_date = models.PositiveIntegerField(choices=PAYMENT_DATE_OPTIONS)


    def get_absolute_url(self):
        """Returns the url to access a detail record for this client."""
        return reverse('client-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class TrainerProfile(models.Model):
    """Model representing the personal trainer."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    

class StartPeriod(models.Model):
    """This class represents the beginning date of a period of 4 weeks training."""
    initial = models.DateField(unique=True)

    def __str__(self):
        return f"{self.initial.month}/{self.initial.year}"

class TrainingInstance(models.Model):
    """This class represents a client's view classes and payment status for a monthly control."""
    begins_at = models.ForeignKey(StartPeriod, on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)

    WEEK_STATUS = (
        ('?', 'Feito!'),
        ('?', 'Não'),
        ('?', '1/2'),
        ('?', '1/3'),
        ('?', '2/3'),
        ('?', 'Aula dada'),
        ('?', 'Feriado'),
    )

    CLASS_STATUS = (
        ('ok', 'Feito!'),
        ('no', 'Não'),
        ('gc', 'Aula dada'),
        ('hd', 'Feriado'),
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

    def __str__(self):
        return f"Início: {self.begins_at} | Aluno: {self.client_id}"