# api/serializers.py

from rest_framework import serializers
from .models import Author  # Import your Author model

class AuthorSerializer(serializers.ModelSerializer):
    # Define fields here if needed

    class Meta:
        model = Author
        fields = '__all__'  # You can specify particular fields if needed

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # Assuming an Author has many Books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # Customize fields as necessary
