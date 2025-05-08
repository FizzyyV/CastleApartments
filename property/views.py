from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

properties = [
    {
        'id': 0,
        'street_name': 'Faxabraut',
        'house_num': '130',
        'city': 'Keflavík',
        'postal_code': '230',
        'description': 'Fancy house',
        'type': 'blah',
        'listing_price': '123',
        'listing_date': '01.01.2025',
        'is_sold': False,
        'seller_id': 1,
        'image': "https://i.pinimg.com/736x/02/13/7e/02137ec7e0a9be8227b5ef2a43837652.jpg",
        'bed': '2',
        'bathroom': '1',
        'size': 'num',
        'when': '2000'
    }
]

def index(request):
    return render(request, template_name="property/properties.html", context={
        "properties": properties
    })

def get_property_by_id(request, id):
    property = [x for x in properties if x.id == id][0]

    return render(request, template_name="property/property_detail.html", context={
        "property": property
    })