from setuptools import setup, find_packages

setup(
    name='django-smokealarm',
    version='2012.11.21.1',
    description='Simple JavaScript error reporting.',
    long_description='Instructs client browsers to send JavaScript errors back to the server for analysis, alerting site admins as errors occur.',
    author='Brad Beattie',
    author_email='bradbeattie@gmail.com',
    url='https://github.com/bradbeattie/django-smokealarm',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    package_data = { '': ['README.rst'] },
    install_requires=['django'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
