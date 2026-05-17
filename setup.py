from setuptools import setup, find_packages

setup(
    name="plainpaste",
    version="0.1.0",
    description="A cross-platform CLI tool to paste clipboard content as plain text.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Femirins",
    url="https://github.com/femirins/plainpaste",
    packages=find_packages(),
    install_requires=[
        "pyperclip>=1.8.2",
        "colorama>=0.4.4",
    ],
    entry_points={
        "console_scripts": [
            "plainpaste=plainpaste:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)