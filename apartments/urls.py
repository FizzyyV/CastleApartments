from django.urls import path

from . import views
urlpatterns = [

    # http://localhost:9000 (root)
    path('', views.index, name='apartments-index'),

    # http://localhost:9000/123 (id NUM)
    path('<int:id>', views.get_apartment_by_id, name='apartments-by-id'),
]