from acls.models import LoginACL
from authentication import errors
from common.utils import get_request_ip

from django.shortcuts import render, reverse
from django_cas_ng.views import LoginView
from django.utils.translation import ugettext as _


def check_login_acl(request, user, ip):
    # ACL 限制用户登录
    is_allowed, limit_type = LoginACL.allow_user_to_login(user, ip)
    if is_allowed:
        return
    if limit_type == 'ip':
        raise errors.LoginIPNotAllowed(username=user.username, request=request)
    elif limit_type == 'time':
        raise errors.TimePeriodNotAllowed(
            username=user.username, request=request)


class CasAuthRequestView(LoginView):
    def successful_login(self, request, next_page):
        ip = get_request_ip(request)
        try:
            check_login_acl(request, request.user, ip)
        except Exception as e:
            context = {
                'title': _('Authentication failed'),
                'message': _('Authentication failed (before login check failed): {}').format(e),
                'interval': 10,
                'redirect_url': reverse('authentication:login'),
                'auto_redirect': True,
            }
            return render(request, 'auth_fail_flash_message_standalone.html', context)
        return super().successful_login(request, next_page)
