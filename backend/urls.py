"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views.emailview import VerificationEmailView
from .views.productview import ProductList
from .views.typeview import ProductTypeList
from rest_framework.routers import DefaultRouter
from .views.userview import AuthUserViewSet
router = DefaultRouter()
router.register(r'auth-users', AuthUserViewSet)
urlpatterns = [
    path('send-verification-email/', VerificationEmailView.as_view(), name='send_verification_email'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/products/', ProductList.as_view(), name='product-list'),
    path('api/types/', ProductTypeList.as_view(), name='product-type-list'),  # New endpoint for product types

]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
