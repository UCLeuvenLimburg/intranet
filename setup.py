from setuptools import setup


setup(name='intranet',
      version='0.1.0',
      description='Fetches intranet contents',
      url='http://github.com/UCLeuvenLimburg/intranet',
      author='Frederic Vogels',
      author_email='frederic.vogels@ucll.be',
      license='MIT',
      packages=['intranet'],
      entry_points = {
            'console_scripts': [ 'intranet=intranet.command_line:main']
      },
      install_requires=[
          'selenium'
      ],
      zip_safe=False)