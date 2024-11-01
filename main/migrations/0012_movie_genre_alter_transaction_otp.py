# Generated by Django 5.1 on 2024-11-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_theatre_uuid_alter_theatre_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='otp',
            field=models.IntegerField(default=651224, editable=False),
        ),
    ]
