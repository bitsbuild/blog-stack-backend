from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer,CharField,ValidationError
class UserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','email','confirm_password']
    extra_kwargs = {
        "password":{'write_only':True},
    }
    def validate(self,data):
        if User.objects.filter(username=data['username']).exists():
            return ValidationError(
                {
                    "Error":"Account Already Exists For This Email ID"
                }
            )
        elif data['password'] != data['confirm_password']:
            raise ValidationError(
                {
                    "Error":"Passwords Not Matching"
                }
            )
        else:
            return data  
    def create(self,validated_data):
        validated_data.pop('confirm_password')
        user = User(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user