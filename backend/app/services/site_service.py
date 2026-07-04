from uuid import UUID, uuid4
from datetime import datetime, UTC

from app.repository.site_repository import SiteRepository
from app.schemas.site import SiteCreate, SiteResponse


class SiteService:

    def __init__(self, repository: SiteRepository):
        self.repository = repository

    def create_site(self, site_data: SiteCreate) -> SiteResponse:
        """Applies business rules, creates a new site, and saves it."""
        # Create the response object combining user input and system defaults
        new_site = SiteResponse(
            id=uuid4(),
            status="Planned",
            created_at=datetime.now(UTC),
            **site_data.model_dump()  # Assumes Pydantic v2; use .dict() for v1
        )
        return self.repository.add(new_site)

    def get_all_sites(self) -> list[SiteResponse]:
        """Retrieves all existing sites."""
        return self.repository.get_all()

    def get_site_by_id(self, site_id: UUID) -> SiteResponse | None:
        """Retrieves a single site by its unique ID."""
        return self.repository.get_by_id(site_id)
