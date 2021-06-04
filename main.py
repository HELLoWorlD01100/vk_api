import json
from urllib.request import urlopen
import config


def get_user(id_or_name):
    user = get_json(make_request('users.get', f'user_ids={id_or_name}'))
    return user


def get_user_information(user, field):
    return user['response'][0][field]


def get_user_id(user):
    return get_user_information(user, 'id')


def get_user_first_name(user):
    return get_user_information(user, 'first_name')


def get_user_lastname(user):
    return get_user_information(user, 'last_name')


def make_request(method, fields):
    return f'https://api.vk.com/method/{method}?{fields}&v={config.VERSION}&access_token={config.ACCESS_TOKEN}'


def get_friends(user_id):
    return get_json(make_request('photos.getAlbums', 'user_id={}'.format(user_id)))


def get_json(request):
    with urlopen(request) as url:
        j = json.loads(url.read())
    return j


def get_user_albums(user_id):
    result = []
    albums_info = get_json(make_request('photos.getAlbums', 'user_id={}'.format(user_id)))

    response = albums_info['response']
    count = response['count']

    if count == 0:
        return result
    items = response['items']


    for item in items:
        result.append(item['title'])
    return result


def print_list(list):
    for i in range(1, len(list) + 1):
        print(f'{i}. {list[i-1]}')


if __name__ == '__main__':
    print('Введите id или username(из ссылки)')
    user_name_or_id = input()
    user = get_user(user_name_or_id)
    id = get_user_id(user)
    name = get_user_first_name(user)
    lastname = get_user_lastname(user)
    albums_names = get_user_albums(id)
    if (len(albums_names)) == 0:
        print(f'Пользователь {name} {lastname} не создавал альбомов.')
    else:
        print(f'Список альбомов, созданных пользователем {name} {lastname}:')
        print_list(albums_names)
