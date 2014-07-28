import urllib
import urlparse

def url_fix(s, charset='utf-8'):
    """
    Fixes URLs which are not real URLs, as they contains characters
    like ' ' and so on. It is inspired (read: it's a rip-off) the
    Werkzeug ``url_fix`` function, which you can find here:
    https://github.com/mitsuhiko/werkzeug/blob/master/werkzeug/urls.py

    :param charset: the target charset for the URL if the url eas given as unicode
    """
    if isinstance(s, unicode):
        s = s.encode(charset, 'ignore')

    scheme, netloc, path, qs, anchor = urlparse.urlsplit(s)
    path = urllib.quote(path, '/%')
    qs = urllib.quote(qs, ':&=')
    fixed_url = urlparse.urlunsplit((scheme, netloc, path, qs, anchor))
    return fixed_url
