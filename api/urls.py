from django.urls import path, include



from api import views
from geckos.views import species_details, gecko_list
from posts.views import PostList, PostDetail
from rest_framework import routers, serializers, viewsets

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'geckos', views.GeckoViewSet)
router.register(r'posts', views.PostListViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('GeckoList/', gecko_list, name='gecko_list'),
    path('geckos/<int:pk>', species_details, name='species_details'),
    path('PostList/', PostList.as_view(), name='post_list'),
    path('blog/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('api-auth/', include('rest_framework.urls')),
]
