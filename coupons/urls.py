from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^apply/$', views.CouponApplyView.as_view(), name='apply'),
]