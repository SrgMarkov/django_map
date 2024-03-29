from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Location


def get_features(request) -> dict:
    features = [{"type": "Feature", "geometry": {
                 "type": "Point",
                 "coordinates": [location.lng, location.lat]},
                 "properties": {"title": location.title,
                                "placeId": location.id,
                                "detailsUrl": reverse('places',
                                                      args=(location.id,))}}
                for location in Location.objects.all()]
    return {"type": "FeatureCollection", "features": features}


def show_location_properties(request, location_id):
    location = get_object_or_404(Location.objects.prefetch_related('images'),
                                 id=location_id)

    location_images = [image.image.url for image in location.images.all()]
    location_description = {"title": location.title,
                            "imgs": location_images,
                            "short_description": location.short_description,
                            "long_description": location.long_description,
                            "coordinates": {
                                "lng": location.lng,
                                "lat": location.lat
                            }}
    return JsonResponse(location_description, safe=False,
                        json_dumps_params={'ensure_ascii': False, 'indent': 1})


def show_map(request):
    context = {'places_geo': get_features(request)}
    return render(request, 'index.html', context=context)
