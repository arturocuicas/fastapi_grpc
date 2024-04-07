from grpc import StatusCode
from grpc_interceptor.exceptions import NotFound, GrpcException

from pb.bar_pb2 import OrderResponse
from pb.bar_pb2_grpc import BarServicer

mock_drinks = {
    "coffee": 10,
    "soda": 5,
    "beer": 0
}


class BarBaseService(BarServicer):

    def GetOrder(self, request, context):
        drinks_stock = mock_drinks.get(request.order)

        if drinks_stock is None:
            raise GrpcException(
                details="Drink not Found",
                status_code=StatusCode.NOT_FOUND,
            )

        if drinks_stock == 0:
            raise NotFound(
                details="Drink out of stock",
                status_code=StatusCode.NOT_FOUND,
            )

        return OrderResponse(order_status="Delivery!")
