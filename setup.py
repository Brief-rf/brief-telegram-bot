import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brief-telegram-bot",
    version="0.0.6",
    author="Brief",
    author_email="brf2053@gmail.com",
    description="Telegram bot in brief.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Brief-rf/brief-telegram-bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ]
)