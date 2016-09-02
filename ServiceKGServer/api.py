from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.constants import ALL
from tastypie.paginator import Paginator
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS

from ServiceKGServer.models import Category, Advertisement


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        filtering = {
            'name': ALL
        }

    childCategories = fields.ToManyField('ServiceKGServer.api.CategoryResource', 'category_set', full=True, null=True)


class ADVResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category', null=True)

    class Meta:
        limit = 0

        queryset = Advertisement.objects.order_by('position')
        position = 100
        resource_name = 'advert'
        filtering = {
            'title': ALL_WITH_RELATIONS,
            'category': ALL_WITH_RELATIONS
        }

        class_paginator = Paginator
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
