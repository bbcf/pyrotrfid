from distutils.core import setup

setup(
        name             = 'pyrotrfid',
        version          = '1.0.0',
        description      = 'Digital TRFLP with pyrosequencing reads',
        long_description = open('README.txt').read(),
        license          = 'GNU General Public License 3.0',
        url              = 'http://bbcf.epfl.ch/PyroTRF-ID/',
        author           = 'Lucas Sinclair, Gregory Lefebvre, EPFL-BBCF',
        author_email     = 'webmaster.bbcf@epfl.ch',
        classifiers      = ['Topic :: Scientific/Engineering :: Bio-Informatics'],
        install_requires = ['scipy', 'matplotlib', 'biopython', 'pysam'],
        packages         = ['pyrotrfid'],
        scripts          = ['pyrotrfid/pyrotrfid'],
    )
