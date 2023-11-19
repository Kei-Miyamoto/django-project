from rest_framework import serializers
from app.models.users import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        # fields = ('email', 'user_name', 'name', 'biography', 'date_of_birth', 'phone_number', 'link', 'icon', 'adult_flag', 'ban_count', 'status', 'hash_password', 'salt', 'last_login', )
        fields = '__all__'


# class UserSerializer(serializers.Serializers):
#     email = serializers.EmailField()
#     class Meta:
#         model = Users