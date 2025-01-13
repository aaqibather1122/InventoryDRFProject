from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from sendgrid import Mail, SendGridAPIClient

from inventoryDetails.models import InventoryDetail


@receiver(post_save,sender=InventoryDetail)
def check_stock_and_notify(sender,instance,**kwargs):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa out side if condition")
    if instance.quantity_in_stock <= instance.minimum_stock_level:
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa in side if condition")
        send_low_stock_email(instance)

def send_low_stock_email(inventory_detail):
    subject = f"Low Stock Alert: {inventory_detail.product.name}"
    message = (
        f"Dear Admin,\n\n"
        f"The stock of product '{inventory_detail.product.name}' has fallen below the minimum stock level.\n"
        f"Current stock: {inventory_detail.quantity_in_stock}\n"
        f"Minimum stock level: {inventory_detail.minimum_stock_level}\n"
        f"Please reorder {inventory_detail.reorder_quantity} units of this product.\n\n"
        f"Thank you."
    )
    email = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=settings.ADMIN_EMAIL,
        subject=subject,
        plain_text_content=message,
    )
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(email)
        if response.status_code == 202:
            print("Low stock email sent successfully.")
        else:
            print(f"Failed to send email. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")