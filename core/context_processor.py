from dashboard.models import SiteSettings

def site_settings(request):
    settings = SiteSettings.objects.first()
    
    if settings:
        return {
            'website_name': settings.website_name,
            'location': settings.location,
            'website_fav': settings.website_fav,
            'website_logo': settings.website_logo,
        }
    
    return {
        'website_name': '',
        'location': '',
        'website_fav': '',
        'website_logo': '',
    }


def site_metadata(request):
    return {
        'title_name': 'Resturnat Management Service', 
        'description': 'Quickly manage your resturnat service' 
    }


def cart_data(request):
    items = request.session.get('cart_items', []) 
    items_quantity = sum(item['quantity'] for item in items) if items else 0

    return {
        'items': items,
        'items_quantity': items_quantity
    }