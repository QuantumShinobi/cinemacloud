from django.db import models
import uuid
import bcrypt
from django.shortcuts import redirect
from .utils import gen_otp


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.BinaryField(max_length=255)
    name = models.CharField(max_length=255)
    tickets = models.JSONField(default=None, null=True)
    money = models.IntegerField(default=1000)
    transaction_history = models.JSONField(default=None, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email_verified = models.BooleanField(default=False)

    def get_current_ticket(self):
        pass

    def authenticate(self, request):
        email = request.POST['email']
        password = request.POST['password']
        if bcrypt.checkpw(bytes(password, 'utf-8'), User.objects.get(email=email).password):
            user = User.objects.get(email=email)
            return user

    @staticmethod
    def get_user(request, path):
        try:
            request.COOKIES['user-identity']
        except KeyError:
            return redirect(f'main:{path}')
        try:
            user = User.objects.get(uuid=request.COOKIES['user-identity'])
        except User.objects.DoesNotExist:
            resp = redirect(f'main:{path}')
            resp.delete_cookie('user-identity')
            return resp
        else:
            return None


class SuperAdmin(models.Model):
    pass


class TheatreAdmin(models.Model):
    pass


# add logging later
class Log(models.Model):
    info = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=255, choices=[(
        'INFO', 'INFO'), ('ERROR', 'ERROR'), ('WARNING', 'WARNING')])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pass


class Ticket(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_date = models.DateTimeField(auto_now_add=True)
    movie_date = models.DateTimeField()
    price = models.IntegerField(default=100)
    used = models.BooleanField(default=False)
    transaction = models.ForeignKey(
        'Transaction', on_delete=models.CASCADE, null=True)
    food_orders = models.JSONField(default=None, null=True)
    cancelled = models.BooleanField(default=False)
    movie = models.JSONField(default=None, null=True)

    def get_orders(self):
        pass


class Transaction(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    # type = models.CharField(max_length=255, choices=[()])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField(default=gen_otp(), unique=False, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
