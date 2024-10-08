from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from users.forms import SignupForm,LoginForm


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    
class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user) 
            return super().form_valid(form)  

        else:
            return self.form_invalid(form)


#Log out user
def logout_user(request):
    logout(request)
    return redirect('users:login')
