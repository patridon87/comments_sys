from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CreateRetrievePostViewSet, CreateListCommentViewSet,
                    RertrieveCommentVewSet)

router_v1 = SimpleRouter()

router_v1.register(r'comments', RertrieveCommentVewSet, basename='comments')
router_v1.register(r'posts', CreateRetrievePostViewSet, basename='posts')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CreateListCommentViewSet,
                   basename='create_comment')

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
