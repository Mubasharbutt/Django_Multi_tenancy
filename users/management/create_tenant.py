from django.core.management.base import BaseCommand
from users.models import Business, Domain

class Command(BaseCommand):
    help = 'Create a new tenant'

    def handle(self, *args, **kwargs):
        # Create a tenant (business)
        tenant = Business(schema_name='mytenant', name='My Tenant Business')
        tenant.save()

        # Create a domain for the tenant
        domain = Domain(domain='mytenant.local', tenant=tenant)
        domain.save()

        self.stdout.write(self.style.SUCCESS(f'Tenant and domain created successfully!'))
