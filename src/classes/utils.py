from datetime import datetime


def generate_unique_filename() -> str:
    return datetime.now().isoformat()