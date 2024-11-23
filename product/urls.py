
from django.urls import path

from  .views import *

urlpatterns = [

    path('', ShowHome, name='ShowHome'),
    path('Contact/', Contact, name='Contact'),
    path('About/', About, name='About'),
    path('create/', create, name='create'),
    path('Events/', Events, name='Events'),
    path('Highlight Videos/', Highlight, name='Highlight Videos'),
    path('Learn/', Learn, name='Learn'),
    path('Register/', Register, name='Register'),
    path('Services/', Services, name='Services'),




]