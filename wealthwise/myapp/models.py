from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Wallet"

class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    plan = models.CharField(max_length=50, choices=[('vip', 'VIP'), ('Bronze', 'Bronze'), ('Diamond', 'Diamond')])
    method = models.CharField(max_length=50, choices=[('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum'), ('USDT', 'USDT')])
    status = models.CharField(max_length=20, default='Pending')  # Status can help track deposit states
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} ({self.plan})"


class Withdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    wallet_address = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Withdrawal #{self.id} - {self.user.username}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    verification_status = models.CharField(max_length=20, default='Not Verified')

    def __str__(self):
        return f"Profile of {self.user.username}"
