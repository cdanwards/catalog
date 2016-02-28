from django.conf.urls import url, patterns
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.course_list, name = 'course_list'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.course_detail, name='course_detail'),
    url(r'^add/$', views.course_new, name='course_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.course_edit, name='course_edit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
