from django.contrib import admin

from backend.models import *

admin.site.site_header = "销售管理系统"
admin.site.site_title = "欢迎进销售后台管理~"
admin.site.index_title = "天宇集团"

admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(UserAddress)
admin.site.register(OrderInfo)


class category_product(admin.StackedInline):
    model = Product
    # 额外的表数量（用于新增子表数据）
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [category_product]


admin.site.register(Category,CategoryAdmin)  # 后面跟上上面创建的类说明使用
