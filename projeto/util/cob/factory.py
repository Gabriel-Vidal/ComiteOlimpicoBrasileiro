
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')


def make_eventos():
    return{
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=3),
        'decription': fake.sentence(nb_words=12),
        'event_time': fake.random_number(digits=2, fix_len=True),
        'event_time_unit': 'Horas',
        'distance': fake.random_number(digits=2, fix_len=True),
        'distance_unit': 'Metros',
        'event_location': '<i class="fas fa-map-marked-alt"></i>',
        'created_at': fake.date_time(),
        'part': {
            'name': fake.name(),
            'age': fake.random_number(digits=2, fix_len=True),
            'weight': fake.random_number(digits=2, fix_len=True),
            'height': fake.random_number(digits=2, fix_len=True),
        },
        'category': {
            'cat_name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/sports' % rand_ratio()
        },
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_eventos())
