from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
class Home(View):
  def get(self, request):
    return render(request, 'base/home.html')
  def post(self, request):
    button = request.POST.get('button-value')
    print(button)
    return render(request, 'base/home.html')
