from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ №{}'.format(order.id)
    message = 'Уважаемый {}, \n\nВаш заказ №{} бы успешно создан.'.format(order.first_name,
                                                                          order.id)
    mail_sent = send_mail(subject,
                          message,
                          'crazyman2004@list.ru',
                          [order.email])
    return mail_sent
