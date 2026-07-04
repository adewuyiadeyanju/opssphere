from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.repository.site_repository import SiteRepository
from app.schemas.site import SiteCreate, SiteResponse
from app.services.site_service import SiteService

router = APIRouter()

# Temporary singleton instances for the MVP
repository = SiteRepository()
service = SiteService(repository)


@router.post("/", response_model=SiteResponse, status_code=201)
def create_site(site: SiteCreate):
    return service.create_site(site)


@router.get("/", response_model=list[SiteResponse])
def get_sites():
    return service.get_all_sites()

@router.get("/{site_id}", response_model=SiteResponse)
def get_site(site_id: UUID):

    site = service.get_site_by_id(site_id)

    if site is None:
        raise HTTPException(
            status_code=404,
            detail="Site not found"
        )

    return site
