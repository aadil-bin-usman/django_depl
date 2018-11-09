from django.urls import path
from first_app.views import index,signup

app_name = 'first_app'
urlpatterns = [
    # path('', index, name='index'),
    path(r'login', signup, name='sign_up')

]


