# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyUfl(PythonPackage):
    """The Unified Form Language (UFL) is a domain specific language for
    declaration of finite element discretizations of variational forms. More
    precisely, it defines a flexible interface for choosing finite element
    spaces and defining expressions for weak forms in a notation close to
    mathematical notation."""

    homepage = "https://bitbucket.org/fenics-project/ufl"
    url = "https://bitbucket.org/fenics-project/ufl/downloads/ufl-2018.1.0.tar.gz"
    git = "https://bitbucket.org/fenics-project/ufl.git"

    version("master", branch="master")
    version("2018.1.0", sha256="ed191f5e0abfeb9922a68a6802f819e9cc6c50749472c01365319f66a5cfcbea")
    version("2017.2.0", sha256="45562fcd29ceb2f2e37c44bc2552b8e6c5d76409f73526096d2bcdb7078cf99c")
    version("2017.1.0", sha256="af87fa10f492660e8dd9f5c820c03529e017b80bf2002da54b8234c56b8dda8f")
    version("2016.2.0", sha256="be2e165fc13d079c5d98c8864e8c774b68a336fa5a97433993575866c715fa1e")
    version("2016.1.0", sha256="8dccfe10d1251ba48a4d43a4c6c89abe076390223b500f4baf06f696294b8dd0")

    depends_on("py-setuptools", type="build")
