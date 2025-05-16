from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render, redirect

import property.forms.finalize_offer_form
from account.forms.profile_form import CustomUserCreationForm, ProfileForm
from account.models import Buyer, Profile, Seller
from django.core.exceptions import ObjectDoesNotExist

from property.models import PurchaseOffer, FinalizedOffer


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"user: {user}, id: {user.id}")

            if user.role == 'buyer':
                Buyer.objects.create(user=user)
            elif user.role == 'seller':
                pass  # Optional: Create Seller.objects.create(user=user)
            Profile.objects.create(user=user, profile_image='')  # Use default image or logic


            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'account/signup.html', {'form': form})

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('property-index')  # Or whatever page you want
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login_pretty.html', {'form': form})


def profile(request):
    account_profile = Profile.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=account_profile)

    offers = []
    if request.user.is_authenticated and hasattr(request.user, 'buyer'):
        #get the latest offers submitted for each property
        latest_offer_ids = (
            PurchaseOffer.objects
            .filter(buyerId=request.user.buyer)
            .values('propertyId')
            .annotate(latest_id=Max('id'))
            .values_list('latest_id', flat=True)
        )
        offers = PurchaseOffer.objects.filter(id__in=latest_offer_ids).select_related('propertyId')
    all_offers = PurchaseOffer.objects.filter(buyerId=request.user.buyer).select_related('propertyId')
    finalized_offer_ids = set(FinalizedOffer.objects.filter(offerId__in=offers).values_list('offerId', flat=True))
    finalized_success = request.GET.get('finalized', None)=='1'
    return render(request, 'account/profile.html', {
            'form':form,
            'offers':offers,
            'finalized_offer_ids':finalized_offer_ids,
            'finalize_form':property.forms.finalize_offer_form.FinalizeOfferForm()

        })

def finalize_purchase_offer(request, offer_id):
    """finalize an accepted purchase offer"""
    try: #check if offer exists
        offer = PurchaseOffer.objects.get(id=offer_id, buyerId=request.user.buyer)
    except PurchaseOffer.DoesNotExist:
        return HttpResponse("Offer not found", status=404)

    if offer.offerStatus != 'Accepted': #if offer is not accepted it cannot be finalized
        return HttpResponse("Offer must be accepted to finalize", status=400)

    # Check if already finalized
    existing_finalized = getattr(offer, 'finalizedoffer', None)  # OneToOne relation
    if existing_finalized:
        return HttpResponse("Offer already finalized", status=400)

    if request.method == "POST":
        form = property.forms.finalize_offer_form.FinalizeOfferForm(request.POST)
        if form.is_valid():
            finalize_offer = form.save(commit=False)
            finalize_offer.offerId = offer
            finalize_offer.propertyId = offer.propertyId
            finalize_offer.save()
            finalize_offer.propertyId.propIsSold = True
            return redirect('/accounts/profile/?finalized=1')
    else:
        form = property.forms.finalize_offer_form.FinalizeOfferForm()

    return render(request, template_name="account/profile.html",
                  context={'form': form,
                            'offer': offer
                         })

def seller_profile(request, seller_id):
    seller = Seller.objects.get(id=seller_id)
    properties = property.models.Property.objects.filter(sellerId=seller)

    return render(request, template_name="account/seller_profile.html",context={
        'seller': seller,
        'properties':properties
    })