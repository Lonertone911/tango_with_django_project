from django.ruls import path
from rango import views

app_name = 'rango'

urlpatterns = [path(' ', views.about, name='about'),]
