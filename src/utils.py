from pathlib import Path

def path(*parts):
    return Path(__file__).resolve().parent.parent.joinpath(*parts)