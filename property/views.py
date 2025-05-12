
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Property #, Address

# Create your views here.

properties = [
    {
        'id': 0,
        'street_name': 'Faxabraut',
        'house_num': '120',
        'city': 'Keflavík',
        'postal_code': '230',
        'listing_price': '81.000.000 kr.',
        'is_sold': False,
        'seller_id': 1,
        'image': "https://i.pinimg.com/736x/02/13/7e/02137ec7e0a9be8227b5ef2a43837652.jpg",
        'bed': '2',
        'bathroom': '1',
        'size': '848.708m2',
        'built': '2020',
        'listing_date': '30.04.2024',
        'type': 'Town House',
        'description': 'Fancy house'
    }
]

def index(request):
     return render(request, template_name="property/properties.html", context={
         "properties": properties
     })

def get_property_by_id(request, property_id):
    property = next((x for x in properties if x ['id'] == property_id), None)
    if property is None:
        return HttpResponse("Property not found", status=404)

    return render(request, template_name="property/property_detail.html", context={
        "property": property
    })

# someone changed my code so idk what this is below

#def index(request):
    #"""get all properties"""
    #all_properties = Property.objects.all()
    #return  render(request,
                   #"property/properties.html",
                   #{'properties': all_properties,
                    #})
    # latest_property_list = Property.objects.all().order_by('-listing_date')
    # output = {'latest_property_list': latest_property_list}
    # return HttpResponse(output)

    # return render(request, template_name="property/properties.html", context={
    #     "properties": properties
    # })

#def get_property_by_id(request, prop_id):
    #"""return property with some id"""
    #property_to_get = get_object_or_404(Property, pk=prop_id)
    #return render(request,
                  #"property/property_detail.html",
                  #{"property": property_to_get
                   #})


# def submit_offer(request, property_id):
#     try:
#         property_to_get = Property.objects.get(id=property_id)
#     except Property.DoesNotExist:
#         raise Http404("Property not found")
#     #TODO: implement offer