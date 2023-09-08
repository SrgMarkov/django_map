import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Location


class Command(BaseCommand):
    help = '''
    Command to upload locations from JSON files
    add JSON URL as positional argument
    '''

    def add_arguments(self, parser):
        parser.add_argument('download_url', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['download_url'])
        response.raise_for_status()
        place_description = response.json()
        place, create = Location.objects.\
            get_or_create(title=place_description['title'],
                          defaults={
                          'short_description':
                              place_description['description_short'],
                          'long_description':
                              place_description['description_long'],
                          'lat': place_description['coordinates']['lat'],
                          'lng': place_description['coordinates']['lng']})
        if create:
            for image in place_description['imgs']:
                image_name = image.split('/')[-1]
                image_response = requests.get(image)
                image_response.raise_for_status()
                place.images.create(image=ContentFile(image_response.content,
                                                      name=image_name))
