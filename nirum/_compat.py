import datetime

from six import PY3


__all__ = 'classname', 'utc'


def classname(cls_):
    if PY3:
        return cls_.__qualname__
    else:
        return cls_.__name__


try:
    utc = datetime.timezone.utc
except AttributeError:
    ZERO = datetime.timedelta(0)
    HOUR = datetime.timedelta(hours=1)

    class UTC(datetime.tzinfo):
        """UTC"""

        def utcoffset(self, dt):
            return ZERO

        def tzname(self, dt):
            return "UTC"

        def dst(self, dt):
            return ZERO

    utc = UTC()
