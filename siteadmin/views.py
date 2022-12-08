from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import NewUserForm, EditUserForm, EditSportForm, EditCountryForm
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
        form = NewUserForm()

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

    sport = get_object_or_404(Sport, name=name)

    if request.method == 'POST':
        form = EditSportForm(request.POST, request.FILES, instance=sport)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details have been saved.')
            return redirect(reverse('site_home'))
        else:
            messages.error(request, 'Sorry, we were unable to save the updated details. Please try again.')

    else:
        form = EditSportForm(instance=sport)

    args = {
        'form': form,
        'sport': sport,
        'button_text': 'Save Changes'
    }

    args.update(csrf(request))
    return render(request, 'sport_details.html', args)


@login_required(login_url='/login/')
def country_details(request, abbreviation):

    country = get_object_or_404(Country, abbreviation=abbreviation)

    if request.method == 'POST':
        form = EditCountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details have been saved.')
            return redirect(reverse('site_home'))
        else:
            messages.error(request, 'Sorry, we were unable to save the updated details. Please try again.')

    else:
        form = EditCountryForm(instance=country)

    args = {
        'form': form,
        'country': country,
        'button_text': 'Save Changes'
    }

    args.update(csrf(request))
    return render(request, 'country_details.html', args)
