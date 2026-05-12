from setuptools import find_packages, setup


setup(
    name="capitalbench",
    version="0.1.0",
    description="Offline, time-resolved LLM evaluation for one-month market allocation decisions.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Ishtiaq Rahman",
    url="https://github.com/ishtiaqrahman/capitalbench",
    project_urls={
        "Repository": "https://github.com/ishtiaqrahman/capitalbench",
        "Issues": "https://github.com/ishtiaqrahman/capitalbench/issues",
    },
    license="Apache-2.0",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "pydantic>=2,<3",
        "PyYAML>=6",
    ],
    extras_require={
        "test": ["pytest>=8"],
        "web-sync": ["supabase>=2,<3"],
    },
    entry_points={
        "console_scripts": [
            "capitalbench=capitalbench.cli:main",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
