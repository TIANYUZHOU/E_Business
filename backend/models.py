from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField  # 头部增加这行代码导入UEditorField
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime


class Xyz(models.Model):
    name = models.CharField(max_length=100)


# 商品分类表---------,

class Category(models.Model):
    title = models.CharField('分类名', null=True, blank=True, max_length=300)
    # 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    def __str__(self):
        return self.title  # 只将对象中的title返回

    class Meta:
        ordering = ['id']
        # 后台管理中的名称
        verbose_name = '商品分类表'
        verbose_name_plural = '商品分类表'


# 产品表
class Product(models.Model):
    name = models.CharField('商品名', null=True, blank=True, max_length=300)
    small_image = models.ImageField(upload_to='drug_img/%Y/%m/%d/', verbose_name='商品图片')
    price = models.IntegerField('现价', null=True, blank=True, default=89)  # 现价
    origin_price = models.IntegerField('原价', null=True, blank=True, default=99)  # 原价
    spec = models.TextField('商品说明', null=True, blank=True, default="None")  # 描述
    total_sales = models.IntegerField('销售量', null=True, blank=True, default=0)  # 总销量
    vip_price = models.IntegerField('会员价', null=True, blank=True, default=79)  # 会员
    # 外键
    # category = models.ForeignKey(verbose_name='商品分类', to='Category', on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category,verbose_name='商品分类', on_delete=models.DO_NOTHING)
    # 百度富文本编辑器
    body = UEditorField('内容', width=800, height=500,
                        toolbars="full", imagePath="upimg/", filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None, blank=True
                        )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = '商品表'
        verbose_name_plural = '商品表'


# 用户扩展表
class myusertwo(models.Model):
    user_type_choices = (
        (1, "普通用户"),
        (2, "普通会员"),
        (3, "白金会员"),
        (4, "黄金会员"),
    )
    # 关联上系统本身的User表 on_delete级联删除（关联的表中数据一起被删除）
    user = models.OneToOneField(User, related_name="extension", on_delete=models.CASCADE)
    phone = models.CharField('手机号', max_length=11, unique=True)
    icon_image = models.ImageField('头像', upload_to='icon_img/%Y/%m/%d/', null=True, blank=True)
    l_edit = models.DateTimeField('编辑时间', auto_now_add=True)
    c_time = models.DateTimeField('添加时间', auto_now=True)
    user_type = models.IntegerField('用户等级', choices=user_type_choices, null=True, blank=True)
    token = models.CharField(max_length=3000, blank=True)
    expiration_time = models.DateTimeField(default=datetime.now, verbose_name="过期时间", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['id']
        verbose_name = '注册用户'
        verbose_name_plural = '注册用户'


# 当接收到User表.save()运行的信号之后，执行下面函数
@receiver(post_save, sender=User)
# instance表示被保存的对象(实例)
# created 布尔值; True如果创建了新记录（True表示数据创建）
# 参考https://www.jb51.net/article/164598.htm
def create_user_extension(sender, instance, created, **kwargs):
    if created:
        # 如果第一次创建userextension绑定
        myusertwo.objects.create(user=instance)
    else:
        # 修改user对象，那么也要将extension进行保存
        instance.extension.save()


# 地址表
class UserAddress(models.Model):
    # 用户收货地址
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", related_name="uextension", null=True)
    province = models.CharField("省份", max_length=100, default="", null=True, blank=True)
    city = models.CharField("城市", max_length=100, default="", null=True, blank=True)
    district = models.CharField("区域", max_length=100, default="", null=True, blank=True)
    address = models.CharField("详细地址", max_length=100, default="", null=True, blank=True)
    singer_name = models.CharField("签收人", max_length=100, default="", null=True, blank=True)
    singer_mobile = models.CharField("电话", max_length=100, default="", null=True, blank=True)
    add_tiem = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        # 返回的类型是类的实例（对象），值是对象的address
        return self.address


class OrderInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ouextension", verbose_name="用户")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="opextension", verbose_name="商品")
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE, related_name="oaextension", verbose_name="地址")
    order_sn = models.CharField("订单编号", max_length=30, unique=True)
    product_num = models.CharField("商品数量", max_length=30)
    post_script = models.CharField("订单留言",max_length=200,null=True,blank=True)
    order_amount = models.FloatField("订单金额",default=0.0)
    add_time = models.DateTimeField("添加时间",default=datetime.now,null=True,blank=True)

    class Meta:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_sn

