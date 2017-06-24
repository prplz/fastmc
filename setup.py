from setuptools import setup

setup(
    name = 'fastmc',
    version = '1.8.0-alpha1',
    description = 'Fast Minecraft Protocol Parser/Writer',
    author = 'Florian Wesch',
    author_email = 'fw@dividuum.de',
    packages = ['fastmc', 'fastmc.proto'],
    license = 'BSD2',
    install_requires = ['requests', 'pycrypto', 'simplejson', 'gevent'],
    zip_safe = True,
)
