from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from cms.forms import LoginForm, NewCompetitionForm
from .models import User, Sport, Country


# Create your views here.
@login_required(login_url='/login/')
def site_home(request):
    user = request.user

    if user.is_authenticated:

        users = User.objects.all().order_by('date_modified')[:10]
        sports = Sport.objects.all().order_by('date_modified')[:10]
        countries = Country.objects.all().order_by('date_modified')[:10]

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
    return render(request, 'new_user.html', args)
