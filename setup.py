from setuptools import setup, find_packages

setup(
    name="FMP",
    version="0.0.1",
    description="Python client library for the Financial Modeling Prep API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vimal Seshadri Raguraman",
    url="https://github.com/Vimal-Seshadri-Raguraman/FMP",
    packages=find_packages(),
    install_requires=[
        "requests",
        "ratelimit",
        "websockets",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
