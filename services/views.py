from django.shortcuts import render

def services_view(request):
    return render(request, 'services/services.html')

def design_service_view(request):
    return render(request, 'services/design_service.html')

