from grpc import StatusCode
from grpc_interceptor.exceptions import NotFound, GrpcException

from pb.kitchen_pb2 import OrderResponse
from pb.kitchen_pb2_grpc import KitchenServicer

mock_meals = {
    "pasta": 10,
    "pizza": 5,
    "meat": 0
}


class KitchenBaseService(KitchenServicer):

    def GetOrder(self, request, context):
        meals_stock = mock_meals.get(request.order)

        if meals_stock is None:
            raise GrpcException(
                details="Meal not Found",
                status_code=StatusCode.NOT_FOUND,
            )

        if meals_stock == 0:
            raise NotFound(
                details="Meal out of stock",
                status_code=StatusCode.NOT_FOUND,
            )

        return OrderResponse(order_status="Delivery!")
