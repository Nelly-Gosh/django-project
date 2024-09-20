from django.shortcuts import render, redirect,get_object_or_404
from .models import Wallet, Deposit, Withdrawal, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .forms import CustomUserCreationForm,DepositForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.core.mail import send_mail  # Import send_mail for sending emails
from django.conf import settings  # Import settings for email configurations
from django.db.models import Sum  

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def invest(request):
    return render(request, 'invest.html')

def services(request):
    return render(request, 'services.html')
def reinvest(request):
    return render(request,'re-invest.html')

def withdraw(request):
    return render(request,'withdraw.html')
def transactions(request):
    return render(request,'transactions.html')

@login_required
def deposit(request):
    wallet = Wallet.objects.get(user=request.user)
    deposits = Deposit.objects.filter(user=request.user, status="Approved")  # Filter only approved deposits
    withdrawals = Withdrawal.objects.filter(user=request.user)

    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.status = 'Approved'  # Automatically approve the deposit (adjust logic as needed)
            deposit.save()
            return redirect('dashboard')  # Redirect to the dashboard after a successful deposit
    else:
        form = DepositForm()

    # Calculate total deposits (approved)
    total_deposits = deposits.aggregate(Sum('amount'))['amount__sum'] or 0.00

    context = {
        'wallet': wallet,
        'total_deposits': total_deposits,
        'total_withdrawals': withdrawals.aggregate(Sum('amount'))['amount__sum'] or 0.00,
        'form': form,
    }

    return render(request, 'deposit.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            # Create a Profile for the user with the additional details
            Profile.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                country=form.cleaned_data['country'],
                phone_number=form.cleaned_data['phone_number']
            )

            # Send a welcome email
            subject = 'Welcome to WealthWise!'
            message = f"Hi {user.username},\n\nThank you for signing up to WealthWise!"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            
            send_mail(subject, message, from_email, recipient_list)

            # Log in the user and redirect to the dashboard
            auth_login(request, user)
            return redirect('Dashboard')
        else:
            messages.error(request, "An error occurred during registration")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('Dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

@login_required
def dashboard(request):
    wallet, created = Wallet.objects.get_or_create(user=request.user)
    profile = get_object_or_404(Profile, user=request.user)

    deposits = Deposit.objects.filter(user=request.user)
    withdrawals = Withdrawal.objects.filter(user=request.user)

    context = {
        'wallet': wallet,
        'deposits': deposits,
        'withdrawals': withdrawals,
        'profile': profile,  # Include profile in context
    }

    return render(request, 'dashboard.html', context)



# class CreatePaymentView(APIView):
#     def post(self, request):
#         # Get the required data from the request (e.g., cryptocurrency, amount, callback URL, etc.)
#         crypto = request.data.get('crypto', 'btc')  # Default to Bitcoin if not specified
#         amount = request.data.get('amount', 0.01)   # Specify the amount in the respective cryptocurrency

#         # CryptAPI endpoint for generating a payment address
#         cryptapi_url = f'https://api.cryptapi.io/{crypto}/create/?callback={withdraw}'

#         # Make a request to CryptAPI to create a new payment address
#         try:
#             response = requests.get(cryptapi_url)
#             data = response.json()

#             if response.status_code == 200:
#                 return Response(data, status=status.HTTP_200_OK)
#             else:
#                 return Response(data, status=status.HTTP_400_BAD_REQUEST)

#         except requests.exceptions.RequestException as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class PaymentCallbackView(APIView):
#     def post(self, request):
#         # Extract payment information from the callback
#         payment_data = request.data

#         # Perform any necessary processing, like updating the user's balance, verifying payment, etc.
#         # For example:
#         tx_id = payment_data.get('tx_id')
#         status = payment_data.get('status')
#         amount_received = payment_data.get('value')

#         # Update your database or perform any other necessary actions

#         return Response({"message": "Callback received"}, status=status.HTTP_200_OK)