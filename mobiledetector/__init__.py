from useragents import search_strings
from flask import request

def is_mobile(request):
    if hasattr(request, 'HTTP_X_OPERAMINI_FEATURES'):
        # Then it's running opera mini. 'Nuff said.
        # Reference from:
        #  http://dev.opera.com/articles/view/opera-mini-request-headers/
        return True

    if hasattr(request, 'HTTP_ACCEPT'):
        s = request.HTTP_ACCEPT.lower()
        if 'application/vnd.wap.xhtml+xml' in s:
            # Then it's a wap browser
            return True

    if hasattr(request, 'HTTP_USER_AGENT'):
        # This takes the most processing. Surprisingly enough, when I
        # Experimented on my own machine, this was the most efficient
        # algorithm. Certainly more so than regexes.
        # Also, Caching didn't help much, with real-world caches.
        s = request.HTTP_USER_AGENT.lower()
        for ua in search_strings:
            if ua in s:
                return True
    return false


def detect_mobile(view):
    """View Decorator that adds a "mobile" attribute to the request which is
       True or False depending on whether the request should be considered
       to come from a small-screen device such as a phone or a PDA"""

    def detected(*args, **kwargs):
        request.mobile = is_mobile(request)
        return view(*args, **kwargs)
    detected.__doc__ = "%s\n[Wrapped by detect_mobile which detects if the request is from a phone]" % view.__doc__
    return detected


__all__ = ['detect_mobile']
