from fastapi import APIRouter, Depends

from schemas.orders import OrderCreate, OrderRead
from business_logic.restaurants import RestaurantLogic

router = APIRouter()


@router.post(
    "",
    status_code=201,
    name="create_order",
    response_model=OrderRead,
)
def create_order(
    order_create: OrderCreate,
    restaurant_logic: RestaurantLogic = Depends(RestaurantLogic),
) -> OrderRead:

    return restaurant_logic.build_order(order_create=order_create)
