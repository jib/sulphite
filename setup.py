from setuptools import setup, find_packages

setup(
    name             = 'sulphite',
    version          = "1.0.0",
    description      = 'Library & Eventlistener for Supervisord to send events to Graphite',
    author           = 'Jos Boumans',
    author_email     = 'jos@dwim.org',
    url              = 'https://github.com/jib/sulphite',
    packages         = find_packages(),
    install_requires = [ 'supervisor', ],
    entry_points     = {
        'console_scripts': [ 'sulphite = sulphite.cli:main' ]
    },
)
