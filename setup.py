import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="module_exports",
    version="1.1.0",
    author="Roman Shemyakin",
    author_email="ramon93i7@gmail.com",
    description="One decorator to export them __all__ :)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ramon93i7/module_exports",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
