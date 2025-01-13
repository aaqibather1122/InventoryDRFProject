from django.apps import AppConfig


class InventoryDetailsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventoryDetails'

    def ready(self):
        import inventoryDetails.signals