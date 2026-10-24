import pytest


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
