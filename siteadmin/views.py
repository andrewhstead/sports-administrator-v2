from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import NewUserForm, EditUserForm, SportForm, CountryForm, StateForm
from .models import User, Sport, Country, State


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
        form = SportForm(request.POST, request.FILES, instance=sport)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details have been saved.')
            return redirect(reverse('site_home'))
        else:
            messages.error(request, 'Sorry, we were unable to save the updated details. Please try again.')

    else:
        form = SportForm(instance=sport)

    args = {
        'form': form,
        'sport': sport,
        'button_text': 'Save Changes'
    }

    args.update(csrf(request))
    return render(request, 'sport_details.html', args)


@login_required(login_url='/login/')
def new_sport(request):

    if request.method == 'POST':
        form = SportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New sport has been added.')
            return redirect(reverse('site_home'))
        else:
            messages.error(request, 'Sorry, we were unable to add the new sport. Please try again.')

    else:
        form = SportForm()

    args = {
        'form': form,
        'button_text': 'Save Details'
    }

    args.update(csrf(request))
    return render(request, 'new_sport.html', args)


@login_required(login_url='/login/')
def country_details(request, abbreviation):

    country = get_object_or_404(Country, abbreviation=abbreviation)
    states = country.state_country.all()

    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details have been saved.')
            return redirect(reverse('site_home'))
        else:
            messages.error(request, 'Sorry, we were unable to save the updated details. Please try again.')

    else:
        form = CountryForm(instance=country)

    args = {
        'form': form,
        'country': country,
        'button_text': 'Save Changes',
        'states': states
    }

    args.update(csrf(request))
    return render(request, 'country_details.html', args)


@login_required(login_url='/login/')
def state_details(request, country, state):

    country = get_object_or_404(Country, abbreviation=country)
    state = get_object_or_404(State, country=country.id, abbreviation=state)

    if request.method == 'POST':
        form = StateForm(request.POST, request.FILES, instance=state)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details have been saved.')
            return redirect(reverse('site_home'))
        else:
            messages.error(request, 'Sorry, we were unable to save the updated details. Please try again.')

    else:
        form = StateForm(instance=state)

    args = {
        'form': form,
        'state': state,
        'button_text': 'Save Changes'
    }

    args.update(csrf(request))
    return render(request, 'state_details.html', args)


@login_required(login_url='/login/')
def new_country(request):

    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New country has been added.')
            return redirect(reverse('all_countries'))
        else:
            messages.error(request, 'Sorry, we were unable to add the new country. Please try again.')

    else:
        form = CountryForm()

    args = {
        'form': form,
        'button_text': 'Save Details'
    }

    args.update(csrf(request))
    return render(request, 'new_country.html', args)


@login_required(login_url='/login/')
def all_countries(request):

    world = Country.objects.all()

    # Use pagination to restrict the number displayed at any one time.
    country_list = Paginator(world, 25)

    page = request.GET.get('page')

    if page:
        current_page = int(page)
    else:
        current_page = 1

    page_count = country_list.num_pages

    page = request.GET.get('page')
    try:
        countries = country_list.page(page)
    except EmptyPage:
        countries = country_list.page(country_list.num_pages)
    except PageNotAnInteger:
        countries = country_list.page(1)

    args = {
        'countries': countries,
        "current_page": current_page,
        "page_count": page_count
    }

    args.update(csrf(request))
    return render(request, 'all_countries.html', args)
