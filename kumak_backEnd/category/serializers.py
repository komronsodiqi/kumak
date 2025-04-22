from rest_framework import serializers
from category.models import Category, Product

class CategorySerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField()
   description = serializers.CharField()
   
   def create(self, validated_data):
       instance = Category(
           name=validated_data.get('name'),
           description=validated_data.get('description'))
       instance.save()
       return instance
   
   def update(self, instance, validated_data):
       instance.name = validated_data.get("name")
       instance.description = validated_data.get("description", instance.description)
       instance.save()
       return instance

class CategorySerializer2(serializers.ModelSerializer):
   class Meta:
       model = Category
       fields = ("id", "name", "description")

class ProductSerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField()
   description = serializers.CharField()
   rating = serializers.CharField()
   price = serializers.FloatField()
   image_url = serializers.CharField(required=False)
   
   def create(self, validated_data):
       instance = Product(
           name=validated_data.get('name'),
           description=validated_data.get('description'),
           rating=validated_data.get('rating'),
           price=validated_data.get('price'),
           image_url=validated_data.get('image_url')
        )
       instance.save()
       return instance
   
   def update(self, instance, validated_data):
       instance.name = validated_data.get("name", instance.name)
       instance.description = validated_data.get("description", instance.description)
       instance.save()
       return instance

class ProductSerializer2(serializers.ModelSerializer):
   image_url = serializers.CharField(max_length=1500)
   
   class Meta:
       model = Product
       fields = ("id", "name", "description", "rating", "image_url", "price", "categoryId")