from typing import List
from sys import executable, platform
from subprocess import check_call

dependencies = [
    'jupyter',
    'transformers',
    'pandas',
    'numpy',
    'alive-progress'
]

darwin_dependencies = [
    'tensorflow-macos',
    'tensorflow-metal'
]


def install_deps(deps: List[str]) -> None:
    for dependency in deps:
        check_call([executable, "-m", "pip", "install", dependency])


if __name__ == "__main__":
    check_call([executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])
    install_deps(dependencies)
    if platform == 'darwin':
        install_deps(darwin_dependencies)
