Dependencies
============

.. index:: RDEPEND; optional
.. index:: USE flags; for optional RDEPEND

Optional runtime dependencies
-----------------------------
:Source: QA
:Reference: https://wiki.gentoo.org/index.php?title=Project:Quality_Assurance/Policies&oldid=104017#USE-Controlled_Optional_RDEPENDS
:Reported: no

Using USE flags to control optional runtime dependencies is not
acceptable except under very specific circumstances, such as a package
being nonfunctional unless at least one of a set of optional runtime
dependencies is installed.

There is no specific preference as to how user should be informed
of optional runtime dependencies.  The two possible options include
using ``elog`` messages and ``readme.gentoo-r1`` eclass.

*Rationale*: toggling USE flags in order to enable or disable optional
runtime dependencies causes needless rebuilds of packages in question.
This is especially important for packages that take long time to build.

.. Note::

   `GLEP 62`_ proposes a solution permitting flipping USE flags without
   rebuilding package in question.  It has been tentatively approved
   by the Council but no reference implementation has been written.


.. _GLEP 62: https://www.gentoo.org/glep/glep-0062.html
