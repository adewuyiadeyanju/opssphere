from uuid import uuid4
from datetime import datetime, UTC
import pytest

from app.repository.site_repository import SiteRepository
from app.schemas.site import SiteResponse
from app.models.enums import SiteType, SiteStatus

@pytest.fixture
def repository() -> SiteRepository:
    """Provides a fresh, empty repository instance for each test."""
    return SiteRepository()

@pytest.fixture
def mock_site() -> SiteResponse:
    """Provides a mock SiteResponse data object for testing."""
    return SiteResponse(
        id=uuid4(),
        name="Test Location",
        country="Test Country",
        site_type=SiteType.LAND,
        status=SiteStatus.PLANNED,
        latitude=-90,
        longitude=-180,
        created_at=datetime.now(UTC)
    )


def test_new_repository_starts_empty(repository: SiteRepository):
    """New repository starts empty"""
    assert len(repository.get_all()) == 0

def test_add_site(repository: SiteRepository, mock_site: SiteResponse):
    """Add a site"""
    saved_site = repository.add(mock_site)
    assert saved_site == mock_site
    sites = repository.get_all()
    assert sites[0] == mock_site

def test_retrieve_all_sites(repository: SiteRepository, mock_site: SiteResponse):
    """Retrieve all sites"""
    second_site = SiteResponse(
        id=uuid4(),
        name="Second Location",
        country="Another Country",
        site_type=SiteType.LAND,
        status=SiteStatus.PLANNED,
        latitude=-90,
        longitude=-180,
        created_at=datetime.now(UTC)
    )
   
    repository.add(mock_site)
    repository.add(second_site)
    
    all_sites = repository.get_all()
    assert len(all_sites) == 2
    assert mock_site in all_sites
    assert second_site in all_sites


def test_retrieve_site_by_valid_id(repository: SiteRepository, mock_site: SiteResponse):
    """Retrieve site by valid ID"""
    repository.add(mock_site)
    
    found_site = repository.get_by_id(mock_site.id)
    assert found_site == mock_site


def test_retrieve_site_by_invalid_id_returns_none(repository: SiteRepository):
    """Retrieve site by invalid ID returns None"""
    random_id = uuid4()
    
    found_site = repository.get_by_id(random_id)
    assert found_site is None
