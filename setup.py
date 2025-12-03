from setuptools import find_packages, setup

__version__ = "0.0.3"

src = 'src/'
DESCRIPTION = 'Portfolio Optimization, CAPM, VaR, and Clustering'
URL = 'https://github.com/nickkats1/Portfolio'
EMAIL = 'katsarelas1@outlook.com' #or katsarelasnick3@gmail.com
AUTHOR = 'Nick'
REQUIRES_PYTHON = '>=3.6.0'










setup(
    name=src,
    version=__version__,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR}/{URL}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{URL}/issues",
    },
    package_dir={"": "src"},
)








