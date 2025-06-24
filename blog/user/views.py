from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,throttle_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from user.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
@api_view(['POST'])
@throttle_classes([AnonRateThrottle])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        token,collector = Token.objects.get_or_create(user=serializer.instance)
        return Response(
            {
                "Status":"Account Creation Successful",
                "Token":str(token.key)
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {
            "Status":"Account Creation Failed",
            "Error":str(serializer.errors)
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
@api_view(['POST'])
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def delete_user(request):
    try:
        request.user.delete()
        return Response(
            {
                "Status":"Account Deletion Successful"
            },
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response({
            "Status":"Account Deletion Failed",
            "Error":str(e)
        },status=status.HTTP_400_BAD_REQUEST)
