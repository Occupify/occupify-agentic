from app.features.cv_generator.schemas import ArtifactFile, GenerateCvInput
from app.features.cv_generator.service import CvGeneratorService
from tests.unit.cv_generator.helpers import make_pdf, sample_payload


class Compiler:
    def __init__(self, pages=1):
        self.pages = pages

    async def compile(self, tex):
        assert "[YOUR NAME]" in tex
        return make_pdf(self.pages)


class Storage:
    def __init__(self):
        self.objects = []

    async def publish(self, artifact_id, owner_id, tex, pdf):
        self.objects.append((owner_id, tex, pdf))
        return [
            ArtifactFile(
                format=fmt,
                filename=f"cv.{fmt}",
                content_type=ctype,
                download_url=f"https://example.invalid/{fmt}",
                expires_at="2026-11-13T00:00:00Z",
            )
            for fmt, ctype in [
                ("tex", "application/x-tex; charset=utf-8"),
                ("pdf", "application/pdf"),
            ]
        ]


async def test_service_returns_links_only_after_checked_pdf_and_paired_upload():
    storage = Storage()
    result = await CvGeneratorService(Compiler(2), storage).generate(
        GenerateCvInput.model_validate(sample_payload()), "owner"
    )
    assert result.status == "succeeded" and result.page_count == 2
    assert len(result.files) == 2 and result.error is None
    assert result.warnings == ["PERSONAL_DETAILS_ARE_PLACEHOLDERS"]
    assert storage.objects[0][0] == "owner"


async def test_three_pages_does_not_publish_any_file():
    storage = Storage()
    result = await CvGeneratorService(Compiler(3), storage).generate(
        GenerateCvInput.model_validate(sample_payload()), "owner"
    )
    assert result.status == "failed" and result.error.code == "CONTENT_TOO_LONG"
    assert not result.files and not storage.objects
