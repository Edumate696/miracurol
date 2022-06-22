from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

router = FastAPI()

# CORS (Cross-Origin Resource Sharing)
origins = [
    '*',
]

router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Front End
router.mount('/', StaticFiles(directory='www/dist/www', html=True), name='static')
