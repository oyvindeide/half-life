from setuptools import setup, find_packages

setup(
    name="half_life",
    entry_points={
        "console_scripts": [
            "half-life=half_life.cli.main:main",
        ]
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pandas", "matplotlib"],
)
