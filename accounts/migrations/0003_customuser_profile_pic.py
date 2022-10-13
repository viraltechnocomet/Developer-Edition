# Generated by Django 3.2.12 on 2022-10-13 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profile_pic'),
            preserve_default=False,
        ),
    ]
