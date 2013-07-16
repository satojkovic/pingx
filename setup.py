from setuptools import setup, find_packages

setup(
    name = "pingx",
    version = "1.0",
    description = "pingx is a command line tool to post a tweet with items provided on iTunes store.",
    author = "satojkovic",
    author_email = "satojkovic@gmail.com",
    url = "https://github.com/satojkovic/pingx",
    entry_points = {
        "console_scripts": [
            "pingx = pingx:main",
            ]
        },
    install_requires = [
        "python-itunes",
        "docopt",
        "pit",
        "python-twitter",
        "python-googl",
        ],
    )
