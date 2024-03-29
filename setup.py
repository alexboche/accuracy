import re
import pathlib

import setuptools

PROJECT_DIR = pathlib.Path(__file__).parent

with open(PROJECT_DIR / "requirements.in") as f:
    INSTALL_REQUIRES = f.read().splitlines()


setuptools.setup(
    name="accuracy",
    version="0.0.1",
    description="Shell pipes for Python.",
    long_description=open(PROJECT_DIR / "README.rst").read(),
    long_description_content_type="text/x-rst",
    author="author name",
    author_email="author@example.com",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/author/accuracy",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires=">=3.4",
    install_requires=INSTALL_REQUIRES,
    entry_points={
        "console_scripts": [
            "accuracy_console_script = accuracy.cli:cli",
        ],
    },
)
