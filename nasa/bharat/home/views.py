from django.shortcuts import render,HttpResponse
from django.conf import settings
from datetime import datetime

# Create your views here.
#def index(request):
    #return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def contact(request):
    return render(request,"contact.html")
# bharat/views.py
from .utils import get_apod
from .utils import get_epic_image
from .utils import get_mars_rover_photos
def index(request):
    apod_data = get_apod()
    user_date = None

    if request.method == 'POST':
        user_date = request.POST.get('user_date', '')
        # Validate and store the user date in settings
        if user_date:
            settings.USER_DATE = user_date
        if not user_date:
            user_date = datetime.now().strftime('%Y-%m-%d')
    
    epic_data = get_epic_image()
    rover_photos_data=get_mars_rover_photos
    return render(request, 'index.html', {'apod_data': apod_data, 'user_date': user_date ,'epic_data': epic_data ,'rover_photos_data': rover_photos_data})
    


