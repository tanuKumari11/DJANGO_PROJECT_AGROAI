from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def ocean_data_dashboard(request):
    return render(request, 'data/dashboard.html')