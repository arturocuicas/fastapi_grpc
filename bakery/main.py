import logging
from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from core.config import settings
from pb.bakery_pb2_grpc import add_BakeryServicer_to_server
from services.bakery import BakeryBaseService


class BakeryService(BakeryBaseService):
    pass


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    add_BakeryServicer_to_server(BakeryService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=settings.logging_level, format=settings.log_format)
    logging.info('Bakery Server Starter...')

    serve()
