import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    dependencies = fh.read()

setuptools.setup(
    name="helloworld",
    version="0.1",
    packages=setuptools.find_packages(),
    install_requires=dependencies,
    author="Foo Bar",
    author_email="foobar@example.com",
    description="An example of how to create a Python package",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="python example",
    url="https://github.com/Julian-Nash/python-package-guide",
    project_urls={
        "Bug Tracker": "https://github.com/Julian-Nash/python-package-guide",
        "Documentation": "https://github.com/Julian-Nash/python-package-guide",
        "Source Code": "https://github.com/Julian-Nash/python-package-guide",
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)