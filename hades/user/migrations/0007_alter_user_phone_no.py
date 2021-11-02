# Generated by Django 3.2.8 on 2021-11-02 12:12

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(max_length=10, null=True, validators=[user.models.validate_phone_no]),
        ),
    ]