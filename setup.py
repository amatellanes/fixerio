import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('fixerio/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst') as f:
    readme = f.read()
with open('CHANGELOG.rst') as f:
    changelog = f.read()

requirements = ['requests==2.10.0']
test_requirements = ['coverage==4.1', 'flake8==2.5.5', 'httpretty==	0.8.14',
                     'nose==1.3.7', 'prospector==0.11.7', 'tox==2.3.1']

setup(
    name='fixerio',
    version=version,
    description='A Python client for Fixer.io',
    long_description=readme + '\n\n' + changelog,
    author="Adrian Matellanes",
    author_email='matellanesadrian@gmail.com',
    url='https://github.com/amatellanes/fixerio',
    install_requires=requirements,
    license='MIT License',
    packages=['fixerio'],
    package_dir={'fixerio': 'fixerio'},
    include_package_data=True,
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
    tests_require=test_requirements,
)
