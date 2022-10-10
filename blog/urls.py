from django.urls import path
from rest_framework import routers
from .views import (
    CategoryView,
    CommentView,
    LikeView,
    PostView,
    PostVView,
)


router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('post', PostView)
router.register('comment', CommentView)
router.register('like', LikeView)
router.register('postview', PostVView)


urlpatterns = [
    
] 

urlpatterns += router.urls
