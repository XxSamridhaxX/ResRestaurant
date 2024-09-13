from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, FormView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer
from .forms import CustomerRegistrationForm, CustomerLoginForm


# Function-based view
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'app1/customer_list.html', {'customers': customers})

# OR: Using a Class-based view
class CustomerListView(ListView):
    model = Customer
    template_name = 'app1/customer_list.html'
    context_object_name = 'customers'

class CustomerRegistrationView(CreateView):
    template_name = "app1/register.html"
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy("app1:customer_list")
    # after successful register redirect to customer_list(name)

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            form.add_error('username', 'Username already exists')
            return self.form_invalid(form)

        # Check if a user with the same email address already exists
        if User.objects.filter(email=email).exists():
            form.add_error('email', 'Email address already in use')
            return self.form_invalid(form)

        new_user = User.objects.create_user(username, email, password)
        form.instance.user = new_user
        login(self.request, new_user)
        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url


class CustomerLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("app1:home")  # Redirect to home page


class CustomerLoginView(FormView):
    template_name = "app1/customerlogin.html"
    form_class = CustomerLoginForm
    success_url = reverse_lazy("app1:userprofile_")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data.get("password")
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Customer.objects.filter(user=usr).exists():
            login(self.request, usr)
            
            # Store custom session data (e.g., user_id, username)
            self.request.session['customer_id'] = usr.id
            self.request.session['email'] = usr.email
        else:
            return render(self.request, self.template_name, {"form": self.form_class(), "error": "Invalid credentials"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url

# New view: CustomerProfileView
# class CustomerProfileView(View):
#     template_name = "app1/customer_profile.html"

#     def get(self, request):
#         customer = Customer.objects.get(user=request.user)
#         return render(request, self.template_name, {'customer': customer})

#To show user profile 


class UserProfileView(LoginRequiredMixin, View):
    template_name = "app1/user_profile.html"

    def get(self, request):
        # Retrieve session data
        user_id = request.session.get('user_id')
        username = request.session.get('username')

        # Optional: Fetch customer data based on the session data
        try:
            customer = Customer.objects.get(user__id=user_id)
        except Customer.DoesNotExist:
            customer = None

        # Pass the session data and customer info to the template
        return render(request, self.template_name, {
            'user_id': user_id,
            'username': username,
            # 'customer': customer,
        })