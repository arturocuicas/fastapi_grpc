import logging
from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from core.config import settings
from pb.bar_pb2_grpc import add_BarServicer_to_server
from services.bar import BarBaseService


class BarService(BarBaseService):
    pass


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    add_BarServicer_to_server(BarService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=settings.logging_level, format=settings.log_format)
    logging.info('Bar Server Starter...')

    serve()
