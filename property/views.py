
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Property #, Address


from django.contrib.sessions.models import Session

def session_debug(request):
    sessions = Session.objects.all()
    return render(request, 'session_debug.html', {'sessions': sessions})


# Create your views here.

# Corrected properties list in views.py
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
        'size': '848.708m²',
        'built': '2020',
        'listing_date': '30.04.2024',
        'type': 'Town House',
        'description': 'Fancy house',
        'seller_name': 'John Smithy',
        'bed_icon': 'https://i.postimg.cc/vBj3YZW5/image-1.png',
        'bath_icon': 'https://i.postimg.cc/SQ2gZchd/image-2.png',
        'built_icon': 'https://i.postimg.cc/sgNB0GyP/image-3.png',
        'images': [
            "https://i.pinimg.com/736x/02/13/7e/02137ec7e0a9be8227b5ef2a43837652.jpg",
            "https://i.pinimg.com/474x/41/ce/b1/41ceb16c038f914ddad1a165f5da4868.jpg",
            "https://i.pinimg.com/474x/cd/58/08/cd58082240cdca4c89e284a6bf782a37.jpg"
        ],
    },
    {
        'id': 1,
        'street_name': 'Faxabraut',
        'house_num': '30',
        'city': 'Keflavík',
        'postal_code': '230',
        'listing_price': '70.000.000 kr.',
        'is_sold': True,
        'seller_id': 1,
        'image': "https://i.pinimg.com/736x/ae/0f/f8/ae0ff820b7d2738b668f2d7150b180cd.jpg",
        'bed': '2',
        'bathroom': '1',
        'size': '749.196m²',
        'built': '2018',
        'listing_date': '30.04.2024',
        'type': 'Detached House',
        'description': 'Pretty House',
        'seller_name': 'John Smithy',
        'bed_icon': 'https://i.postimg.cc/vBj3YZW5/image-1.png',
        'bath_icon': 'https://i.postimg.cc/SQ2gZchd/image-2.png',
        'built_icon': 'https://i.postimg.cc/sgNB0GyP/image-3.png',
        'images': [
            "https://i.pinimg.com/736x/ae/0f/f8/ae0ff820b7d2738b668f2d7150b180cd.jpg",
            "https://example.com/image2.jpg",
            "https://example.com/image3.jpg"
        ],
    },

    {
        'id': 2,
        'street_name': 'Birkihlíð',
        'house_num': '45',
        'city': 'Reykjavík',
        'postal_code': '101',
        'listing_price': '95.500.000 kr.',
        'is_sold': False,
        'seller_id': 0,
        'image': 'https://i.pinimg.com/736x/8f/6f/07/8f6f07b1e4254eed9f4dac2080b9057a.jpg',
        'bed': '3',
        'bathroom': '2',
        'size': '920.453m²',
        'built': '2021',
        'listing_date': '05.05.2024',
        'type': 'Modern Villa',
        'description': 'Spacious modern villa with a garden view.',
        'seller_name': 'John Smithy',
        'bed_icon': 'https://i.postimg.cc/vBj3YZW5/image-1.png',
        'bath_icon': 'https://i.postimg.cc/SQ2gZchd/image-2.png',
        'built_icon': 'https://i.postimg.cc/sgNB0GyP/image-3.png',
        'images': [
            "https://i.pinimg.com/736x/8f/6f/07/8f6f07b1e4254eed9f4dac2080b9057a.jpg",
            "https://example.com/image2.jpg",
            "https://example.com/image3.jpg"
        ],
    },

    {
        'id': 3,
        'street_name': 'Lindargata',
        'house_num': '78',
        'city': 'Akureyri',
        'postal_code': '600',
        'listing_price': '65.000.000 kr.',
        'is_sold': False,
        'seller_id': 0,
        'image': 'https://i.pinimg.com/736x/f6/65/48/f66548110843eda678d70692dd528dda.jpg',
        'bed': '2',
        'bathroom': '1',
        'size': '688.120m²',
        'built': '2016',
        'listing_date': '03.05.2024',
        'type': 'Cottage',
        'description': 'Cozy cottage nestled in a quiet neighborhood.',
        'seller_name': 'John Smithy',
        'bed_icon': 'https://i.postimg.cc/vBj3YZW5/image-1.png',
        'bath_icon': 'https://i.postimg.cc/SQ2gZchd/image-2.png',
        'built_icon': 'https://i.postimg.cc/sgNB0GyP/image-3.png',
        'images': [
            "https://i.pinimg.com/736x/f6/65/48/f66548110843eda678d70692dd528dda.jpg",
            "https://example.com/image2.jpg",
            "https://example.com/image3.jpg"
        ],
    },
    {
        'id': 4,
        'street_name': 'Sólheimar',
        'house_num': '12B',
        'city': 'Hafnarfjörður',
        'postal_code': '220',
        'listing_price': '78.000.000 kr.',
        'is_sold': True,
        'seller_id': 1,
        'image': 'https://i.pinimg.com/736x/66/ab/bd/66abbdb2ab203c976da1a765761cc8f1.jpg',
        'bed': '3',
        'bathroom': '2',
        'size': '810.000m²',
        'built': '2019',
        'listing_date': '28.04.2024',
        'type': 'Semi-Detached',
        'description': 'Elegant semi-detached house with upgraded interiors.',
        'seller_name': 'John Smithy',
        'bed_icon': 'https://i.postimg.cc/vBj3YZW5/image-1.png',
        'bath_icon': 'https://i.postimg.cc/SQ2gZchd/image-2.png',
        'built_icon': 'https://i.postimg.cc/sgNB0GyP/image-3.png',
        'images': [
            "https://i.pinimg.com/736x/66/ab/bd/66abbdb2ab203c976da1a765761cc8f1.jpg",
            "https://example.com/image2.jpg",
            "https://example.com/image3.jpg"
        ],
    }
]

# property/views.py
def about(request):
    return render(request, 'property/about.html')

def contact(request):
    return render(request, 'property/contact.html')

def agencies(request):
    return render(request, 'property/agencies.html')



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

def auth_test(request):
    return render(request, 'property/auth_test.html', {
        'user': request.user,
        'authenticated': request.user.is_authenticated
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