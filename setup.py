import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qrcode",
    version="1.0.0",
    author="",
    author_email="",
    description="artistic QR Code in Python （Animated GIF qr code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Simplici/qrcode",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)