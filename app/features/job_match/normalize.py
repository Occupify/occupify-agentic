import re
import unicodedata


def remove_accents(text: str) -> str:
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def normalize_skill_name(name: str) -> str:
    """
    Normalises a skill name for rule-based comparison:
    - Lowercase, trim whitespace, strip diacritics/accents
    - Standardises common framework aliases and suffixes (.js, js)
    """
    cleaned = remove_accents(name.strip().lower())

    # Replace punctuation
    cleaned = re.sub(r"[\s\-_.]+", " ", cleaned).strip()

    # Canonical aliases mapping
    aliases: dict[str, str] = {
        "react js": "react",
        "reactjs": "react",
        "react": "react",
        "node js": "node",
        "nodejs": "node",
        "node": "node",
        "postgresql": "postgres",
        "postgres": "postgres",
        "tailwind css": "tailwind",
        "tailwindcss": "tailwind",
        "tailwind": "tailwind",
        "ts": "typescript",
        "typescript": "typescript",
        "js": "javascript",
        "javascript": "javascript",
        "next js": "next",
        "nextjs": "next",
        "next": "next",
        "vue js": "vue",
        "vuejs": "vue",
        "vue": "vue",
        "golang": "go",
        "go": "go",
    }

    if cleaned in aliases:
        return aliases[cleaned]

    # Remove trailing 'js' or '.js' if present on generic word
    if cleaned.endswith(" js"):
        cleaned = cleaned[:-3]
    elif cleaned.endswith("js") and len(cleaned) > 4:
        cleaned = cleaned[:-2]

    return cleaned.strip()
