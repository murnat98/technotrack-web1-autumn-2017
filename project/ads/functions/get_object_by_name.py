from django.http import Http404


def get_object_by_name(name, accordance):

    if not name in accordance:
        raise Http404

    return accordance[name]