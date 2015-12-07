from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^update_profile$', views.update_profile, name='update_profile'),

                       )