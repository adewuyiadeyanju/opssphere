from uuid import uuid4

import pytest

from app.models.enums import SiteStatus, SiteType
from app.repository.site_repository import SiteRepository
from app.schemas.site import SiteCreate, SiteResponse
from app.services.site_service import SiteService


@pytest.fixture
def repository() -> SiteRepository:
    """Provides a fresh repository for each test."""
    return SiteRepository()


@pytest.fixture
def service(repository: SiteRepository) -> SiteService:
    """Provides a SiteService instance."""
    return SiteService(repository)


@pytest.fixture
def sample_site_create() -> SiteCreate:
    """Provides valid site creation data."""
    return SiteCreate(
        name="Test Site",
        country="Nigeria",
        site_type=SiteType.LAND,
        latitude=6.5244,
        longitude=3.3792,
    )


def test_create_site(service: SiteService, sample_site_create: SiteCreate):
    """Service should create a valid SiteResponse."""

    result = service.create_site(sample_site_create)

    assert isinstance(result, SiteResponse)

    # User input is preserved
    assert result.name == sample_site_create.name
    assert result.country == sample_site_create.country
    assert result.site_type == sample_site_create.site_type
    assert result.latitude == sample_site_create.latitude
    assert result.longitude == sample_site_create.longitude

    # Business rules
    assert result.status == SiteStatus.PLANNED
    assert result.id is not None
    assert result.created_at is not None


def test_get_all_sites(
    service: SiteService,
    sample_site_create: SiteCreate,
):
    """Service should return all created sites."""

    service.create_site(sample_site_create)

    second_site = SiteCreate(
        name="Second Site",
        country="Ghana",
        site_type=SiteType.LAND,
        latitude=5.6037,
        longitude=-0.1870,
    )

    service.create_site(second_site)

    sites = service.get_all_sites()

    assert len(sites) == 2


def test_get_site_by_id(
    service: SiteService,
    sample_site_create: SiteCreate,
):
    """Service should retrieve a site by ID."""

    created_site = service.create_site(sample_site_create)

    retrieved_site = service.get_site_by_id(created_site.id)

    assert retrieved_site == created_site


def test_get_unknown_site_returns_none(service: SiteService):
    """Unknown site IDs should return None."""

    result = service.get_site_by_id(uuid4())

    assert result is None


def test_create_site_persists_to_repository(
    service: SiteService,
    repository: SiteRepository,
    sample_site_create: SiteCreate,
):
    """Creating a site should persist it in the repository."""

    created_site = service.create_site(sample_site_create)

    stored_site = repository.get_by_id(created_site.id)

    assert stored_site == created_site
