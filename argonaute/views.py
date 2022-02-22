from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms

from .models import BoatTeam


class TeamForm(forms.ModelForm):

    class Meta:
        model = BoatTeam
        fields = ('name', )


# Create your views here.
def homepage(request):
    members = BoatTeam.objects.all()

    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('homepage'))
    else:
        form = TeamForm()

    return render(request, 'argonaute/homepage.html', {'members': members})
