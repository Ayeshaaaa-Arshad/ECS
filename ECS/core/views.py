from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class IndexPageView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'
    login_url = reverse_lazy('users:login')