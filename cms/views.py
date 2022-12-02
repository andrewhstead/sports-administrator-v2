from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import LoginForm, NewCompetitionForm
from data.models import Sport, Country, Competition


# Create your views here.
@login_required(login_url='/login/')
def cms_home(request):
    user = request.user

    if user.is_authenticated:
        competitions = Competition.objects.all()

        return render(request, "cmshome.html", {'competitions': competitions})

    else:

        return redirect(reverse('login'))


@login_required(login_url='/login/')
def site_home(request):
    user = request.user

    if user.is_authenticated:

        competitions = Competition.objects.all()

        return render(request, "sitehome.html", {'competitions': competitions})

    else:

        return redirect(reverse('login'))


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in!")
                if user.is_superuser:
                    return redirect(request.GET.get('next') or reverse('site_home'))
                else:
                    return redirect(request.GET.get('next') or reverse('cms_home'))
            else:
                messages.error(request, "Your username or password was not recognised. Please try again.")

    else:
        form = LoginForm()

    args = {'form': form}

    args.update(csrf(request))
    return render(request, 'login.html', args)


@login_required(login_url='/login/')
def new_competition(request):

    if request.method == 'POST':
        form = NewCompetitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Competition has been created.')
            return redirect(reverse('cms_home'))
        else:
            messages.error(request, 'Sorry, we were unable to create the competition. Please try again.')

    else:
        form = NewCompetitionForm()

    args = {
        'form': form,
        'button_text': 'Create Competition'
    }

    args.update(csrf(request))
    return render(request, 'new_competition.html', args)


@login_required(login_url='/login/')
def new_user(request):

    if request.method == 'POST':
        form = NewCompetitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Competition has been created.')
            return redirect(reverse('cms_home'))
        else:
            messages.error(request, 'Sorry, we were unable to create the competition. Please try again.')

    else:
        form = NewCompetitionForm()

    args = {
        'form': form,
        'button_text': 'Create Competition'
    }

    args.update(csrf(request))
    return render(request, 'new_competition.html', args)
