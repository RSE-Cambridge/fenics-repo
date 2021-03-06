# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class FenicsPerformanceTest(CMakePackage):
    """performance tests for fenics"""

    homepage = "https://github.com/FEniCS/performance-test"
    git = "https://github.com/FEniCS/performance-test.git"

    version("2019-nov", commit="d60c2265514a85e11164da4fbf80667a2236e98f")
    version("2019-jun", commit="67b599f")
    version("2019-may", commit="40c70e62d089595a646ed0487f5374dbd87babef")
    version("2019-apr", commit="37c7777ca986d0eb88d84974b77c76b38d257bf6")
    version("2019-mar", commit="386b8fc")
    version("2019-feb", commit="354b12806b81d2a25ea14c2e48cb763fcd6e64e5")


    depends_on("py-ffcx")
    depends_on("dolfinx")
    depends_on("boost+program_options")

    @run_before("cmake")
    def compile_forms(self):
        ffc = which("ffc", path=self.spec["py-ffcx"].prefix.bin)
        with working_dir("src"):
            ffc("Elasticity.ufl")
            ffc("Poisson.ufl")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path("..", "spack-build", "dolfin-scaling-test"), prefix.bin)

    root_cmakelists_dir = "src"

    def cmake_args(self):
        mpi = self.spec["mpi"]
        return ["-DMPI_C_COMPILER=%s" % mpi.mpicc, "-DMPI_CXX_COMPILER=%s" % mpi.mpicxx]
