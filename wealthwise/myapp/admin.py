from django.contrib import admin
# Register your models here.
from .models import Wallet, Deposit, Withdrawal, Profile

admin.site.register(Wallet)
admin.site.register(Deposit)
admin.site.register(Withdrawal)
admin.site.register(Profile)
