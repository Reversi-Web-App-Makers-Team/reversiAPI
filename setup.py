from setuptools import setup, find_packages

try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements
setup(
    name='reversiAPI',
    version='1.0.11',
    url='https://github.com/reversiWebApp/reversiAPI.git',
    license='Free',
    author='Kosei Teramoto',
    author_email='kogupi93@gmail.com',
    description='you can play reversi game with this package',
    install_requires=['setuptools', 'numpy', 'toml', 'torch'],
    packages=find_packages(),
    include_package_data=True
)
