# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Dolfinx(CMakePackage):
    """Next generation FEniCS problem solving environment"""

    homepage = "https://github.com/FEniCS/dolfinx"
    url = "https://github.com/FEniCS/dolfinx"
    git = "https://github.com/FEniCS/dolfinx.git"

    submodules = True

    version("2019-may", commit="85efe3eed55d2cf92668a4a17c364a0cd9489791")
    version("2019-apr", commit="c4c208651d2ad37aa983e10a1b58d5a77b1106a9")
    version("2019-mar", commit="3fd0d56")
    version("2019-feb", commit="84ba31dc2401caf46d99f139944d6cec9c07eedf")

    extends("python")

    variant("doc", default=False, description="Builds the documentation")

    depends_on("mpi")
    depends_on("hdf5+hl+fortran")
    depends_on("petsc+mpi+shared+hypre+metis~superlu-dist@develop")
    depends_on("py-numpy")
    depends_on("py-sympy")
    depends_on("py-ffcx")
    depends_on("py-fiat@master")
    depends_on("py-dijitso@master")
    depends_on("py-ufl@master")
    depends_on("scotch+mpi~metis")
    depends_on("python@3.5:")
    depends_on("py-sphinx@1.0.1:", when="+doc", type="build")
    depends_on("eigen~fftw~metis~mpfr~scotch~suitesparse@3.2.0:")
    depends_on("metis")
    depends_on("boost")

    depends_on("swig@3.0.3:", type=("build", "run"))
    depends_on("cmake@2.8.12:", type="build")

    root_cmakelists_dir = "cpp"

    def cmake_args(self):
        mpi = self.spec["mpi"]
        return [
            "-DDOLFIN_SKIP_BUILD_TESTS=True",
            "-DMPI_C_COMPILER=%s" % mpi.mpicc,
            "-DMPI_CXX_COMPILER=%s" % mpi.mpicxx,
        ]

    @run_after("install")
    def python_install(self):
        with working_dir("python"):
            which("pip")("install", ".")
