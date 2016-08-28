from sqlite3 import IntegrityError

from tastypie import fields
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.constants import ALL
from tastypie.exceptions import BadRequest
from tastypie.paginator import Paginator
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS

from ServiceKGServer.models import Category, Advertisement, PageDataAddition


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        filtering = {
            'name': ALL
        }


class ADVResource(PageDataAddition, ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category', null=True)

    class Meta:
        limit = 0
        allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
        queryset = Advertisement.objects.order_by('position')
        position = 100
        resource_name = 'advert'
        resource_name_page = 'page'
        filtering = {
            'name': ALL_WITH_RELATIONS,
            'category': ALL_WITH_RELATIONS
        }

        class_paginator = Paginator
        authorization = Authorization()
        authentication = Authentication()
        include_resource_uri = False

    def obj_create(self, bundle, **kwargs):
        try:
            bundle = super(ADVResource, self).obj_create(bundle, **kwargs)
            bundle.obj.user.set_password(bundle.data['user'].get('password'))
            bundle.obj.user.save()
        except IntegrityError:
            print "error : user already exists."
            raise BadRequest('That username already exists')
        return bundle
