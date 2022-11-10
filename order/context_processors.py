from django.conf import settings 

def get_current_currency(req):
    if 'admin' in req.path:
        return {}
    else:
        return {'CURRENT_CURRENCY' :settings.CURRENCY, 'CURRENCIES': settings.CURRENCIES}