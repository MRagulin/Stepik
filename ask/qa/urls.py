from django.conf.urls import url
from . import views


urlpatterns = [
   # path('admin/', admin.site.urls),
   url('login/', views.test),
   url('signup/', views.test),
   url(r'^(question/)\d+/$', views.test),
   url(r'ask/', views.test),
   url(r'popular/', views.test),
   url(r'new/', views.test),
   url(r'^$', views.test)
]

