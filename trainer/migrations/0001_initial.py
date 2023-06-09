# Generated by Django 4.2.2 on 2023-06-06 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('payment_date', models.PositiveIntegerField(choices=[(5, 'Dia 5'), (10, 'Dia 10'), (25, 'Dia 25')])),
            ],
        ),
        migrations.CreateModel(
            name='FrequencyPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('month_frequency', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StartPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsersPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contract_length', models.CharField(choices=[('M', 'Mensal'), ('T', 'Trimestral'), ('S', 'Semestral'), ('A', 'Anual')], default='M', max_length=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.frequencypackage')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.serviceplan')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class1_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class2_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class3_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class4_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class5_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class6_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class7_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class8_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class9_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class10_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class11_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class12_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class13_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class14_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class15_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('class16_status', models.CharField(blank=True, choices=[('ok', 'Feito!'), ('no', 'Não'), ('gc', 'Aula dada'), ('hd', 'Feriado'), ('na', '-')], help_text='Class status', max_length=2)),
                ('observations', models.TextField(help_text='Enter any observation about this month', max_length=1000)),
                ('begins_at', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trainer.startperiod')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.clientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='TrainerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='plan_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainer.usersplan'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='trainer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainer.trainerprofile'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
