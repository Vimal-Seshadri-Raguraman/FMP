from setuptools import setup, find_packages

setup(
    name="fmp-client",
    version="1.0.0",
    description="Python client library for the Financial Modeling Prep API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vimal Seshadri Raguraman",
    url="https://github.com/Vimal-Seshadri-Raguraman/FMP",  # Replace with your repository URL
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
