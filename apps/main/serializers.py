from rest_framework import serializers


from .models import Product


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["category"] = instance.category.title
        return rep


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ("id",)


class ProductCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'