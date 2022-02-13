from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from backend.core.docs import get_rapidoc_html

router = FastAPI(
    title='Miracurol API',
    docs_url=None, redoc_url=None,
)


# Attach api docs endpoint
@router.get('/api/docs', include_in_schema=False)
async def get_rapidoc() -> HTMLResponse:
    return get_rapidoc_html(
        openapi_url=router.openapi_url,
        title=f'{router.title} Docs'
    )
