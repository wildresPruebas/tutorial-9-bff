from fastapi import APIRouter
from .endpoints import users, orders, products, payments

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(orders.router, prefix="/orders", tags=["Orders"])
router.include_router(products.router, prefix="/products", tags=["Products"])
router.include_router(payments.router, prefix="/payments", tags=["Payments"])
