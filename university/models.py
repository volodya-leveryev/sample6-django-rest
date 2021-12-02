from django.db.models import Model, CharField, fields
from rest_framework import serializers


class Student(Model):
    last_name = CharField('фамилия', max_length=25)
    first_name = CharField('имя', max_length=25)
    second_name = CharField('отчество', max_length=25, blank=True, default='')
    id_number = CharField('номер студбилета', max_length=15)

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