# #购物车表
# class ShopCart(models.Model):
#     #项目id
#     card_id=models.CharField(max_length=256)
#     #产品
#     product=models.ForeignKey(to=Product,unique=False,on_delete=models.DO_NOTHING)
#     #数量
#     quantity=models.IntegerField(default=1)
#     create_time=models.DateTimeField(null=True, blank=True, default=datetime.datetime.now())
#     #cookie过期时间
#     expiracation_time=models.DateTimeField(null=True,blank=True,default=datetime.datetime.now()+datetime.timedelta(days=7))
#
#     def __str__(self):
#         return self.product.title + " quantity:" + str(self.quantity)
#
#     # 求购物车商品价格总和
#     def sum_price(self):
#         return self.quantity * self.product.new_price
#
#     # 购物车中商品增加数量
#     def add_quantity(self):
#         self.quantity += 1
#         self.save()
#
#     # 购物车中商品数量减一
#     def del_quantity(self):
#         self.quantity -= 1
#         if self.quantity < 1:
#             self.delete()
#         else:
#             self.save()
#
#     # 删除购物车中的商品
#     def delete_product(self):
#         self.delete()
#
#
#
# #当前下订单的用户信息表.
# class UserProfile(models.Model):
#     belong_to=models.OneToOneField(to=User,related_name="profile",on_delete=models.CASCADE)
#     phone=models.CharField(max_length=11,default="12345678910")
#     address=models.CharField(max_length=512,default="北京")
#     birth_data=models.DateField(null=True,blank=False)
#     uuid=models.CharField(max_length=15,default="None")
#
#     def __str__(self):
#         return self.belong_to.username+":"+self.address
#
#
#
# #订单表
# class Order(models.Model):#订单所有者表(收货人)
#     status=(
#         (0,"等待付款"),
#         (-1,"失败订单"),
#         (1,"成功订单"),
#     )
#     user=models.ForeignKey(to=User,related_name="orders",on_delete=models.CASCADE)
#     phone=models.CharField(max_length=15)
#     address=models.CharField(max_length=512)
#     total=models.IntegerField(default=0)
#     create_time=models.DateTimeField(null=True,default=datetime.datetime.now())
#     status=models.IntegerField(choices=status,default=0)
#     #products=models.ForeignKey(to=Order_product,on_delete=models.CASCADE)
#
# #订单商品表
# class Order_product(models.Model):#订单表
#     title=models.CharField(max_length=512)
#     image=models.CharField(max_length=512)
#     price=models.IntegerField()
#     quantity=models.IntegerField()
#     product_id=models.IntegerField()
#     order=models.ForeignKey(to=Order,related_name="products",default=None,null=True,blank=True,on_delete=models.CASCADE)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# class Order(models.Model):
#     status=((0,"等待付款"),(-1,"失败订单"),(1,"成功订单"),)
#     user=models.ForeignKey(to=User,related_name="orders",on_delete=models.DO_NOTHING)
#     phone=models.CharField(max_length=15)
#     address=models.CharField(max_length=512)
#     total=models.IntegerField(default=0)
#     create_time=models.DateTimeField(null=True,blank=True,default=datetime.datetime.now())
#     status=models.IntegerField(choices=status,default=0)
#     #products=models.ForeignKey(to=Order_product,on_delete=models.DO_NOTHING)
#
#
#
# class Order_product(models.Model):
#     title=models.CharField(max_length=512)
#     image=models.CharField(max_length=512)
#     price=models.IntegerField()
#     quantity=models.IntegerField()
#     product_id=models.IntegerField()
#     order=models.ForeignKey(to=Order,related_name="products",default=None,null=True,blank=True,on_delete=models.DO_NOTHING)
#
#
# #分页存参
# class fenyechanshui(models.Model):
#     fram=models.CharField(max_length=300)
#     fdisk=models.CharField(max_length=300)
#     fcpu=models.CharField(max_length=300)
#     fprice=models.CharField(max_length=300,null=True)
