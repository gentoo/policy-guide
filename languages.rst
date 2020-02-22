Language-specific policies
==========================

.. index:: python

Python
------

.. index:: python; eclass
.. index:: eclass; python-any-r1
.. index:: eclass; python-r1
.. index:: eclass; python-single-r1

Eclass usage
~~~~~~~~~~~~
:PG: 0501
:Source: Python project
:Reference: https://wiki.gentoo.org/wiki/Project:Python/Eclasses
:Reported: by pkgcheck

All packages using Python (either through installing Python modules
or scripts, linking to libpython, calling Python at runtime or build
time) must do it through one of the python-r1 eclasses.  Packages must
not directly depend on Python, directly use PYTHON_SINGLE_TARGET
or PYTHON_TARGETS.  The variables and functions provided by the eclasses
must be used instead.

All ebuilds must explicitly define supported Python implementations
in PYTHON_COMPAT.  Dependencies between Python packages must use
PYTHON_USEDEP, PYTHON_SINGLE_USEDEP or python_gen_cond_dep in order
to ensure implementation match.

*Rationale*: the eclass code guarantees consistent and reliable handling
of slotted Python.  It ensures that the whole dependency graph uses
matching implementation and that programs will not accidentally break
if user changes his Python preferences.  The helper functions
and variables also make it possible to gracefully retire old
implementations with minimal changes to existing ebuilds.


.. index:: python; python 2

Python 2 deprecation
~~~~~~~~~~~~~~~~~~~~
:PG: 0502
:Source: Python project
:Reference: https://wiki.gentoo.org/wiki/Project:Python#Python_2_end-of-life
:Reported: no

Python 2 is being phased out of Gentoo packages.  Python 2 support
must not be introduced in new packages, unless explicitly required
to maintain compatibility with existing packages.  Packages that do not
support Python 3 should be removed sooner or later, depending
on Python 3 porting chances.

In packages that support both Python 2 and Python 3, the Python 2
support should be gracefully retired, as soon as their reverse
dependencies are ready or removed.

*Rationale*: Python 2 has reached its (deferred) end-of-life by the end
of 2019.  Many important upstream projects have already removed support
for Python 2.  Those packages are frequently dependencies of other
packages, causing the cost of maintaining Python 2 support to grow
exponentially.

Early removal of unnecessary Python 2 support will both reduce
the long-term maintenance costs, and give users better chance to prepare
than delaying it until the number of packages losing Python 2 support
will cause major upgrade issues.
