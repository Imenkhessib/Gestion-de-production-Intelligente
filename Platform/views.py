from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    name = "anonyme"
    if request.session.has_key('user_name'):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        name = request.session['user_name']
    return render(request, 'index.html', {'name': name})
def login(request):
    form: UserCreationForm = UserCreationForm()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'login.html', {'form': form})