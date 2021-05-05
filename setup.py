#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'rabies'
DESCRIPTION = 'RABIES: Rodent Automated Bold Improvement of EPI Sequences.'
URL = 'https://github.com/CoBrALab/RABIES'
EMAIL = 'contact@cobralab.ca'
AUTHOR = 'CoBrALab'
REQUIRES_PYTHON = '>=3.6.0'

# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
    'matplotlib>=3.1.1',
    'nibabel>=2.3.1',
    'nilearn>=0.4.2',
    'nipype>=1.1.4',
    'numpy>=1.16.2',
    'pandas',
    'pybids',
    'scikit-learn>=0.20.0',
    'scipy',
    'simpleitk>=2.0.2',
    # from twolevel_dbm
    'tqdm',
    'pathos',
    'qbatch',
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
with open(os.path.join(here, project_slug, '__version__.py')) as f:
    exec(f.read(), about)

VERSION = about['__version__']
DOWNLOAD_URL = (
    '{url}/archive/{ver}.tar.gz'.format(
        url=URL, ver=VERSION))


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        #self.status('Pushing git tags…')
        #os.system('git tag v{0}'.format(about['__version__']))
        #os.system('git push --tags')

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='LICENSE',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Science/Research',
        'License :: Free for non-commercial use',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
    scripts=[
        'scripts/rabies',
        'scripts/gen_DSURQE_masks.py',
        'scripts/install_DSURQE.sh',
        'scripts/preprocess_scripts/ants_dbm.sh',
        'scripts/preprocess_scripts/heavy_SyN_registration.sh',
        'scripts/preprocess_scripts/light_SyN_registration.sh',
        'scripts/preprocess_scripts/multiRAT_registration.sh',
        'scripts/preprocess_scripts/null_nonlin.sh',
        'scripts/preprocess_scripts/plot_overlap.sh',
        'scripts/preprocess_scripts/rabies_antsMultivariateTemplateConstruction2.sh',
        'scripts/preprocess_scripts/rabies-mouse-preprocessing-v5.sh',
        'twolevel_ants_dbm/twolevel_dbm.py',
        'minc-toolkit-extras/ants_generate_iterations.py',
        'minc-toolkit-extras/antsRegistration_affine_SyN.sh',
        ]
)
