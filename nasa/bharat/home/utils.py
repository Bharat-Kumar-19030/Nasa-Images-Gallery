# bharat/utils.py
import requests
from django.conf import settings

def get_apod():
    api_key = settings.NASA_API_KEY
    base_url = 'https://api.nasa.gov/planetary/apod'
    user_date = settings.USER_DATE
    
    params = {
        'api_key': api_key,
        'date':  user_date,
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    return {
        'title': data['title'],
        'url': data['url'],
        'explanation': data['explanation'],
    }

# bharat/utils.py

from datetime import datetime, timedelta

def get_epic_image():
    api_key = settings.NASA_API_KEY
    base_url = 'https://epic.gsfc.nasa.gov/api/natural'

    # Get yesterday's date
    date_yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    params = {
        'api_key': api_key,
        'date': date_yesterday,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        if data:
            image_data = data[0]
            image_date = image_data['date']
            image_name = image_data['image']
            image_date= image_date[0:10]
            image_url = f'https://epic.gsfc.nasa.gov/archive/natural/{image_date.replace("-", "/")}/png/{image_name}.png'

            return {
                'date': image_date,
                'image': image_url,
                #'explanation': image_data['explanation'],
            }
        else:
            return None

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None

    except requests.exceptions.RequestException as req_err:
        print(f'Request error occurred: {req_err}')
        return None
def get_mars_rover_photos():
    api_key = settings.NASA_API_KEY
    base_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000'
    params = {
        'api_key': api_key,
    }
    rover_photos_data = []
    response=requests.get(base_url,params=params)
    data=response.json()

    photos=data.get('photos',[])
    for photo in photos:
        rover_photos_data.append({'img_src': photo['img_src'],'Camera': photo['camera']['full_name'], 'Earth_Date' : photo['earth_date']})


    return rover_photos_data



