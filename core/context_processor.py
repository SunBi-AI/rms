from dashboard.models import SiteSettings

def site_settings(request):
    settings = SiteSettings.objects.first()  # Get the first SiteSettings object (or handle as needed)
    
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
