from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from ...forms.register import RegisterForm

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, authenticated_user)

            return redirect("/")
    
    else:
        form = RegisterForm()
        context = {
            'form': form
        }

        return render(request, "registration/register.html", context)
