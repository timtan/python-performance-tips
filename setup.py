__author__ = 'tim'
import sys
if sys.argv[-1] == 'cython':
    sys.argv.pop()
    print 'cython'
    from distutils.core import setup
    #from setuptools import find_packages
    from Cython.Distutils import Extension, build_ext

else:
    from setuptools import setup
    from Cython.Distutils import Extension, build_ext
    #from setuptools import find_packages


ext_modules = [
    Extension(
        name='cython_sample',
        sources=['cython_sample.pyx'],
    )
]

setup(
    name = 'performance_samples',
    install_requires = [
        'Cython', 'gevent',
        ],
    version = 1.0,
    description = "samples about performance",
    author = 'wen chang',
    author_email = 'tim.yellow@gmailc.om',
    py_modules= ['profile_sample1', 'profile_sample2', 'cython_sample'],
    entry_points = {
        'console_scripts': [
            "profile_sample1 = profile_sample1:main",
            "cython_sample = cython_sample:main",

            ],
        },
    package_data = {},
    cmdclass = {'build_ext': build_ext },
    ext_modules = ext_modules,
)
