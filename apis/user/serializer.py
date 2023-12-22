from rest_framework import serializers

from apis.user.models import User

from django.contrib.auth.hashers import make_password

"""
existe ModelSerializer y Serializer. El primero es para hacer referencia a un modelo 
y el otro hace referencia a varios modelos (general)
"""


class UserSerializer(serializers.Serializer):
    # aqui defino la data que va ingresar
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    # existen los validadores que si es especifico tiene que ir un "validate_" seguido del nombre del atributo
    # validate solo, sirve para el validador general y es el ultimo que se ejecuta
    @staticmethod
    def validate_username(self, data):
        print("Validate Username => {0}".format(data))
        user = User.objects.filter(username=data).first()
        if user:
            raise serializers.ValidationError("Nombre de usuario ya encontrado")
        else:
            return data

    @staticmethod
    def validate_email(self, data):
        print("Validate Email => {0}".format(data))
        user = User.objects.filter(email=data).first()
        if user:
            raise serializers.ValidationError("El email ya se encuentra registrado")
        else:
            return data


    def create(self, validated_data):
        # instance = User()
        # instance.first_name = validated_data.get('first_name', instance.first_name)
        # instance.last_name = validated_data.get('last_name', instance.last_name)
        # instance.username = validated_data.get('username', instance.username)
        # instance.email = validated_data.get('email', instance.email)
        # instance.password = validated_data.get('password', instance.password)
        # instance.save()
        # return instance

        # También se puede realizar de la siguiente forma.
        return User.objects.create(**validated_data)
        # el ( ** ) siginifica que envia el dato del objeto sin tener que nombrar instance.first_name
