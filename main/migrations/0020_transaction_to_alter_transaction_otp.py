# Generated by Django 5.1 on 2024-11-07 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_transaction_to_alter_transaction_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.theatreadmin'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='otp',
            field=models.IntegerField(default=515042, editable=False),
        ),
    ]