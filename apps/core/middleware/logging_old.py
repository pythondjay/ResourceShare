from django.conf import settings
from django.utils import timezone
from apps.core.logging import Logging

logging = Logging(str(settings.BASE_DIR / "logs" / "req_res_logs.txt"))


def simple_logging_middleware(get_response):
    def middleware(request):
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers["Content-Type"]
        user_agent = request.headers["User-Agent"]

        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"

        logging.info(msg)
        response = get_response(request)

        status_code = response.status_code

        msg = f"{status_code}"
        logging.info(msg)

        return response

    return middleware


class ViewExecutionTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = timezone.now()
        response = self.get_response(request)
        end_time = timezone.now()
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()

        execution_time = end_time - start_time

        msg = f"Execution time: {execution_time} >> {http_method} | {host_port}{url}"

        logging.info(msg)

        return response
