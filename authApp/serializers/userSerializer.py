from authApp.models.user import User
#from authApp.models.account import Account
#from authApp.serializers.accountSerializer import AccountSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    #account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id','username','password','name','email','company','role']
    
    def to_representation(self, obj):
        user = User.objects.get(id = obj.id) 
        
        return {
            'id':user.id,
            'username':user.username,
            'name': user.name,
            'email':user.email,
            'company':user.company,
            'role':user.role
        }
    
    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

        