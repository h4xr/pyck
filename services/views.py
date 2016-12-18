from django.shortcuts import render
from django.views import View

class HomeView(View):
    ''' The home page view '''

    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
