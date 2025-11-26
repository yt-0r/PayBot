from aiogram import Router
from handlers.user.start import router as start_router
from handlers.user.referrer import router as referrer_router
from handlers.user.status import router as check_sub_router
from handlers.user.help import router as help_router
from handlers.user.payment import router as payment_router
from handlers.admin.address import router as address_router
from handlers.admin.coupon import router as coupon_router

router = Router()
router.include_router(start_router)
router.include_router(referrer_router)
router.include_router(check_sub_router)
router.include_router(help_router)
router.include_router(payment_router)
router.include_router(address_router)
router.include_router(coupon_router)
