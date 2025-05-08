from django.urls import path

from . import views
urlpatterns = [

    # http://localhost:9000 (root)
    path('', views.index, name='property-index'),

    # http://localhost:9000/123 (id NUM)
    path('<int:property_id>/', views.get_property_by_id, name='property-by-id'),

    path('<int:property_id>/submit_offer', views.submit_offer, name='property-submit-offer'),
]