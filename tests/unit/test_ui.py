import pytest
from httpx import ASGITransport, AsyncClient

from app.core.config import get_settings
from app.main import app


@pytest.mark.asyncio
async def test_ui_serves_page_and_assets(client):
    res_html = await client.get("/ui")
    assert res_html.status_code == 200
    html_text = res_html.text
    for elem_id in ["session-list", "chat-messages", "chat-form", "log-panel"]:
        assert f'id="{elem_id}"' in html_text or f"id='{elem_id}'" in html_text

    res_js = await client.get("/ui/app.js")
    assert res_js.status_code == 200

    res_css = await client.get("/ui/styles.css")
    assert res_css.status_code == 200


@pytest.mark.asyncio
async def test_ui_404_in_production(monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    get_settings.cache_clear()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as prod_client:
        res = await prod_client.get("/ui")
        assert res.status_code == 404

    monkeypatch.undo()
    get_settings.cache_clear()
