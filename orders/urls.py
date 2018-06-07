from django.conf.urls import url
from orders import views


urlpatterns = [
    url(r'^create/$', views.OrderCreateForm.as_view(), name='order_create'),
]
