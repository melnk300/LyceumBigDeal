import requests as rq

static_address = "http://static-maps.yandex.ru/1.x/"
geocode_address = "http://geocode.yandex.ru/1.x/"


def get_img(coords, z='14'):  # => coords = (lon - долгота lat - широта)
    res = rq.get("http://static-maps.yandex.ru/1.x/", {'ll': coords, 'z': z, 'l': 'map'})
    with open('map.png', 'wb+') as f:
        f.write(res.content)
    return res
