from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_sites():
    return {
        "message": "List of sites"
    }


@router.post("/")
def create_site():
    return {
        "message": "Site created"
    }
