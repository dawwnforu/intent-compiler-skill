"""Image-input wiring for local evaluations; not a Skill runtime requirement."""
from pathlib import Path


def image_arguments(workspace, references, *, required=False):
    """Preserve declared reference order; never silently drop a required file."""
    if required and not references:
        raise ValueError("Required visual references were not supplied")
    root = Path(workspace).resolve()
    arguments = []
    for reference in references:
        path = (root / reference).resolve()
        if not path.is_relative_to(root):
            raise ValueError(f"Reference leaves evaluation workspace: {reference}")
        if not path.is_file() or path.stat().st_size == 0:
            raise ValueError(f"Missing or empty visual reference: {reference}")
        arguments.extend(["--image", str(path)])
    return arguments
