from os.path import exists

from django.shortcuts import render, redirect
from django.http import HttpResponse

from property.models import PurchaseOffer
from .forms import submit_offer_form
from .forms.finalize_offer_form import FinalizeOfferForm
from .forms.submit_offer_form import SubmitOfferForm
from .models import Property, PurchaseOffer, FinalizedOffer


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
        'bed_icon': 'https://i.postimg.cc/vBj3YZW5/image-1.png',
        'bath_icon': 'https://i.postimg.cc/SQ2gZchd/image-2.png',
        'built_icon': 'https://i.postimg.cc/sgNB0GyP/image-3.png'
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
        'bed_icon': 'https://i.postimg.cc/vBj3YZW5/image-1.png',
        'bath_icon': 'https://i.postimg.cc/SQ2gZchd/image-2.png',
        'built_icon': 'https://i.postimg.cc/sgNB0GyP/image-3.png'
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
        'bed_icon': 'https://i.postimg.cc/vBj3YZW5/image-1.png',
        'bath_icon': 'https://i.postimg.cc/SQ2gZchd/image-2.png',
        'built_icon': 'https://i.postimg.cc/sgNB0GyP/image-3.png'
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
        'bed_icon': 'https://i.postimg.cc/vBj3YZW5/image-1.png',
        'bath_icon': 'https://i.postimg.cc/SQ2gZchd/image-2.png',
        'built_icon': 'https://i.postimg.cc/sgNB0GyP/image-3.png'
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
        'image': 'https://i.pinimg.com/736x/66/ab/bd/66abbdb2ab203c976da1a765761cc8f1.jpg',  # replace with real image
        'bed': '3',
        'bathroom': '2',
        'size': '810.000m²',
        'built': '2019',
        'listing_date': '28.04.2024',
        'type': 'Semi-Detached',
        'description': 'Elegant semi-detached house with upgraded interiors.',
        'bed_icon': 'https://i.postimg.cc/vBj3YZW5/image-1.png',
        'bath_icon': 'https://i.postimg.cc/SQ2gZchd/image-2.png',
        'built_icon': 'https://i.postimg.cc/sgNB0GyP/image-3.png'
    }
]




def index(request):
     return render(request, template_name="property/properties.html", context={
         "properties": properties
     })

def get_property_by_id(request, property_id):
    property_to_get = next((x for x in properties if x ['id'] == property_id), None)
    if property_to_get is None:
        return HttpResponse("Property not found", status=404)

    user_offer = None
    #if user is logged in, check if there is submitted offer to display, else None
    if request.user.is_authenticated and hasattr(request.user, 'buyer'):
        user_offer = PurchaseOffer.objects.filter(
            user=request.user.buyer,
            property_id=property_to_get).order_by('-dateSubmitted').first()
    form = SubmitOfferForm()

    return render(request, template_name="property/property_detail.html",
                  context={"property": property_to_get ,
                           "user_offer": user_offer,
                           "form": form
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

### OFFER VIEWS ###

def submit_offer(request, property_id):
    """submit a purchase offer for available property
        calls helper function offer_exists to check for previous offers"""
    user = request.user
    if not user.is_authenticated or not hasattr(user, 'buyer'):
        return HttpResponse("User does not have permission to submit offers", status=403)

    try:
        property_to_get = Property.objects.get(id=property_id)
    except Property.DoesNotExist as e:
        return HttpResponse("Property not found", status=404)

    # if the property is sold, user cant make offer
    if property_to_get.propIsSold:
        return HttpResponse("Property is already sold", status=400)
        #TODO: make submit button grayed out if prop unavailable

    # if the user has submitted an offer previously, we ask if user wants to resubmit
    # call offer_exists() to check if offer exists for user id and property id
    prev_offer = offer_exists(user.id, property_id)
        #TODO: implement how to display previous offer

    if request.method == "POST":
        form = SubmitOfferForm(request.POST)
        if form.is_valid(): #if required fields are valid then create an instance of PurchaseOffer class
            offer = form.save(commit=False)
            offer.buyerId = user.buyer
            offer.sellerId = property_to_get.sellerId
            offer.propertyId = property_to_get
            offer.offerStatus = 'Pending'
            #offer= form.save(commit=True)
            return redirect('property-by-id', property_id= property_id)
    else:
        form = SubmitOfferForm()

    return render(request, template_name="property/property_detail.html",
                  context={'property': property_to_get,
                           'previous_offer': prev_offer,
                           'form': form
                })
    #TODO: create template for purchase offer

def offer_exists(user_id, property_id)-> PurchaseOffer | None:
    """finds previously submitted offer by user for some property"""
    #check if offer(s) with user_id exists and has property_id
    prev_offer = PurchaseOffer.objects.filter(
        buyerId__user__id = user_id,
        propertyId__id = property_id
    ).order_by('-dateSubmitted').first()
    #if offer exists, return offer id
    return prev_offer if prev_offer else None


def finalize_purchase_offer(request, property_id, offer_id):
    """finalize an accepted purchase offer"""
    try: #check if offer exists
        offer = PurchaseOffer.objects.get(id=offer_id, propertyId__id=property_id)
    except PurchaseOffer.DoesNotExist:
        return HttpResponse("Offer not found", status=404)

    if offer.offerStatus != 'Accepted': #if offer is not accepted it cannot be finalized
        return HttpResponse("Offer must be accepted to finalize", status=400)

    if request.method == "POST":
        form = FinalizeOfferForm(request.POST)
        if form.is_valid():
            finalize_offer = form.save(commit=False)
            finalize_offer.offerId = offer
            finalize_offer.propertyId = property_id
            #finalized_offer.save()
            return redirect('property-by-id', property_id=property_id)
    else:
        form = FinalizeOfferForm()

    return render(request, template_name="property/property_detail.html",
                  context={'property': property_id,
                            'form': form,
                            'offer': offer
                         })

def get_contact_info_finalize(finalized_offer_obj):
    """helper function for finalizing offer
        stores contact info for buyer"""
    pass
    #address is saved as an Address class instance
    national_id = input("Your National ID...")
    phone_number = input("Your Phone Number...")

    #create variables to store each field,


def get_payment_method_finalize(finalized_offer_obj):
    """helper function for finalizing offer
    stores payment method info for buyer"""
    pass
    match FinalizedOffer.paymentMethod:
        case 'Credit Card':
            cardholder_name = input("Cardholder name")
            card_number = input("Card number")
            card_expiration_date = input("E.X. date")
            card_cvc = input("CVC")
            finalized_offer_obj

        case 'Bank Transfer':
            pass
