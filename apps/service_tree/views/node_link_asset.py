from rest_framework.decorators import action

from base.response import json_ok_response, json_error_response
from base.views import BaseModelViewSet

from ..models import NodeLinkAsset, NodeLinkClassify
from ..serializers import NodeLinkAssetSerializer
from ...cmdb.verify.operate import OperateInstance
from ...cmdb.serializers import AssetSerializer


class NodeLinkAssetViewSet(BaseModelViewSet):
    queryset = NodeLinkAsset.objects.filter().order_by('-id')
    serializer_class = NodeLinkAssetSerializer
    ordering_fields = (
        'id',
    )
    filter_fields = ('id', 'node_link',)
    search_fields = ('asset__data',)

    def list(self, request, *args, **kwargs):
        try:
            node_link = request.query_params.get('node_link')
            if not node_link:
                return json_error_response('node_link是必传参数')
            node_classify = NodeLinkClassify.objects.filter(id=node_link).first()
            if not node_classify:
                return json_error_response('找不到节点与表的绑定关系!')

            classify_field_obj = OperateInstance.get_classify_field(node_classify.classify.id)
            if not classify_field_obj:
                return json_error_response('找不到分类表的字段表')

            ordering = request.query_params.get('ordering', '')
            ordering = ordering.replace('+', '').strip()
            if ordering:
                if self.serializer_class is None:
                    queryset = self.filter_queryset(self.get_serializer_class().Meta.model.objects.order_by(ordering))
                else:
                    queryset = self.filter_queryset(self.serializer_class.Meta.model.objects.order_by(ordering))
            else:
                queryset = self.filter_queryset(self.get_queryset())
            page = request.query_params.get('page', '')
            size = request.query_params.get('size', '')
            if page or size:
                page_queryset = self.paginate_queryset(queryset)
                if page is not None:
                    da_l = []
                    for i in page_queryset:
                        a = AssetSerializer(i.asset, many=False)
                        t_d = a.data
                        t_d['id'] = i.id
                        t_d['node_link'] = i.node_link.id
                        t_d['asset'] = i.asset.id
                        da_l.append(t_d)
                    return self.get_paginated_response({'data': da_l,
                                                        'fields': classify_field_obj.fields,
                                                        'rules': classify_field_obj.fields
                                                        })
            da_l = []
            for i in queryset:
                a = AssetSerializer(i.asset, many=False)
                t_d = a.data
                t_d['id'] = i.id
                t_d['node_link'] = i.node_link.id
                t_d['asset'] = i.asset.id
                da_l.append(t_d)

            return json_ok_response(data={'data': da_l,
                                          'fields': classify_field_obj.fields,
                                          'rules': classify_field_obj.fields
                                          })
        except Exception as e:
            return json_error_response(message=str(e))
