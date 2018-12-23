__title__ = 'pyb00st'
__version__ = '0.3'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  # pylint: disable=F0401,E0611

setup(name=__title__,
      version=__version__,
      description='Python for LEGO BOOST',
      url='https://github.com/JorgePe/pyb00st',
      author='Jorge Pereira',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['pyb00st'],
      zip_safe=False)
