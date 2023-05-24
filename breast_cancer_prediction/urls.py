
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('breast_cancer_prediction_app.urls')),
    path('admin/', admin.site.urls),
]
