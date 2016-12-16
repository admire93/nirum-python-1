""":mod:nirum.exc`
~~~~~~~~~~~~~~~~~~

"""
from six.moves import urllib

__all__ = (
    'InvalidNirumServiceMethodNameError',
    'InvalidNirumServiceMethodTypeError',
    'HttpError',
    'NirumProcedureArgumentError',
    'NirumProcedureArgumentRequiredError',
    'NirumProcedureArgumentValueError',
    'NirumServiceError',
    'NirumUrlError',
    'UnexpectedNirumResponseError',
)


class NirumServiceError(Exception):
    """Base nirum service error"""


class InvalidNirumServiceMethodNameError(ValueError, NirumServiceError):
    """Raised when nirum service has invalid method name."""


class InvalidNirumServiceMethodTypeError(TypeError, NirumServiceError):
    """Raised when nirum service method is not callable."""


class NirumProcedureArgumentError(ValueError, NirumServiceError):
    """WIP"""


class NirumProcedureArgumentRequiredError(NirumProcedureArgumentError):
    """WIP"""


class NirumProcedureArgumentValueError(NirumProcedureArgumentError):
    """WIP"""


class HttpError(urllib.error.HTTPError, NirumServiceError):
    """Nirum HTTP Error."""

    DEFAULT_ERROR_CODE = 500

    def __init__(self, code=DEFAULT_ERROR_CODE,
                 description='something goes wrong.', url=None):
        super(HttpError, self).__init__(
            url=url,
            code=code,
            msg=description,
            hdrs=None, fp=None
        )
        self.description = description

    def __repr__(self):
        return 'HttpError(code={}, description={})'.format(
            self.code, self.description
        )


class NirumUrlError(urllib.error.URLError, NirumServiceError):
    """TODO"""

    def __init__(self, exc):
        self.text = exc.read()
        super(NirumUrlError, self).__init__(exc.reason)


class UnexpectedNirumResponseError(HttpError):
    """TODO"""
