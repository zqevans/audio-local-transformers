import setuptools

setuptools.setup(
    name="audio-local-transformers",
    version="0.1.0",
    author="Zach Evans",
    author_email="zqevans@gmail.com",
    description="Audio autoencoders using local attention",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zqevans/audio-local-transformers",
    packages=setuptools.find_packages(),
    install_requires=[
        "einops",
        "torch",
        "x-transformers",
        "local-attention"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)