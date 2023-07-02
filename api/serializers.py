from rest_framework import serializers

from geckos.models import Gecko
from posts.models import Post


class GeckoSerializer(serializers.Serializer):

            id = serializers.IntegerField(read_only=True)
            name = serializers.CharField()
            genus = serializers.CharField()
            species = serializers.CharField()
            locale_subspecies = serializers.CharField()
            discovered = serializers.CharField()
            description = serializers.TextField()
            habitat = serializers.CharField()
            snout_to_vent = serializers.IntegerField()
            lifespan = serializers.IntegerField()
            species_range = serializers.CharField()

class PostSerializer(serializers.Serializer):

            id = serializers.IntegerField(read_only=True)
            author = serializers.CharField()
            title = serializers.CharField()
            body = serializers.TextField()

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']