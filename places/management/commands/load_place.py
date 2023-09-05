import os
import requests
from django.core.management.base import BaseCommand
from places.models import Location, Picture


class Command(BaseCommand):
    help = '''
    Command to upload locations from JSON files
    
    add JSON URL as positional argument
    '''

    def add_arguments(self, parser):
        parser.add_argument('download_url', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['download_url'])
        place_description = response.json()
        Location.objects.get_or_create(title=place_description['title'],
                                       description_short=place_description['description_short'],
                                       description_long=place_description['description_long'],
                                       lat=place_description['coordinates']['lat'],
                                       lng=place_description['coordinates']['lng']
                                       )
        place_images = place_description['imgs']
        place = Location.objects.get(title=place_description['title'])
        for image in place_images:
            image_name = image.split('/')[-1]
            os.makedirs('media', exist_ok=True)
            image_response = requests.get(image, stream=True)
            with open(f'media/{image_name}', 'wb') as image_file:
                for chunk in image_response.iter_content(chunk_size=512):
                    image_file.write(chunk)
            place.image.create(image=image_name)
