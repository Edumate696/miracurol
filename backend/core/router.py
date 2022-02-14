from fastapi import FastAPI

from backend.core.docs import description, tags_metadata
from backend.resources.user import user_router

router = FastAPI(
    title='Miracurol API',
    description=description,
    version='un-versioned',
    contact={},
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata,
    docs_url=None,
    redoc_url=None,
    swagger_ui_parameters={},
)

# Attach User resource
router.include_router(user_router)
