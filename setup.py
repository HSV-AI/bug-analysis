import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bug-analysis", # Replace with your own username
    version="0.0.1",
    author="J. Langley",
    author_email="jameselangley@gmail.com",
    description="Model that provides textual analysis of Bugzilla Bugs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HSV-AI/bug-analysis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Eclipse Public License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    data_files=[('data',['data/bugzilla.doc2vec'])],
)
