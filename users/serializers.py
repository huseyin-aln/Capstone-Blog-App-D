from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer
from users.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [validators.UniqueValidator(queryset=User.objects.all(), message = "This email has been used.")]
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {"input_type": "password"}
    )
    password1 = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {"input_type": "password"}
    )
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password1'
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError(
                {"password": "Password didn't match...."}
            )
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("password1")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'id'
        )


class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = (
            'key',
            'user'
        )


class ProfileUpdateForm(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = (
            'image',
            'user'
        )

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.image = validated_data.get('image', instance.image)
        instance.save()   

        user.username = user_data.get(
            'username',
            user.username
        ) 
        user.email = user_data.get(
            'email', 
            user.email
        )
        user.save()

        return instance