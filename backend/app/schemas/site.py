from pydantic import BaseModel, Field
from app.models.enums import SiteType
from uuid import UUID
from datetime import datetime
from typing import Optional

class SiteCreate(BaseModel):
    """
    Schema used when creating a new Site.
    """

    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Name of the operational site"
    )

    country: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Country where the site is located"
    )

    site_type: SiteType = Field(
        ...,
        description="Type of site (Land, Deepwater, Swamp, etc.)"
    )

    latitude: float = Field(
        ...,
        ge=-90,
        le=90,
        description="Latitude coordinate"
    )

    longitude: float = Field(
        ...,
        ge=-180,
        le=180,
        description="Longitude coordinate"
    )


class SiteResponse(BaseModel):

    id: UUID

    name: str

    country: str

    site_type: SiteType

    latitude: float

    longitude: float

    status: str

    created_at: datetime


class SiteUpdate(BaseModel):
    """
    Schema used when updating an existing Site.
    """

    name: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=100
    )

    country: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    site_type: Optional[SiteType] = None

    latitude: Optional[float] = Field(
        default=None,
        ge=-90,
        le=90
    )

    longitude: Optional[float] = Field(
        default=None,
        ge=-180,
        le=180
    )
