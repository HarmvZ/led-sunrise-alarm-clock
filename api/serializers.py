from rest_framework import serializers

class ColorSerializer(serializers.Serializer):
    r = serializers.IntegerField(min_value=0, max_value=255)
    g = serializers.IntegerField(min_value=0, max_value=255)
    b = serializers.IntegerField(min_value=0, max_value=255)
    rgb = serializers.SerializerMethodField()
    
    def get_rgb(self, obj):
        """
        Returns a tuple of (r, g, b) color values.
        """
        r = obj.get('r', 0)
        g = obj.get('g', 0)
        b = obj.get('b', 0)
        return (r, g, b)