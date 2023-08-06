from users.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from profiles.models import Profile
from django.core.exceptions import ObjectDoesNotExist


# сериализаторы drf = формы djnago
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'email')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # These are claims, you can add custom claims
        token['first_name'] = user.profile.first_name
        token['last_name'] = user.profile.last_name
        token['phone'] = user.phone
        token['email'] = user.email
        token['verified'] = user.profile.verified
        token['gender'] = user.profile.gender
        token['avatar'] = str(user.profile.avatar)

        hobbies = []
        birthday = None
        try:
            profile = user.profile
            for hobby in profile.hobbies.all():
                # You can choose how to serialize the hobby object; here, we're just using its string representation
                hobbies.append(str(hobby))
                # Extract the user's birthday as an ISO-formatted string (e.g., '2022-03-14') if the field is not null
                if profile.birthday:
                    birthday = profile.birthday.isoformat()
        except ObjectDoesNotExist:
            # If the profile does not exist, you may opt to handle it as you see fit
            pass

        token['birthday'] = birthday
        token['hobbies'] = hobbies

        # ...
        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('phone', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            phone=validated_data['phone'],
            email=validated_data['email']

        )

        user.set_password(validated_data['password'])
        user.save()

        return user
