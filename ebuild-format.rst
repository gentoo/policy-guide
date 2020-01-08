Ebuild file format
==================

.. index:: eblit

Code must be contained within ebuild and eclasses
-------------------------------------------------
:Source: QA
:Reference: https://bugs.gentoo.org/612630
:Reported: no

The ebuild code must be fully contained within .ebuild and .eclass
files.  It is forbidden to load additional ebuild code from other files
via ``source``, ``eval`` or any other possible method.

This affects historical use of 'eblits' to include phase functions from
external files.  The eblits used by the few affected packages were
converted into eclasses.

*Rationale*: moving ebuild code to non-standard locations is against
the principle of least surprise.  It makes the maintenance harder,
confuses other developers and tools that do not explicitly account for
that possibility, including linting tools.
