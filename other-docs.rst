Other policy documents
======================

Gentoo-specific documentation
-----------------------------

Package Manager Specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PMS_ provides the specification of ebuild format, as well as general
guidelines for implementing package managers.  All ebuilds in the Gentoo
repository are required to conform to the PMS.  Tree policies may
enforce additional restrictions upon the format discussed in PMS.

PMS is maintained by the `PMS project`_.  All major changes are done
in subsequent EAPIs that are approved by the Council.  The project's
wiki page discusses how PMS can be changed via `future EAPI process`_.

GLEPs
~~~~~
GLEPs_ provide the highest level policies applicable to Gentoo.  Final
or active GLEPs apply to all developers.  Tree policies may impose
additional restrictions on GLEPs but may not override them.

The process for creating and updating GLEPs is documented in `GLEP 1`_.
In general, all GLEP updates go through mailing list review and need
to be approved by the Council.

Developer Manual
~~~~~~~~~~~~~~~~
Devmanual_ is the basic guide for ebuild developers.  Besides policies,
it contains many general recommendations and detailed instructions.
Developer Manual does not specify policies itself, and needs to comply
with policies defined in this document.

Technically, devmanual can be changed by any developer.  However, it is
recommended that all changes are reviewed by the `devmanual project`_.


External standards
------------------

POSIX
~~~~~
POSIX_ is the basic standard for operating systems.  However, its rules
apply to the software packaged in Gentoo rather than the distribution
itself.  Nevertheless, when no more specific policy applies, following
POSIX is recommended.


FHS
~~~
FHS_ specifies the suggested filesystem layout for Linux systems.
Gentoo follows FHS only partially.  Whenever Gentoo policies and FHS
disagree, Gentoo policies should be followed.


.. _PMS: https://projects.gentoo.org/pms/latest/pms.html
.. _PMS project: https://wiki.gentoo.org/wiki/Project:PMS
.. _future EAPI process: https://wiki.gentoo.org/wiki/Project:Package_Manager_Specification/Future_EAPI_process
.. _GLEPs: https://www.gentoo.org/glep/
.. _GLEP 1: https://www.gentoo.org/glep/glep-0001.html
.. _devmanual: https://devmanual.gentoo.org/
.. _devmanual project: https://wiki.gentoo.org/wiki/Project:Devmanual
.. _POSIX: http://get.posixcertified.ieee.org/
.. _FHS: https://refspecs.linuxfoundation.org/fhs.shtml
