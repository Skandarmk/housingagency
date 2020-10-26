from django.shortcuts import render
from property.models import Property , Category
from .models import Service
from agents.models import Agent
from django.db.models import Count
# Create your views here.


def home(request):
    category_list = Category.objects.annotate(property_count=Count('property')).values('category_name' , 'property_count' , 'category_image')
    property_list = Property.objects.all()
    service_list = Service.objects.all()
    agent_list = Agent.objects.all()
    template = 'home/home.html'
    context = {
        'category_list' : category_list ,
        'property_list_home' : property_list ,
        'service_list' : service_list ,
        'agent_list' : agent_list ,
    }

    return render(request, template, context)