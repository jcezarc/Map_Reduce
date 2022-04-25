import os
import requests

URL_PREFIX = 'https://api.mapbox.com/geocoding/v5/mapbox.places'
URL_COUNTRY = 'country=br&language=pt'


class Mapbox:
    def __init__(self, access_token=None):
        self.access_token = access_token or os.getenv('MAPBOX_ACCESS_TOKEN')
        self.base_url = {
            'address': '{prefix}/{endereco}.json?{country}&access_token={token}',
            'geocoord': "{prefix}/{lat},{long}.json?{country}&access_token={token}"
        }

    def get_coordinates(self, address: str) -> list[float]:
        url = self.base_url['address'].format(
            prefix=URL_PREFIX, country=URL_COUNTRY,
            token=self.access_token, endereco=address
        )
        data = requests.get(url).json()['features']
        return next(iter(data), {}).get('center')

    def get_address(self, lat: float, long: float) -> str:
        url = self.base_url['geocoord'].format(
            prefix=URL_PREFIX, country=URL_COUNTRY,
            token=self.access_token, lat=lat, long=long
        )
        data = requests.get(url).json()['features']
        return next(iter(data), {}).get('place_name')
