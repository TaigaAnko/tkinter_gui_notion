class BadRequestError(Exception):
    """400 Bad Request 用のエラー"""

    pass


class UnauthorizedError(Exception):
    """401 Unauthorized 用のエラー"""

    pass


class GeneralAPIError(Exception):
    """その他のエラー"""

    pass
