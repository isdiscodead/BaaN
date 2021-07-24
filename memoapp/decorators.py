# from django.http import HttpResponseForbidden
#
# from memoapp.models import Memo
#
#
# def memo_ownership_required(func):
#     def decorated(request, *args, **kwargs):
#         memo = Memo.objects.get(pk=kwargs['pk'])
#         if not memo.writer == request.user:
#             return HttpResponseForbidden()
#         return func(request, *args, **kwargs)
#     return decorated