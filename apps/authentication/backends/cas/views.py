from acls.models import LoginACL
from apps.authentication import mixins
from apps.authentication.mixins import AuthACLMixin
from authentication import errors
from common.utils import get_request_ip

from django.shortcuts import render, reverse
from django_cas_ng.views import LoginView
from django.utils.translation import ugettext as _
from django.contrib.auth import logout as auth_logout


class CasAuthRequestView(LoginView, mixins.AuthMixin):
    def successful_login(self, request, next_page):
        ip = get_request_ip(request)
        try:
            self._check_login_acl(request.user, ip)
        except Exception as e:
            auth_logout(request)
            context = {
                'title': _('Authentication failed'),
                'message': _('Authentication failed (before login check failed): {}').format(e),
                'interval': 10,
                'redirect_url': reverse('authentication:login'),
                'auto_redirect': True,
            }
            return render(request, 'auth_fail_flash_message_standalone.html', context)
        return self.redirect_to_guard_view()
