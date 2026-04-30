from fastapi import APIRouter

router = APIRouter(
    tags=["asteroid"],
)

@router.get("")
def get_all_asteroids() -> dict:
    return {"Hello": "World"}
