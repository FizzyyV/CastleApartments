from os.path import exists

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from property.models import PurchaseOffer
from .forms import submit_offer_form
from .forms.finalize_offer_form import FinalizeOfferForm
from .forms.submit_offer_form import SubmitOfferForm
from .models import Property, Address, PurchaseOffer, FinalizedOffer, PropertyImages


from django.contrib.sessions.models import Session

def session_debug(request):
    sessions = Session.objects.all()
    return render(request, 'session_debug.html', {'sessions': sessions})


# Create your views here.


# property/views.py
def about(request):
    return render(request, 'property/about.html')

def contact(request):
    return render(request, 'property/contact.html')

def agencies(request):
    return render(request, 'property/agencies.html')

def index(request):
    order_by_has_value = True
    order_by = request.GET.get("order_filter","")
    
    #If there is no specified value then we will order by name
    if order_by == "":
        order_by = "propertyName"
        order_by_has_value = False
    
    #high base price incase no value gets sent
    low_value = 0
    high_value = 99999999999999999999999999999999
    pricerange = request.GET.get("price_filter", "")
    if pricerange != "":
        #try is there to keep the request running incase there is a bad/incorrect value sent
        try:
            low_value,high_value = pricerange.split("-")
            low_value = int(low_value)
            high_value = int(high_value)
        except:
            pass

    if 'street_filter' in request.GET or "postal_filter" in request.GET or "type_filter" in request.GET or "price_filter" in request.GET:
        return JsonResponse({
            'data': [{
                'id': x.id,
                'propertyName': x.propertyName,
                'propDescription': x.propDescription,
                'propertyType': x.propertyType,
                'propListingPrice': x.propListingPrice,
                'propListingDate': x.propListingDate,
                'propIsSold': x.propIsSold,
                'propBedrooms': x.propBedrooms,
                'propBathrooms': x.propBathrooms,
                'propSquareMeters': x.propSquareMeters,
                'propAddress_id': x.propAddress_id,
                'built': x.built,
                'house_number': Address.objects.get(id=x.propAddress_id).house_number,
                'city': Address.objects.get(id=x.propAddress_id).city,
                'postal_code': Address.objects.get(id=x.propAddress_id).postal_code,
                'propThumbnail': str(x.propThumbnail)
            } for x in Property.objects.filter(propertyName__icontains=request.GET['street_filter'],
                                               propertyType__icontains=request.GET['type_filter'],
                                               propListingPrice__lte=high_value,
                                               propListingPrice__gte=low_value,
                                               postalCode__icontains=request.GET['postal_filter'],
                                               ).order_by(order_by)]
        })
    elif order_by_has_value:
        return JsonResponse({
            'data': [{
                'id': x.id,
                'propertyName': x.propertyName,
                'propDescription': x.propDescription,
                'propertyType': x.propertyType,
                'propListingPrice': x.propListingPrice,
                'propListingDate': x.propListingDate,
                'propIsSold': x.propIsSold,
                'propBedrooms': x.propBedrooms,
                'propBathrooms': x.propBathrooms,
                'propSquareMeters': x.propSquareMeters,
                'propAddress_id': x.propAddress_id,
                'built': x.built,
                'house_number': Address.objects.get(id=x.propAddress_id).house_number,
                'city': Address.objects.get(id=x.propAddress_id).city,
                'postal_code': Address.objects.get(id=x.propAddress_id).postal_code,
            } for x in Property.objects.filter().order_by(order_by)]
        })

    properties = Property.objects.all()

    addprop = []
    for property in properties:
        address = Address.objects.get(id=property.propAddress_id)
        addprop.append({property,address})


    return render(request, template_name="property/properties.html", context={
         "properties": addprop
    })

def get_property_by_id(request, property_id):
    property = Property.objects.get(id=property_id)
    address = Address.objects.get(id=property.propAddress_id)
    seller = property.sellerId
    user_offer = None
    #if user is logged in, check if there is submitted offer to display, else None
    if request.user.is_authenticated and hasattr(request.user, 'buyer'):
        user_offer = PurchaseOffer.objects.filter(
            buyerId=request.user.buyer,
            propertyId__id=property_id).order_by('-dateSubmitted').first()

    if request.method == "POST":
        form = SubmitOfferForm(request.POST)
        if form.is_valid(): #if required fields are valid then create an instance of PurchaseOffer class
            offer = form.save(commit=False)
            offer.buyerId = request.user.buyer
            offer.sellerId = property.sellerId
            offer.propertyId = property
            offer.save()
            return redirect('property-by-id', property_id= property_id)
    else:
        form = SubmitOfferForm()

    return render(request, template_name="property/property_detail.html", context={
        "property": property,
        "address": address,
        "previous_offer": user_offer,
        "form": form,
        "seller": seller,
    })

def auth_test(request):
    return render(request, 'property/auth_test.html', {
        'user': request.user,
        'authenticated': request.user.is_authenticated
    })


