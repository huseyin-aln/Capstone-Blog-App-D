from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryView,
    BlogView,
    comment_list, 
    like

    # CommentView,
    # LikeView
    # PostVView,
)


router = routers.DefaultRouter()

router.register('blog', BlogView)
router.register('category', CategoryView)

# router.register('comment', CommentView)
# router.register('like', LikeView)
# router.register('postview', PostVView)


urlpatterns = [
    path("", include(router.urls)),
    path("likes/<int:pk>/", like, name="like"),
    path("comments/<int:pk>/", comment_list, name="comment_list"),
] 

# urlpatterns += router.urls
