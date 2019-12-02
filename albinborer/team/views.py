from django.shortcuts import render
from django.http import HttpResponse
from team.models import Designation,Member,AccessRecord
from team.forms import contactForm

# Create your views here.

def index(request):
        member = Member.objects.all()
        return render(request,'team.html', {'member': member })