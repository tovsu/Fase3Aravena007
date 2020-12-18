from .models import Comic, Editorial
from rest_framework import serializers

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'


class ComicSerializer(serializers.ModelSerializer):
    nombre_editorial = serializers.CharField(read_only=True, source="editorial.nombre")
    editorial = EditorialSerializer(read_only=True)
    editorial_id = serializers.PrimaryKeyRelatedField(queryset=Editorial.objects.all(), source="Editorial")
    nombre = serializers.CharField(required=True, min_length=3)

    def validate_nombre (self, value):
        existe = Comic.objects.filter(nombre_iexact=value).exists()

        if existe:
            raise serializers.ValidationError(" Este Comic ya existe ")

        return value
    
    class Meta:
        model = Comic
        fields = '__all__'
        