# Generated by Django 5.1.3 on 2024-11-14 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_alter_transaction_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='otp',
            field=models.IntegerField(default=948123, editable=False),
        ),
    ]