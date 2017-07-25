from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class WorkshopView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'workshop.html', context=None)

class DSSTView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'dsst.html', context=None)

class MLTView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'mlt.html', context=None)
