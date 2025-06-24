from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer,CharField,ValidationError
class UserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    model = User
    fields = ['username','password','email','confirm_password']
    extra_kwargs = {
        "password":{'write_only':True},
    }
    def validate(self,data):
        if data['password'] == data['confirm_password']:
            return data
        else:
            raise ValidationError(
                {
                    "Error":"Passwords Not Matching"
                }
            )
    def create(self,validated_data):
        user = User(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user