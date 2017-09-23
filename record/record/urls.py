from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers

from diary.views import DiaryViewSet
from post.views import PostViewSet, PhotoViewSet
from record import settings
from user.views import UserViewSet, emailcertification

router = routers.DefaultRouter()
router.register(
    r'users',
    UserViewSet
)
router.register(
    r'diary',
    DiaryViewSet
)
router.register(
    r'post',
    PostViewSet
)
router.register(
    r'photo',
    PhotoViewSet
)

urlpatterns = \
    [
        url(r'^admin/', admin.site.urls),
        url(r'^user/', include('user.urls')),
        url(r'^api/', include(router.urls, namespace='api')),
        url(r'^rest-auth/', include('rest_auth.urls')),
        url(r'^auth/$', emailcertification)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
