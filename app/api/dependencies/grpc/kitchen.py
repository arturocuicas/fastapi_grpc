import grpc
from google.protobuf.json_format import MessageToDict

from core.config import settings
from pb.kitchen_pb2 import OrderRequest
from pb.kitchen_pb2_grpc import KitchenStub


class KitchenClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel(f"{settings.grpc_kitchen}:50053")
        # self.channel = grpc.insecure_channel("0.0.0.0:50053")
        self.stub = KitchenStub(self.channel)

    def get_order(self, order):
        try:
            stub = self.stub.GetOrder(OrderRequest(order=order))

            return MessageToDict(
                stub,
                preserving_proto_field_name=True,
                including_default_value_fields=True
            )

        except grpc.RpcError as rpc_error:
            return {
                "order_status": rpc_error.details()
            }
