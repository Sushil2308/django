from django.http import Http404, HttpResponseGone


class Resolver404(Http404):
    pass


class NoReverseMatch(Exception):
    pass


class HTTP410(HttpResponseGone):
    pass
