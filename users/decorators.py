from django.shortcuts import redirect
from django.contrib.auth import get_user_model

User = get_user_model()


def schoolmaster_required(view_func):
    def _wrapper(request, *args, **kwargs):
        if request.user.role != 1:
            return redirect('core:index')
        return view_func(request, *args, **kwargs)

    return _wrapper
