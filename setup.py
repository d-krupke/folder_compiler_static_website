import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="folder_compiler_static_website",
    version="0.1.1",
    author="Dominik Krupke",
    author_email="krupked@gmail.com",
    description="A simple util for 'compiling' a folder, e.g. to a static website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/d-krupke/folder_compiler_static_website",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["folder-compiler", "jinja2", "markdown2", "bibtexparser"],
    python_requires='>=3.6',
)
