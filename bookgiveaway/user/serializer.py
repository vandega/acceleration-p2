from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'address', 'image']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
            image=validated_data.get('image'),
        )



        user.set_password(validated_data['password'])
        user.save()
        return user



class UserLoginSerializer(serializers.Serializer):
    """
    uses for registration only
    """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserEditSerializer(serializers.ModelSerializer):
    """
    this class uses only for edit registered users information [patch]
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'address', 'image']