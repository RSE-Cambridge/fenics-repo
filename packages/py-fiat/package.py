# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFiat(PythonPackage):
    """The FInite element Automatic Tabulator FIAT supports generation of
    arbitrary order instances of the Lagrange elements on lines, triangles, and
    tetrahedra. It is also capable of generating arbitrary order instances of
    Jacobi-type quadrature rules on the same element shapes. Further, H(div)
    and H(curl) conforming finite element spaces such as the families of
    Raviart-Thomas, Brezzi-Douglas-Marini and Nedelec are supported on
    triangles and tetrahedra. Upcoming versions will also support Hermite and
    nonconforming elements"""

    homepage = "https://bitbucket.org/fenics-project/fiat"
    url = "https://bitbucket.org/fenics-project/fiat/downloads/fiat-2018.1.0.tar.gz"
    git = "https://bitbucket.org/fenics-project/fiat.git"

    version("master", branch="master")
    version("2018.1.0", sha256="3d897d99fdc94441f9c8720fb5a3bcaf8a0b9ede897a0600cb1f329dacec5c92")
    version("2017.2.0", sha256="abf4bfae6ab67601ab49e6df1ee3664c19c36f18467720706ec9e62d4c75837c")
    version("2017.1.0", sha256="d4288401ad16c4598720f9db0810a522f7f0eadad35d8211bac7120bce5fde94")
    version("2016.2.0", sha256="812ecf100211bc680e74b9b6546a356efd8be26a492f500cab975e5fa8d64d5d")
