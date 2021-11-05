# Generated by Django 3.2.8 on 2021-11-04 15:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organisation', '0007_alter_organisation_contact_no'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='member',
            unique_together={('user', 'organisation')},
        ),
    ]