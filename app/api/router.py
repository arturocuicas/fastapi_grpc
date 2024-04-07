from fastapi import APIRouter

from api.routes.restaurants import router as restaurants_router

router = APIRouter()


router.include_router(restaurants_router, tags=["Restaurants"], prefix="/restaurants")
