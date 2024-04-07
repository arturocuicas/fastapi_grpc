from grpc import StatusCode
from grpc_interceptor.exceptions import NotFound, GrpcException

from pb.bakery_pb2 import OrderResponse
from pb.bakery_pb2_grpc import BakeryServicer

mock_desserts = {
    "cookie": 10,
    "donut": 5,
    "gelato": 0
}


class BakeryBaseService(BakeryServicer):

    def GetOrder(self, request, context):
        desserts_stock = mock_desserts.get(request.order)

        if desserts_stock is None:
            raise GrpcException(
                details="Dessert not Found",
                status_code=StatusCode.NOT_FOUND,
            )

        if desserts_stock == 0:
            raise NotFound(
                details="Dessert out of stock",
                status_code=StatusCode.NOT_FOUND,
            )

        return OrderResponse(order_status="Delivery!")
