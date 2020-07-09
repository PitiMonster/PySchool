from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from user.models import UserSchoolStatus


class CustomRegisterSerializer(RegisterSerializer):
    user_status = serializers.ChoiceField(
        required=True,
        choices=UserSchoolStatus.choices,
    )

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['user_status'] = self.validated_data.get('user_status', '')
        return data_dict