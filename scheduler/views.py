from django.shortcuts import render
from django.http import HttpResponse, response
from django.template import loader
from django.forms.models import model_to_dict
# Create your views here.
from .models import Schedule
def index(request):
    template = loader.render_to_string('schedule/index.html')
    context = {
        'schedule_list':'',
    }
    return HttpResponse(template)

def showall(request):
    schedule_list = Schedule.objects.all()
    template = loader.get_template('schedule/show.html')
    context = {
        'schedule_list':schedule_list,
    }
    return HttpResponse(template.render(context,request))

def category(request):
    template = loader.get_template('schedule/category.html')
    context = {
        'schedule_list':'',
    }
    return HttpResponse(template.render(context,request))

def catsubmit(request):
    date_check = request.POST['date']
    catname = request.POST['catname']
    schedule_list = Schedule.objects.get(date=date_check)
    print(model_to_dict(schedule_list))
    template = loader.get_template('schedule/showsome.html')
    context = {
        'date':date_check,
        'value':getattr(schedule_list,catname),
    }
    return HttpResponse(template.render(context,request))