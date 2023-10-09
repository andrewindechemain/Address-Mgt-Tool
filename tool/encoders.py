import json
from .models import Address,Customer

class CustomerEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Customer):
            return {"id": obj.id, "name": obj.name, "email": obj.email}
        return super().default(obj)
    
class AddressEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Address):
            return {'ip': obj.ip, 'customer': obj.customer, 'allocated': obj.allocated}
        return super().default(obj)