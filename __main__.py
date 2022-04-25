import json
from mapbox import Mapbox

def pessoas_que_moram_juntas() -> dict:
    mapbox = Mapbox()
    locais = {}
    with open('map_reduce/dados.json', encoding='utf-8') as f:
        for pessoa in json.load(f):
            if 'endereço' in pessoa:
                coord = mapbox.get_coordinates(pessoa['endereço'])
                pessoa['coordenadas'] = coord
            else:
                coord = pessoa['coordenadas']
                pessoa['endereço'] = mapbox.get_address(*coord)
            locais.setdefault(str(coord), []).append(pessoa)
    return locais


print('PESSOAS QUE MORAM JUNTAS:'.center(50, '='))
for casa in pessoas_que_moram_juntas().values():
    for pessoa in casa:
        print('{}\n\tmora em {}'.format(
            pessoa['nome'], pessoa['endereço']
        ))
    print('-' * 50)
