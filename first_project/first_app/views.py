from django.shortcuts import render
from first_app.models import User
from .forms import NewUserForm
# Create your views here.

def index(request):
    webpages_list = User.objects.all()
    user_dictb = {'user_dict':webpages_list}

    return render(request,'first_app/index.html', context=user_dictb)

def signup(request):

    form=NewUserForm()

    if request.method == "POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error fill all')
    return render(request,'first_app/signup.html',{'form':form})