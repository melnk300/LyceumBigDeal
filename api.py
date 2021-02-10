import requests as rq

static_address = "http://static-maps.yandex.ru/1.x/"
geocode_address = "http://geocode.yandex.ru/1.x/"
spn = 0.05


def get_img(coords, spn='0.01,0.01'):  # => coords = (lon - долгота lat - широта)
    res = rq.get("http://static-maps.yandex.ru/1.x/", {'ll': coords, 'spn': spn, 'l': 'map'})
    with open('map.png', 'wb') as f:
        f.write(res.content)
    return res