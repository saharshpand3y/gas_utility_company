# Generated by Django 5.1.3 on 2024-11-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0003_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('resolved', 'Resolved'), ('closed', 'Closed')], default='pending', max_length=20),
        ),
    ]
