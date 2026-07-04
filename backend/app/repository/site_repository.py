from uuid import UUID

from app.schemas.site import SiteResponse


class SiteRepository:

    def __init__(self):
        self._sites: dict[UUID, SiteResponse] = {}

    def add(self, site: SiteResponse) -> SiteResponse:
        """Adds a new site to the repository."""
        self._sites[site.id] = site
        return site

    def get_all(self) -> list[SiteResponse]:
        """Returns a list of all sites in the repository."""
        return list(self._sites.values())

    def get_by_id(self, site_id: UUID) -> SiteResponse | None:
        """Returns a site by its ID, or None if it doesn't exist."""
        return self._sites.get(site_id)
