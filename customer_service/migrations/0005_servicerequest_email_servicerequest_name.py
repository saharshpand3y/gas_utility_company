# Generated by Django 5.1.3 on 2024-11-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0004_alter_servicerequest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
