from setuptools import setup, find_packages

setup(
      name='liapi',
      packages=['liapi'],
      install_requires=["requests"],
      description='Python wrapper for lichess api',
      author='Axeltherabbit',
      author_email='backb0x@hotmail.com',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
                  ],
      keywords = ['wrapper', 'lichess', 'api','chess'],
      url = 'https://github.com/Axeltherabbit/liapi/',
      
      version='1.0'
)
