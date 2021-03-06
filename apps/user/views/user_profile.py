# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import json
from django.contrib import auth
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from base.views import BaseModelViewSet, BaseApiView
from base.response import json_ok_response, json_error_response
from ..models import UserProfile
from ..serializers import UserProfileSerializer


class UserProfileViewSet(BaseModelViewSet):
    queryset = UserProfile.objects.filter().order_by('-id')
    serializer_class = UserProfileSerializer

    ordering_fields = ('id',)
    filter_fields = (
        'id',
    )
    search_fields = ('name',)
    def create(self, request, *args, **kwargs):
        try:
            serializer = UserProfileSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_obj = serializer.save()
            user_obj.set_password(request.data.get('password'))
            user_obj.save()
            return json_ok_response(data=serializer.data)
        except Exception as e:
            return json_error_response(message=str(e))

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.copy()
        if data.get('icon'):
            if not isinstance(data.get('icon'), InMemoryUploadedFile):
                del data['icon']
        else:
            del data['icon']
        serializer = self.get_serializer(instance, data=data, partial=kwargs.pop('partial', False))
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return json_ok_response(serializer.data)

    @action(methods=['put'], detail=True, url_path='change-password')
    def change_password(self, request, pk):
        """
        普通用户 修改密码
        """
        username = request.data.get('username')
        old_pwd = request.data.get('old_password')
        new_pwd = request.data.get('new_password')
        if username and old_pwd and new_pwd:
            user_obj = auth.authenticate(request, username=username, password=old_pwd)
            if user_obj:
                user_obj.set_password(new_pwd.strip())
                user_obj.save()
                return json_ok_response(data=f'{user_obj.username} 账户密码修改成功!')
            else:
                return json_error_response(message='用户或密码错误,请检查重试!')
        else:
            return json_error_response(message='<username>,<old_password>,<new_password>为必传参数.')

    @action(methods=['put'], detail=True, url_path='reset-password')
    def reset_password(self, request, pk):
        """管理员重置密码"""
        instance = self.get_object()
        new_pwd = request.data.get('new_password')
        if new_pwd:
            instance.set_password(new_pwd.strip())
            instance.save()

            return json_ok_response(data=f'{instance.name} 账户密码修改成功!')
        else:
            return json_error_response(message='<name>,<new_password>为必传参数.')

    def list(self, request, *args, **kwargs):
        return super(UserProfileViewSet, self).list(request, *args, **kwargs)


class UserInfoApiView(BaseApiView):
    """
    通过token用户信息
    """

    def get(self, request, *args, **kwargs):
        user = request.user
        try:
            u = UserProfile.objects.get(id=user.id)
        except UserProfile.DoesNotExist:
            return json_error_response(message='not found')
        s = UserProfileSerializer(u)
        return json_ok_response(data=s.data)


class UserLogoutApiView(BaseApiView):
    """
    通过token用户信息
    """

    def post(self, request, *args, **kwargs):
        return json_ok_response(data='ok')
