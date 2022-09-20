from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from bugs.views import BugDetailView, BugCreateView, BugsListView, \
    ResolvedBugsListView, CommentDetailView, CommentsListView, CommentCreateView

router = DefaultRouter()
router.register(r'product', BugDetailView, basename='Product')
# router.register(r'image', ImageViewSet, basename='Image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('bug/<int:id>/', BugDetailView.as_view(), name='bug-retrive-update-delete'),
    path('bug/create/', BugCreateView.as_view(), name='bug-create'),
    path('buglist/', BugsListView.as_view(), name='bugs-list'),
    path('bug/list/resolved/', ResolvedBugsListView.as_view(), name='bugs-resolved-list'),


    path('comment/<int:id>/', CommentDetailView.as_view(), name='comment-retrive-update-delete'),
    path('comment/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/list/', CommentsListView.as_view(), name='comment-list'),
    # path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
