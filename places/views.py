from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from .models import Location


def get_features() -> dict:
    features = []
    for location in Location.objects.all():
        feature = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [location.lng, location.lat]},
                   "properties": {"title": location.title,
                                  "placeId": location.id,
                                  "detailsUrl": f"places/{location.id}"}}
        features.append(feature)
    return {"type": "FeatureCollection", "features": features}


def show_location_properties(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    location_images = [image.image.url for image in location.images.all()]
    location_description = {"title": location.title,
                            "imgs": location_images,
                            "short_description": location.short_description,
                            "long_description": location.long_description,
                            "coordinates": {
                                "lng": location.lng,
                                "lat": location.lat
                            }}
    return JsonResponse(location_description, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 1})


def show_map(request):
    template = loader.get_template('index.html')
    context = {'places_geo': get_features()}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
