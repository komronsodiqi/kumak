from rest_framework import serializers
from category.moodels import Category, Product

class CategorySerializer(serializers.Serializer):
   name = serializers.CharField()
   description = serializers.CharField()
   
   def create(self, validated_data):
       instance = Category(
           title=validated_data.get('name'),
           description=validated_data.get('description'))
       instance.save()
   
   def update(self, instance, validated_data):
       instance.name = validated_data.get("name")
       instance.save()
       return validated_data

class CategorySerializer2(serializers.ModelSerializer):
   id = serializers.IntegerField(required=True)
   name = serializers.CharField()
   description = serializers.IntegerField()
   
   class Meta:
       model = Category
       fields = ("id", "name", "description", "created_at")

class ProductSerializer(serializers.Serializer):
   id = serializers.IntegerField()
   name = serializers.CharField()
   description = serializers.CharField()
   rating = serializers.CharField()
   price = serializers.FloatField()
   
   def create(self, validated_data):
       instance = Product(
           name=validated_data.get('name'),
           description=validated_data.get('description'),
           ratting=validated_data.get('rating'),
           price=validated_data.get('price'),
           image_url=validated_data.get('image_url')
        )
       instance.save()
       instance.save()
       return instance
   
   def update(self, instance, validated_data):
       instance.name = validated_data.get("name")
       instance.save()
       return True

class ProductSerializer2(serializers.ModelSerializer):
   id = serializers.IntegerField()
   name = serializers.EmailField()
   description = serializers.CharField()
   rating = serializers.CharField()
   image_url = serializers.CharField(max_length=15)
   price = serializers.CharField()
   
   class Meta:
       model = Product
       fields = ("id", "name", "description" "rating", "image_url", "price", "categoryId")