# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFfcx(PythonPackage):
    """Next generation FEniCS Form Compiler"""

    homepage = "https://github.com/FEniCS/ffcx"
    git = "https://github.com/FEniCS/ffcx.git"

    version("2019-mar", commit="492d4f1a89f732c0100f6f652454c2e60992e303")
    version("2019-feb", commit="8337f39d19588cb445a1838a63836ebf35438213")

    depends_on("py-setuptools", type="build")
    depends_on("py-cffi")
