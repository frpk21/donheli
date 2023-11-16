from django.urls import include, path

from generales import views

from django.contrib.auth import views as auth_views

from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.HomeView, name='home'),
    path('noticias/seccion/<int:pk>', views.SeccionView, name="seccion"),
    path('noticias/subseccion/<int:pk>', views.SubSeccionView, name="subseccion"),
    path('noticia/<slug>', views.DetalleView, name="detalle"),
    path('contacto', views.ContactView.as_view(), name="contact"),
    path('videolive', views.VideoLiveView.as_view(), name="envivo"),
    path('update/', views.ajax_update, name='upd'),
    #url(r'^post/(?P<slug>[^/]+)', views.post, name='post'),
    #path('login/', auth_views.LoginView.as_view(template_name='generales/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='generales/login.html'), name='logout'),
    #path('sin_privilegios/', HomeSinPrivilegios.as_view(), name='sin_privilegios'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 