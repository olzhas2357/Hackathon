from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import CustomUser
from .forms import UserRegisterForm  # Ensure you create a form for user registration.

def home(request):
    """
    Displays the home page with some role-specific content.
    """
    return render(request, 'users/home.html', {})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data.get('role')  # Save the selected role

            # If the user is an admin, create a superuser
            if user.role == 'admin':
                user.is_superuser = True
                user.is_staff = True  # Staff permissions for admin to access the admin interface
                user.set_password(form.cleaned_data.get('password'))  # Ensure the password is hashed
                user.save()

                # Optionally, create a superuser through the Django ORM (if needed)
                # This is automatically done above with `user.set_password` and `user.save()`

                messages.success(request, f'Admin account created for {user.username}')
                return redirect('login')  # Redirect to login after creating an admin
            else:
                # If the role is not admin, save the user normally
                user.save()

            messages.success(request, f'Account created for {user.username}')
            return redirect('login')  # After registration, redirect to login
        else:
            print(form.errors)  # Debugging: Print form errors if any
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})


def user_login(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Check user role and redirect accordingly
            if user.is_superuser:  # Superuser check for admin
                return redirect(reverse('admin:index'))  # Redirect to Django admin panel
            elif user.role == 'teacher':
                return redirect('teacher_dashboard')  # Teacher dashboard
            elif user.role == 'student':
                return redirect('student_dashboard')  # Student dashboard
            else:
                return redirect('home')  # Default fallback
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

def redirect_user_by_role(user):
    """
    Redirects user to the appropriate dashboard based on their role.
    """
    if user.role == 'admin':
        return redirect('admin_dashboard')  # Replace with the actual admin dashboard URL
    elif user.role == 'teacher':
        return redirect('teacher_dashboard')  # Replace with the teacher dashboard URL
    elif user.role == 'student':
        return redirect('student_dashboard')  # Replace with the student dashboard URL
    else:
        return redirect('home')

@login_required
def user_logout(request):
    """
    Logs out the user and redirects to login page.
    """
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')



@login_required
def teacher_dashboard(request):
    """
    Dashboard view for teachers.
    """
    return render(request, 'users/teacher_dashboard.html')


@login_required
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')


@login_required
def student_dashboard(request):
    """
    Dashboard view for students.
    """
    return render(request, 'users/student_dashboard.html')