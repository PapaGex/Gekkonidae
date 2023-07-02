from rest_framework import viewsets, permissions

from rest_framework.response import Response
from rest_framework.decorators import api_view
from geckos.models import Gecko
from geckos.serializers import GeckoSerializer

from posts.models import Post
from posts.serializers import PostSerializer

@api_view()
def gecko_list(request):
    def gecko_list(request):
        geckos = Gecko.objects.all()
        serializer = GeckoSerializer(geckos, many=True)
        data = {
            'geckos': list(geckos.values())
        }
        return Response(serializer.data)

@api_view()
def species_details(request, pk):
    gecko = Gecko.objects.get(pk=pk)
    serializer = GeckoSerializer(gecko)
    data = {
        'name': gecko.name,
        'genus': gecko.genus,
        'species': gecko.species,
        'description': gecko.description,
        'discovered': gecko.discovered,
        'habitat': gecko.habitat,
        'snout_to_vent': gecko.snout_to_vent,
        'lifespan': gecko.lifespan,
        'species_range': gecko.species_range,
    }
    return Response(serializer.data)

class GeckoListViewSet(viewsets.ModelViewSet):
    queryset = Gecko.objects.all()
    serializer_class = GeckoSerializer

class GeckoViewSet(viewsets.ModelViewSet):
    queryset = Gecko.objects.all()
    serializer_class = GeckoSerializer

class PostListViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
