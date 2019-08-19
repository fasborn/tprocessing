from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name="tprocessing",
      version="0.0.3",
      packages=["tprocessing"],
      url="https://github.com/fasborn/tprocessing",
      author="Fasborn",
      long_description=README,
      long_description_content_type = "text/markdown")