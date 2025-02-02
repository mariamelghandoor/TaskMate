from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from signup.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import re

def is_valid_email(email):
    """
    Validates an email address format using regex.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


# View to render the homepage
def home(request):
    """
    Renders the base/homepage of the application.

    Parameters:
    - request: HttpRequest object containing metadata about the request.

    Returns:
    - Rendered HTML template 'users/base.html'.
    """
    return render(request, 'users/base.html')

# View to handle user signup
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        confirm_password = request.POST.get("confirm_password", "").strip()

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html', {
                'form_data': {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email
                }
            })
        
        if not is_valid_email(email):
            messages.error(request, "Enter a valid email address.")
            return render(request, 'signup.html', {
                'form_data': {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email
                }
            })

        # Ensure all fields are filled
        if not all([first_name, last_name, email, password, confirm_password]):
            messages.info(request, "All fields are required.")
            return render(request, 'signup.html', {
                'form_data': {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email
                }
            })

        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return render(request, 'signup.html', {
                'form_data': {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email
                }
            })

        # Create the new user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        # Notify user of success
        messages.success(request, "Signup successful! Please check your email to verify your account.")
        return redirect("login") 

    return render(request, 'signup.html')

# View to activate user account through email
def activate_mail(request, uidb64, token):
    """
    Activates a user account based on email verification.

    Parameters:
    - request: HttpRequest object.
    - uidb64: Base64-encoded user ID.
    - token: Token for email verification.

    Returns:
    - On success: Redirects to login with a success message.
    - On failure: Redirects to signup with an error message.
    """
    try:  
        # Decode user ID and fetch user
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(id=uid)  
        if user is not None: 
            user.is_verified = True  # Mark user as verified
            user.save()
            messages.success(request, 'Email confirmation done successfully')
            return redirect('login')
    except User.DoesNotExist: 
        # Handle invalid user cases
        messages.error(request, "Please sign up.") 
        return redirect('signup')

# View to create a new user with hashed password
def create_user(request):
    """
    Handles the creation of a new user:
    - Hashes the provided password.
    - Saves the user to the database.

    Parameters:
    - request: HttpRequest object containing form data submitted via POST.

    Returns:
    - On success: Redirects to login page.
    """
    if request.method == "POST":
        # Extract username and password from form
        username = request.POST['username']
        password = request.POST['password']
        
        # Hash the password before saving
        hashed_password = make_password(password)
        user = User.objects.create(username=username, password=hashed_password)
        user.save()
        
        return redirect('login')
    
    return render(request, 'signup.html')
