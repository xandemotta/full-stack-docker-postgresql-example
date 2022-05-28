from fastapi import HTTPException


def http_exception_handler(_, exc: HTTPException):
    return {
        'status_code': exc.status_code,
        'detail': exc.detail
    }
