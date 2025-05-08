#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Property #, Address

# Create your views here.

# properties = [
#     {
#         'id': 0,
#         'street_name': 'Faxabraut',
#         'house_num': '130',
#         'city': 'Keflavík',
#         'postal_code': '230',
#         'description': 'Fancy house',
#         'type': 'blah',
#         'listing_price': '123',
#         'listing_date': '01.01.2025',
#         'is_sold': False,
#         'seller_id': 1,
#         'image': "https://i.pinimg.com/736x/02/13/7e/02137ec7e0a9be8227b5ef2a43837652.jpg",
#         'bed': '2',
#         'bathroom': '1',
#         'size': 'num',
#         'when': '2000'
#     }
# ]

def index(request):
    """get all properties"""
    all_properties = Property.objects.all()
    return  render(request,
                   "property/properties.html",
                   {'properties': all_properties,
                    })
    # latest_property_list = Property.objects.all().order_by('-listing_date')
    # output = {'latest_property_list': latest_property_list}
    # return HttpResponse(output)

    # return render(request, template_name="property/properties.html", context={
    #     "properties": properties
    # })

def get_property_by_id(request, prop_id):
    """return property with some id"""
    property_to_get = get_object_or_404(Property, pk=prop_id)
    return render(request,
                  "property/property_detail.html",
                  {"property": property_to_get
                   })


# def submit_offer(request, property_id):
#     try:
#         property_to_get = Property.objects.get(id=property_id)
#     except Property.DoesNotExist:
#         raise Http404("Property not found")
#     #TODO: implement offer