from django.http import HttpResponse
from django.template import loader


feature_1 = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [37.62, 55.793676]},
             "properties": {"title": "«Легенды Москвы",
                            "placeId": "moscow_legends",
                            "detailsUrl": "./static/places/moscow_legends.json"}}

feature_2 = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [37.64, 55.753676]},
             "properties": {"title": "Крыши24.рф",
                            "placeId": "roofs24",
                            "detailsUrl": "./static/places/roofs24.json"}}

features = [feature_1, feature_2]


def show_map(request):
    template = loader.get_template('index.html')
    context = {'places_geo': {"type": "FeatureCollection", "features": features}}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
