from django.contrib import admin
from app.models import ProductModel, CategoryModel, OrderModel, CommentModel 

admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(OrderModel)
admin.site.register(CommentModel)