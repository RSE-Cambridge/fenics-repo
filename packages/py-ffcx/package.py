# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFfcx(PythonPackage):
    """Next generation FEniCS Form Compiler"""

    homepage = "https://github.com/FEniCS/ffcx"
    git = "https://github.com/FEniCS/ffcx.git"

    version("2019-nov", commit="d56bbab95fa0b4fc04f84e2259ab8570ea7fdd34")
    version("2019-jun", commit="d093bf83")
    version("2019-may", commit="f2e2dd3d1604c9528e343122bfd36c2d0ca51e13")
    version("2019-apr", commit="f2e2dd3d1604c9528e343122bfd36c2d0ca51e13")
    version("2019-mar", commit="492d4f1a89f732c0100f6f652454c2e60992e303")
    version("2019-feb", commit="8337f39d19588cb445a1838a63836ebf35438213")

    depends_on("py-setuptools")
    depends_on("py-cffi")
    depends_on("py-ufl@master")
    depends_on("py-fiat@master")
    depends_on("py-numpy")
