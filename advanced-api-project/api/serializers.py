from rest_framework import serializers
from .models import Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value
# api/serializers.py

from rest_framework import serializers
from .models import Author  # Import your Author model

class AuthorSerializer(serializers.ModelSerializer):
    # Define fields here if needed

    class Meta:
        model = Author
        fields = '__all__'  # You can specify particular fields if needed
