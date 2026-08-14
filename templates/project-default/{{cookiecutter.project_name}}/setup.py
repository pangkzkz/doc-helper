import setuptools

setuptools.setup(
    name="{{ cookiecutter.project_name }}",
    version="0.0.1",
    author="{{ cookiecutter.ptl }}",
    description="Project {{ cookiecutter.project_name }}",
    long_description="Project {{ cookiecutter.project_name }}",
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "dochelper",
    ],
)
