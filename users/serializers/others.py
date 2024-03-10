from rest_framework import serializers
from users.models import AddressRegister
from users.models import User


class UserSignupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',

            'first_name',
            'last_name',
            'email',
            'mobile_number',
            'date_of_birth',
            'gender',

            'profile_picture',
        )

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.is_customer = True
        instance.save()
        return instance


class UserDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',

            'first_name',
            'last_name',
            'email',
            'mobile_number',
            'date_of_birth',
            'gender',

            'profile_picture',
            'is_customer',
            'customer_id',
            'is_suspended'
        )


class AddressRegisterModelSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, attrs):
        return UserDataModelSerializer(attrs.user).data

    class Meta:
        model = AddressRegister
        fields = '__all__'

