# Generated by Django 5.1.3 on 2024-11-14 23:22

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('snacks', 'snacks'), ('beverages', 'beverages'), ('combos', 'combos')], default='snacks', max_length=255)),
                ('food_id', models.BigIntegerField(default=None, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('movie_id', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=255)),
                ('popularity', models.FloatField()),
                ('adult', models.BooleanField()),
                ('overview', models.TextField()),
                ('poster_path', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('vote_average', models.FloatField()),
                ('backdrop_path', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('genre', models.JSONField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('screen_number', models.IntegerField()),
                ('seats', models.JSONField(default=None, null=True)),
                ('type', models.CharField(choices=[('2D', '2D'), ('3D', '3D'), ('IMAX', 'IMAX')], default='2D', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('shows', models.JSONField(blank=True, default=None, null=True)),
                ('admin_uuid', models.UUIDField(blank=True, default=None, null=True)),
                ('default_screen_id', models.UUIDField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.BinaryField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('tickets', models.JSONField(default=list, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('google_account', models.BooleanField(default=False, editable=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('bookings', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=100)),
                ('user_id', models.UUIDField(default=None, null=True)),
                ('transaction_history', models.JSONField(null=True)),
                ('th_admin_wallet', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('available_seats', models.IntegerField(default=100)),
                ('is_active', models.BooleanField(default=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.movie')),
                ('screen', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.screen')),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.theatre')),
            ],
        ),
        migrations.AddField(
            model_name='screen',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.theatre'),
        ),
        migrations.CreateModel(
            name='TheatreAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('phone', models.CharField(max_length=13, null=True)),
                ('theatre', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.theatre')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
                ('wallet', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.wallet')),
            ],
            options={
                'permissions': (('theateradmin', 'User is a theater admin'),),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('type', models.CharField(choices=[('add', 'add'), ('withdraw', 'withdraw'), ('refund', 'refund'), ('ticket', 'ticket'), ('food', 'food')], max_length=255, null=True)),
                ('otp', models.IntegerField(default=847598, editable=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('executed', models.BooleanField(default=False)),
                ('to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.theatreadmin')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('booked_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.BigIntegerField(default=100)),
                ('food_orders', models.JSONField(default=None, null=True)),
                ('cancelled', models.BooleanField(default=False)),
                ('used', models.BooleanField(default=False)),
                ('seats', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('booked', 'booked'), ('cancelled', 'cancelled'), ('used', 'used')], default='booked', max_length=255)),
                ('food_order_confirmed', models.BooleanField(default=False)),
                ('food_order_price', models.IntegerField(default=0)),
                ('show', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.show')),
                ('transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('INFO', 'INFO'), ('ERROR', 'ERROR'), ('WARNING', 'WARNING')], max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='wallet',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.wallet'),
        ),
    ]