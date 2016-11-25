from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.OrderCreateForm.as_view(), name='order_create'),
]
