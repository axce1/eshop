from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_PROCESSED, ST_PP_PENDING  # noqa: F401
from paypal.standard.ipn.signals import valid_ipn_received

from orders.models import Order


def handler_payment(sender, **kwargs):
    ipn_obj = sender
    # if ipn_obj.payment_status == ST_PP_PROCESSED:
    if ipn_obj.payment_status == ST_PP_PENDING:
        order = get_object_or_404(Order, id=ipn_obj.invoice)
        order.paid = True
        order.save()


valid_ipn_received.connect(handler_payment)
