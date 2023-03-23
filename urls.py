from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('MFA/', include(('MFA.urls', 'MFA'), namespace='MFA')),
]
