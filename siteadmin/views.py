from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import NewUserForm, EditUserForm
from cms.forms import NewCompetitionForm
from .models import User, Sport, Country


# Create your views here.
@login_required(login_url='/login/')
def site_home(request):
    user = request.user

    if user.is_authenticated:

        users = User.objects.all().order_by('-date_modified')[:10]
        sports = Sport.objects.all().order_by('-date_modified')[:10]
        countries = Country.objects.all().order_by('-date_modified')[:10]

        args = {
            'users': users,
            'sports': sports,
            'countries': countries
        }

        return render(request, "sitehome.html", args)

    else:

        return redirect(reverse('login'))


@login_required(login_url='/login/')
def new_user(request):

    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                messages.success(request, 'User was successfully created!')
                return redirect(request.GET.get('next') or reverse('site_home'))
            else:
                messages.error(request, 'Sorry, we were unable to create this user. Please try again.')

    else:
        form = NewUserForm(initial={'username': ''})

    args = {
        'form': form,
        'button_text': 'Register User'
    }
    args.update(csrf(request))
    return render(request, 'new_user.html', args)


@login_required(login_url='/login/')
def user_details(request, username):

    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details have been saved.')
            return redirect(reverse('site_home'))
        else:
            messages.error(request, 'Sorry, we were unable to save the user details. Please try again.')

    else:
        form = EditUserForm(instance=user)

    args = {
        'form': form,
        'user': user,
        'button_text': 'Save Changes'
    }

    args.update(csrf(request))
    return render(request, 'user_details.html', args)


@login_required(login_url='/login/')
def sport_details(request, name):

    if request.method == 'POST':
        form = NewCompetitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Competition has been created.')
            return redirect(reverse('site_home'))
        else:
            messages.error(request, 'Sorry, we were unable to create the competition. Please try again.')

    else:
        form = NewCompetitionForm()

    args = {
        'form': form,
        'button_text': 'Create Competition'
    }

    args.update(csrf(request))
    return render(request, 'sport_details.html', args)


@login_required(login_url='/login/')
def country_details(request, abbreviation):

    if request.method == 'POST':
        form = NewCompetitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Competition has been created.')
            return redirect(reverse('site_home'))
        else:
            messages.error(request, 'Sorry, we were unable to create the competition. Please try again.')

    else:
        form = NewCompetitionForm()

    args = {
        'form': form,
        'button_text': 'Create Competition'
    }

    args.update(csrf(request))
    return render(request, 'country_details.html', args)
