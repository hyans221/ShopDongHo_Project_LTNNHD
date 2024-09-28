# from django.shortcuts import redirect
# from django.urls import reverse

# class LoginRequiredMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if not request.user.is_authenticated and self._requires_login(request):
#             return redirect(reverse('admin_login'))
#         elif request.user.is_authenticated and request.path == reverse('admin_login'):
#             return redirect(reverse('admin:pages_admin/dashboard'))
#         return self.get_response(request)

#     def _requires_login(self, request):
#         admin_urls = (
#             reverse('admin_login'),
#         )
#         if request.path in admin_urls:
#             return False
#         return True