from django.urls import path
from .views import *
app_name = "main"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login", LoginView.as_view(), name="login"),
    path("signup", SignupView.as_view(), name="signup"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("movie/<str:movie_id>", MovieView.as_view(), name="movie"),
    path("setup", setup_view, name="setup"),
    path("show/<str:show_id>", ShowView.as_view(), name="show"),
    path("book/", BookView.as_view(), name="book"),
    path("ticket/<uuid:ticket_id>/cancel/",
         CancelTicketView.as_view(), name="cancel_ticket"),
    path("confirm/<uuid:transaction_id>/",
         ConfirmTransactionView.as_view(), name="confirm_transaction"),
    path("ticket/<uuid:ticket_id>/food/",
         FoodOrderView.as_view(), name="order_food"),
    path("wallet", wallet, name="wallet"),
    path("withdraw", withdraw, name="withdraw"),
    path("add", add, name="add"),
    path("404", not_found_404, name="404"),
]
