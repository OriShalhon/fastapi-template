from fastapi import APIRouter

from .routers import auth, users  # noqa

router = APIRouter()

# Include all routers here
router.include_router(users.router)
router.include_router(auth.router)
