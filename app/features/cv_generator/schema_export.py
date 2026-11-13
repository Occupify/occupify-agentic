"""Export the same argument schema Pydantic AI exposes, without initializing a model."""

import json

from app.features.cv_generator.schemas import GenerateCvInput

if __name__ == "__main__":
    print(json.dumps(GenerateCvInput.model_json_schema(), ensure_ascii=False, indent=2))
