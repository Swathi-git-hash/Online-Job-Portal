from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from jobs.views import JobViewSet, ApplicationViewSet

router = DefaultRouter()
router.register('jobs', JobViewSet)
router.register('applications', ApplicationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]