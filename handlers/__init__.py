from aiogram import Router
from .start import router as start_router
from .referrer import router as referrer_router
from .status import router as check_sub_router
from .help import router as help_router

router = Router()
router.include_router(start_router)
router.include_router(referrer_router)
router.include_router(check_sub_router)
router.include_router(help_router)