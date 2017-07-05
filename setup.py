import distutils
import glob
import importlib
import os
import sys

import setuptools.dist

# Recipe needed to get real distutils if virtualenv.
# Error message is "ImportError: cannot import name dist"
# when running app.
# See http://sourceforge.net/p/py2exe/mailman/attachment/47C45804.9030206@free.fr/1/
#
if hasattr(sys, 'real_prefix'):
    # Running from a virtualenv
    assert hasattr(distutils, 'distutils_path'), \
        "Can't get real distutils path"
    libdir = os.path.dirname(distutils.distutils_path)
    sys.path.insert(0, libdir)
    #
    # Get the system "site" package, not the virtualenv one. This prevents
    # site.virtual_install_main_packages from being called, resulting in
    # "IOError: [Errno 2] No such file or directory: 'orig-prefix.txt'
    #
    del sys.modules["site"]
    import site

    assert not hasattr(site, "virtual_install_main_packages")

# We need some packages in order to properly prepare for setup, but
# setuptools.dist.Distribution seems to upgrade them willy-nilly
# So try importing and only ask for ones that are not present.
packages = []
for package_name, import_name in [
    ("clint", "clint"),
    ("javabridge", "javabridge"),
    ("matplotlib", "matplotlib"),
    ("numpy", "numpy"),
    ("pytest", "pytest"),
    ("pyzmq", "zmq"),
    ("requests", "requests"),
    ("scipy", "scipy")]:
    try:
        importlib.import_module(import_name)
    except ImportError:
        packages.append(package_name)

setuptools.dist.Distribution({
    "setup_requires": packages
})

try:
    import matplotlib
    import scipy.sparse.csgraph._validation
    import scipy.linalg
    import zmq  # for proper discovery of its libraries by distutils
    import zmq.libzmq
except ImportError:
    pass


class Test(setuptools.Command):
    user_options = [
        ("pytest-args=", "a", "arguments to pass to py.test")
    ]

    def initialize_options(self):
        self.pytest_args = []

    def finalize_options(self):
        pass

    def run(self):
        try:
            import pytest
            import unittest
        except ImportError:
            raise ImportError

        import cellprofiler.utilities.cpjvm

        #
        # Monkey-patch pytest.Function
        # See https://github.com/pytest-dev/pytest/issues/1169
        #
        try:
            from _pytest.unittest import TestCaseFunction

            def runtest(self):
                setattr(self._testcase, "__name__", self.name)
                self._testcase(result=self)

            TestCaseFunction.runtest = runtest
        except:
            pass

        cellprofiler.preferences.set_headless()

        cellprofiler.utilities.cpjvm.cp_start_vm()

        errno = pytest.main(self.pytest_args)

        cellprofiler.__main__.stop_cellprofiler()

        sys.exit(errno)


version = "3.0.0"

setuptools.setup(
        app=[
            "CellProfiler.py"
        ],
        author="cellprofiler-dev",
        author_email="cellprofiler-dev@broadinstitute.org",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Topic :: Scientific/Engineering :: Bio-Informatics",
            "Topic :: Scientific/Engineering :: Image Recognition",
            "Topic :: Scientific/Engineering"
        ],
        cmdclass={
            "test": Test
        },
        console=[
            {
                "icon_resources": [
                    (1, "artwork/CellProfilerIcon.ico")
                ],
                "script": "CellProfiler.py"
            }
        ],
        description="",
        entry_points={
            "console_scripts": [
                "cellprofiler=cellprofiler.__main__:main"
            ]
        },
        include_package_data=True,
        install_requires=[
            "cellh5",
            "centrosome",
            "h5py",
            "inflect",
            "javabridge",
            "joblib",
            "libtiff",
            "mahotas",
            "matplotlib",
            "MySQL-python",
            "numpy",
            "prokaryote>=1.0.11",
            "pyamg==3.1.1",
            "pytest",
            "python-bioformats",
            "pyzmq",
            "raven",
            "requests",
            "scikit-image",
            "scikit-learn",
            "scipy"
        ],
        keywords="",
        license="BSD",
        long_description="",
        name="CellProfiler",
        package_data={
            "artwork": glob.glob(os.path.join("artwork", "*"))
        },
        packages=setuptools.find_packages(exclude=[
            "*.tests",
            "*.tests.*",
            "tests.*",
            "tests",
            "tutorial"
        ]) + ["artwork"],
        setup_requires=[
            "pytest"
        ],
        url="https://github.com/CellProfiler/CellProfiler",
        version="3.0.0rc1"
)
