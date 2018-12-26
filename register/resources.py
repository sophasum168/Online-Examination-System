from import_export import resources
from .models import Register

class RegisterResource(resources.ModelResource):
    class Meta:
        model = Register