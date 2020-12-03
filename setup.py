from setuptools import find_namespace_packages, setup

setup(
    name="my_package",
    version="0.1.0",
    packages=find_namespace_packages(),
    entry_points=dict(console_scripts=["woo=scripts.my_script:main"]),
)
