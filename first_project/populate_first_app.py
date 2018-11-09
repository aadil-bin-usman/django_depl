import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')


import django
django.setup()

import random
from first_app.models import User
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']


def add_topic():
    t = User.objects.get_or_create(user_name=random.choice(topics))
    print(t)
    t.save()
    return t

def populate(N=5):

    for entry in range(N):


        fake_name=fakegen.company()

        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating scrip!")
    # populate(20)
    print("PO comp")
    topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']
    t = User.objects.get_or_create(user_name=random.choice(topics))
    print(t)







