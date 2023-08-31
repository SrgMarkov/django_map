from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Location

features = []
locations = Location.objects.all()
for location in locations:
    feature = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [location.lng, location.lat]},
               "properties": {"title": location.title,
                              "placeId": location.id,
                              "detailsUrl": f"./static/places/{location.id}.json"}}
    features.append(feature)


def show_location_properties(request, location_id):
    template = get_object_or_404(Location, id=location_id)
    return HttpResponse(template.title)


def show_map(request):
    template = loader.get_template('index.html')
    context = {'places_geo': {"type": "FeatureCollection", "features": features}}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
