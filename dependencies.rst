Dependencies
============

.. index:: dependency; optional runtime
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


.. index::
   pair: slot/subslot; dependency

Slot and subslot dependencies
-----------------------------

on (sub-)slotted packages
~~~~~~~~~~~~~~~~~~~~~~~~~
:Source: QA
:Reference: https://archives.gentoo.org/gentoo-portage-dev/message/9cae3a92412a007febe7ac0612d50f5f
:Reported: by repoman and pkgcheck

Whenever a package dependency specification matches a range of versions
that span different slots or subslots, the package must explicitly
include slot specification.  If the ``:=`` operator is not applicable
and any slot is acceptable, explicit ``:*`` operator must be used.
If the ``:<slot>=`` operator is not applicable and only a specific slot
can be used, ``:<slot>`` value must be explicitly specified.

Package dependency specification without explicit slot specifier can
be used on packages that are not slotted nor subslotted at the moment.

*Rationale*: this policy aims to help detecting missing slot operators
when dependencies start using slots or subslots.  It uses the fact that
the explicit ``:*`` operator is equivalent to no slot specification,
and therefore can be used interchangeably.  In this case, we assume
that the latter means 'dependency not verified yet', while the former
means 'verified that any slot is acceptable'.

.. Note::

   The Paludis_ package manager applies different logic when no slot
   is specified on the dependency.  It pulls in the slot corresponding
   to the newest package version available.


.. index::
   pair: slot/subslot; Qt

special case: Qt packages
~~~~~~~~~~~~~~~~~~~~~~~~~
:Source: Qt project
:Reference: https://wiki.gentoo.org/wiki/Project:Qt/Policies#Dependencies
:Reported: no

The Qt packages use subslots in an uncommon way.  The public ABI of Qt
libraries is stable within each slot, and the subslot is used to refer
to private ABI.  Therefore, the ``:=`` operator must only be used
if your package uses one of the private API parts, and plain ``:5``
or likewise dependency must be used otherwise.

proactive use of slot operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There is an open debate on whether developers should be proactively
adding ``:=`` slot operators on packages that do not define subslots
yet.

Proponents of the idea point out that adding slot operators to reverse
dependencies after the package becomes slotted is cumbersome and usually
results in losing the subslot rebuild opportunity at least once.  They
argue that in many cases the future use of subslots is reasonably
predictable.

Opponents claim that the future use of subslots is not 100% predictable.
They point out the case of Qt packages as an example.


.. _GLEP 62: https://www.gentoo.org/glep/glep-0062.html
.. _Paludis: https://paludis.exherbo.org/
