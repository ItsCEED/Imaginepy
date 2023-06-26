class ImaginePyException(Exception):
    """Exceptions used by pyimagine."""


class InvalidWord(ImaginePyException):
    """Used word is invalid."""


class InvalidSize(ImaginePyException):
    """Both sizes must be the same."""


class BannedContent(ImaginePyException):
    """Content wanting to be generated is banned."""
