from schemas.orders import OrderCreate, OrderRead
from api.dependencies.grpc.bar import BarClient
from api.dependencies.grpc.kitchen import KitchenClient
from api.dependencies.grpc.bakery import BakeryClient


class RestaurantLogic:
    def __init__(self):
        self.bar_client = BarClient()

    def _get_drink(self, drink: str):
        return BarClient().get_order(order=drink)

    def _get_meal(self, meal: str):
        return KitchenClient().get_order(order=meal)

    def _get_dessert(self, dessert: str):
        return BakeryClient().get_order(order=dessert)

    def build_order(self, order_create: OrderCreate) -> OrderRead:
        drink = self._get_drink(order_create.drink)
        meal = self._get_meal(order_create.meal)
        dessert = self._get_dessert(order_create.dessert)

        return OrderRead(
            order_id=order_create.order_id,
            drink=drink["order_status"],
            meal=meal["order_status"],
            dessert=dessert["order_status"],
        )
