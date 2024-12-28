from django.shortcuts import render

def services_view(request):
    return render(request, 'services/services.html')

def design_service_view(request):
    return render(request, 'services/design_service.html')

def logo_design_view(request):
    return render(request, 'services/logo_design.html')

def poster_design_view(request):
    return render(request, 'services/poster_design.html')

def social_media_design_view(request):
    return render(request, 'services/social_media_design.html')

def contact_view(request):
    if request.method == 'POST':
        # Process the contact form (e.g., send an email or save the data)
        return render(request, 'services/contact_success.html')
    return render(request, 'services/contact.html')

