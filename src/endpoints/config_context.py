import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture
def api_request_context(playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
  request_context = playwright.request.new_context(
      base_url="http://127.0.0.1:5000"
  )
  yield request_context
  request_context.dispose()