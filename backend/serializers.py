from rest_framework import serializers
from backend.models import Product, Category, Xyz, UserAddress, OrderInfo


class ProductSer(serializers.ModelSerializer):  # 并说明序列化所有字段
    class Meta:
        # model=ShopCart#获取所有购物车表中的数据，并序列化
        model = Product  # 可以更换数据库,这是个接口
        fields = "__all__"  # 是否显示所有数据,也是个接口
        # fields = ['id', 'image',"new_price"]  # 这里选择只显示这3个
        depth = 1  # 深度为1 关联表也会一起序列化


class CategorySer(serializers.ModelSerializer):  # 并说明序列化所有字段
    class Meta:
        # model=ShopCart#获取所有购物车表中的数据，并序列化
        model = Category  # 可以更换数据库,这是个接口
        fields = "__all__"  # 是否显示所有数据,也是个接口
        # fields = ['id', 'image',"new_price"]  # 这里选择只显示这3个
        depth = 1  # 深度为1 关联表也会一起序列化


class UserAddressSer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'
        depth = 1


class CreatUserAddressSer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'
        # 不能有深度，否则create时需要将关联表数据也同时提交，或外键为null


class OrderInfoSer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = '__all__'
        depth = 1
