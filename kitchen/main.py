import logging
from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from core.config import settings
from pb.kitchen_pb2_grpc import add_KitchenServicer_to_server
from services.kitchen import KitchenBaseService


class KitchenService(KitchenBaseService):
    pass


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    add_KitchenServicer_to_server(KitchenService(), server)
    server.add_insecure_port("[::]:50053")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=settings.logging_level, format=settings.log_format)
    logging.info('Kitchen Server Starter...')

    serve()
