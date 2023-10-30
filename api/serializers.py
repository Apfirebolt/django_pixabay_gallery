from rest_framework import serializers
from accounts.models import CustomUser
from gallery.models import Gallery


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_staff', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        user = super(CustomUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ('id', 'name', 'user_id', 'created_at', 'updated_at')
        extra_kwargs = {'user_id': {'read_only': True}}

    def create(self, validated_data):
        request = self.context.get("request")
        gallery = Gallery()
        gallery.name = validated_data['name']
        gallery.user_id = request.user
        gallery.save()
        return gallery
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        return super().to_representation(instance)
    
    def to_internal_value(self, data):
        return super().to_internal_value(data)
    
    def validate(self, attrs):
        return super().validate(attrs)
        
