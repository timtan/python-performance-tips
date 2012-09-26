__author__ = 'tim'
from setuptools import  setup, find_packages
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [Extension(sources=['profile_sample1.py'], name='profile_sample1')]

setup(
    name = 'performance_samples',
    install_requires = [
        'Cython',
        ],
    version = 1.0,
    description = "samples about performance",
    author = 'wen chang',
    author_email = 'tim.yellow@gmailc.om',
    packages = find_packages(),
    py_modules= ['profile_sample1', 'profile_sample2'],
    entry_points = {
        'console_scripts': [
            "profile_sample1 = profile_sample1:main",
            "profile_sample1clone = profile_sample1clone:main",
            ],
        },
    package_data = {},
    cmdclass = {'build_ext': build_ext },
    ext_modules = ext_modules,
)
