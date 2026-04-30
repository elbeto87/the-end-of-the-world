from fastapi import APIRouter

router = APIRouter(
    prefix="/asteroid",
    tags=["asteroid"],
)

@router.get("/")
def read_root():
    return {"Hello": "World"}
