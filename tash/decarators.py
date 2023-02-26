from django.http import Http404

def check_user_able_to_see_page(*groups):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=groups).exists():
                return function(request, *args, **kwargs)
            raise Http404("SIZNING STATUSIZNGIZ BUS SAHIFGA O'TISH UCHUN ")

        return wrapper

    return decorator