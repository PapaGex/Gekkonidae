from rest_framework import serializers

from .models import Gecko


class GeckoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gecko
        fields = (
            "id",
            "name",
            "genus",
            "species",
            "locale_subspecies",
            "discovered",
            "description",
            "habitat",
            "snout_to_vent",
            "lifespan",
            "species_range",
        )