from fastapi import FastAPI

router = FastAPI()


@router.get('/')
async def ping():
    return {"message": "hello from server!"}
