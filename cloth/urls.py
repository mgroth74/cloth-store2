from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product/create', views.product_create, name='product_create')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
## To display the images from static/ media folder
