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
            key = '-'.join(str(c) for c in coord)
            locais.setdefault(key, []).append(pessoa)
    return locais


print('PESSOAS QUE MORAM JUNTAS:'.center(50, '='))
for mesma_casa in pessoas_que_moram_juntas().values():
    for pessoa in mesma_casa:
        print(f'{pessoa["nome"]}\n\tmora em {pessoa["endereço"]}')
    print('-' * 50)
