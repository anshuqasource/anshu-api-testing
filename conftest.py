# conftest.py
import pytest
from dotenv import load_dotenv
import os
import playwright.sync_api as sync_api
from clients.reqres_client import ReqResClient

load_dotenv()

@pytest.fixture(scope="session")
def api_context():
    with sync_api.sync_playwright() as p:
        context = p.request.new_context(
            base_url=os.getenv("BASE_URL"),
            extra_http_headers={"x-api-key": os.getenv("REQRES_API_KEY")}
        )
        yield context
        context.dispose()

@pytest.fixture(scope="session")
def client(api_context):
    return ReqResClient(api_context)