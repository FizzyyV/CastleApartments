from django.urls import path

from . import views
urlpatterns = [

    # http://localhost:9000 (root)
    path('', views.index, name='property-index'),

    # http://localhost:9000/123 (id NUM)
    path('<int:property_id>/', views.get_property_by_id, name='property-by-id'),

    path('auth-test/', views.auth_test, name='auth-test'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('agencies/', views.agencies, name='agencies'),

]