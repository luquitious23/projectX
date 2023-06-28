
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import MyDataForm
from django.http import HttpResponse
from django.template import loader 
from .models import Member


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
    'mymembers': mymembers,
  }
    return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect URL
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def new_data_view(request):
    if request.method == 'POST':
        form = MyDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_list')  # Replace 'data_list' with the URL or route name for viewing the data list
    else:
        form = MyDataForm()
    return render(request, 'new_data.html', {'form': form})  
