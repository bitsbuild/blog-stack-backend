from rest_framework.permissions import IsAuthenticated
class AccessByOwnership(IsAuthenticated):
    pass