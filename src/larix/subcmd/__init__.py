from pathlib import Path

def modules():
    pyfiles = Path(__file__).parent.glob('*.py')
    return [path.name[:-3] for path in pyfiles if path.is_file() and path != Path(__file__)]

__all__ = modules()

