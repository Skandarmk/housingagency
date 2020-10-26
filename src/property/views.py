from django.shortcuts import render

# Create your views here.
from .models import Property , Category , PropertyImages
from .forms import ReserveForm
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404


def property_list(request , category_slug=None):
    category = None
    property_list = Property.objects.all()
    category_list = Category.objects.annotate(total_properties=Count('property'))

    if category_slug :
        category = get_object_or_404(Category ,slug=category_slug)
        property_list = property_list.filter(category=category)


    adress_query = request.GET.get('q')
    property_type = request.GET.getlist('property_type' , None)
    furnished = request.GET.getlist('furnished' , None)
    purpose = request.GET.getlist('purpose' , None)
    price_cat = request.GET.getlist('price_category', None)

    if adress_query and property_type and furnished and purpose and price_cat :
        property_list = property_list.filter(
            Q(adress__icontains = adress_query) &
            Q(type__icontains = property_type[0]) &
            Q(furnished__icontains = furnished[0]) &
            Q(purpose__icontains = purpose[0]) &
            Q(pricecat__icontains = price_cat[0])
        ).distinct()




    paginator = Paginator(property_list, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    property_list = paginator.get_page(page)
    template = 'property/list.html'





    context = {
        'property_list' : property_list ,
        'category_list' : category_list ,
        'category' : category
    }

    return render(request, template , context)




def property_detail(request, property_slug):
    property_detail = Property.objects.get(slug=property_slug)
    property_images = PropertyImages.objects.filter(property=property_detail)
    template = 'property/detail.html'


    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()


    else:
        reserve_form = ReserveForm()


    context = {
        'property_detail' : property_detail ,
        'reserve_form' : reserve_form ,
        'property_images' : property_images
    }

    return render(request, template, context)
