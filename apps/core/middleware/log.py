import logging

# Get the logging instance
logger = logging.getLogger("logging_mw")


def simple_logging_middleware(get_response):
    def middleware(request):
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers["Content-Type"]
        user_agent = request.headers["User-Agent"]

        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"

        logger.info(msg)

        response = get_response(request)

        # status_code = response.status_code

        # msg = f"{status_code}"
        # logger.info(msg)

        return response

    return middleware
