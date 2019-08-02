from setuptools import setup, find_packages

def readme():
  with open('README.rst') as f:
    return f.read()

setup(name='beepy',
      version='1.0.8',
      description='Play notification sounds.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Topic :: Multimedia :: Sound/Audio',
      ],
      keywords='beep notification sound beepr beeper',
      url='https://github.com/prabeshdhakal/beepy/',
      author='Prabesh Dhakal',
      author_email='prabesh.official@gmail.com',
      license='MIT',
      packages=['beepy'],
      package_data={'beepy':['audio_data/*.wav']},
      python_requires='>=3.0',
      install_requires=['simpleaudio'],
      include_package_data=True,
      zip_safe=False)
