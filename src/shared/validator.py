from pathlib import Path


def validate_input(input_path: str) -> Path:
    path = Path(input_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file does not exist: {path}")

    if not path.is_file():
        raise ValueError(f"Input path is not a file: {path}")

    if path.suffix.lower() not in {".csv", ".json"}:
        raise ValueError(
            f"Unsupported input format: {path.suffix}. "
            "Expected .csv or .json"
        )
    return path

def validate_output(output_folder: str) -> Path:
    path = Path(output_folder)

    if not path.exists():
        raise FileNotFoundError(
            f"Destination folder does not exist: {path}"
        )

    if not path.is_dir():
        raise ValueError(
            f"Destination path is not a directory: {path}"
        )

    return path

