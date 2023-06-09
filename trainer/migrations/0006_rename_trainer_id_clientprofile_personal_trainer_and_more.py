# Generated by Django 4.2.2 on 2023-06-09 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trainer', '0005_alter_clientprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientprofile',
            old_name='trainer_id',
            new_name='personal_trainer',
        ),
        migrations.RenameField(
            model_name='clientprofile',
            old_name='plan_id',
            new_name='plan',
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
