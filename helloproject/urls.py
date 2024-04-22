from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('helloapp.urls')),
    path('admin/', admin.site.urls),
    # path('school/', include('school.urls'))
]
