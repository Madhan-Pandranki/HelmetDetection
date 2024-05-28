from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Frame,NameURL

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.is_active = True  # Deactivate account until it is verified
        user.save()
        return user
    
    # def send_activation_email(self, user):
    #     current_site = get_current_site(self.context.get('request'))
    #     mail_subject = 'Activate your account.'
    #     message = render_to_string('account_activation_email.html', {
    #         'user': user,
    #         'domain': current_site.domain,
    #         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #         'token': default_token_generator.make_token(user),
    #     })
    #     to_email = user.email
    #     email = EmailMessage(mail_subject, message, to=[to_email])
    #     email.send()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials or account not activated.")

class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = Frame
        fields = ['file']

class NameURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameURL
        fields = ['name', 'url']