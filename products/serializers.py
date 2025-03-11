from rest_framework import serializers

from .models import Category, Product, File


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')


class FileSerializers (serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('title', 'file')


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)   

    class Meta:
        model = Product
        field = ('title', 'description', 'avatar', 'categories') 