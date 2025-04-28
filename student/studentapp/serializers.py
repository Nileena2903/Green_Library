from rest_framework import serializers
from . models import student_tbl


class studentForm(serializers.ModelSerializer):
    class Meta:
        model = student_tbl
        fields = '__all__'