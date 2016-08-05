from tastypie import fields
from tastypie.constants import ALL
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
        queryset = Advertisement.objects.order_by('position')
        resource_name = 'advert'
        filtering = {
            'name': ALL_WITH_RELATIONS,
            'category': ALL_WITH_RELATIONS
        }
