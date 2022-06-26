import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Base Application
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

# Bind Frontend UI
if 'WEB_ROOT' not in os.environ:
    os.environ['WEB_ROOT'] = os.path.join(os.path.dirname(__file__), 'http', 'web-app', 'dist')

router.mount('/', StaticFiles(directory=os.getenv('WEB_ROOT'), check_dir=True, html=True))
