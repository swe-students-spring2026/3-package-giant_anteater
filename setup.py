from setuptools import setup, find_packages

setup(
    name="addition_tutor",
    version="0.1.1",
    author="GIANT_ANTEATER",
    author_email="you@example.com",
    description="A Python package to teach step-by-step long integer addition",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)