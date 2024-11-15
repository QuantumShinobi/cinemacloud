# Generated by Django 5.1 on 2024-11-07 07:03

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_wallet_remove_user_money_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theatre',
            name='theatre_admin',
        ),
        migrations.AddField(
            model_name='theatreadmin',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='theatreadmin',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='theatreadmin',
            name='password',
            field=models.BinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='theatreadmin',
            name='theatre',
            field=models.ManyToManyField(related_name='admin', to='main.theatre'),
        ),
        migrations.AddField(
            model_name='theatreadmin',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='theatreadmin',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='theatreadmin',
            name='wallet',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.wallet'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.theatreadmin'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='otp',
            field=models.IntegerField(default=479794, editable=False),
        ),
    ]