Ebuild file format
==================

.. index::
   single: bash; conditions
   single: bash; variable reference
   single: indentation

Coding style
------------
:Source: QA
:Reported: partially via repoman and pkgcheck

While Gentoo leaves most of the coding style choices to developers,
there are a few rules which we try to enforce.  Those are:

- Always indent using a single tab for indentation level.  Do not
  attempt to align, as it will not work with different tab widths.

- Whenever using named variables, use bracketed variable form, i.e.
  ``${foo}`` rather than ``$foo``.

- Use bash conditions ``[[ ... ]]`` rather than POSIX-ish ``[ ... ]``
  or ``test`` builtin.

*Rationale*: the recommended constructs are less error-prone.
Consistency avoids unnecessary changes when other developers edit
the ebuild.


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
