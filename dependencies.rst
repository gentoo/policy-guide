Dependencies
============

.. index:: dependency; optional runtime
.. index:: USE flags; for optional RDEPEND

Optional runtime dependencies
-----------------------------
:PG: 0001
:Source: QA
:Reference: https://wiki.gentoo.org/index.php?title=Project:Quality_Assurance/Policies&oldid=104017#USE-Controlled_Optional_RDEPENDS
:Reported: no

Using USE flags to control optional runtime dependencies is not
acceptable except under very specific circumstances, such as a package
being nonfunctional unless at least one of a set of optional runtime
dependencies is installed.

There is no specific preference as to how user should be informed
of optional runtime dependencies.  Three possible ways are
``optfeature`` eclass, ``readme.gentoo-r1`` eclass and plain ``elog``
messages.

*Rationale*: toggling USE flags in order to enable or disable optional
runtime dependencies causes needless rebuilds of packages in question.
This is especially important for packages that take long time to build.

.. Note::

   `GLEP 62`_ proposes a solution permitting flipping USE flags without
   rebuilding package in question.  It has been tentatively approved
   by the Council but no reference implementation has been written.


.. index:: dependency; = with no revision

=-dependencies with no revision
-------------------------------
:PG: 0002
:Source: QA
:Reported: by repoman and pkgcheck

Whenever a non-wildcard ``=`` (equals) dependency is used on a package,
the requested revision must be specified explicitly.  When the zeroth
revision is requested, ``-r0`` must be used.  When no specific revision
is necessary, the ``~`` (tilde) operator must be used instead.

*Example*::

    # BAD:
    =dev-libs/libfrobnicate-1.2.3
    # GOOD:
    =dev-libs/libfrobnicate-1.2.3-r0
    =dev-libs/libfrobnicate-1.2.3-r3
    ~dev-libs/libfrobnicate-1.2.3

*Rationale*: using ``=`` operator in place of ``~`` to mean a specific
version has been a common mistake.  This policy uses the fact that
no revision and explicit ``-r0`` are equivalent.  By explicitly
requesting the latter, it warns developers to reconsider whether they
used the correct operator.


.. index::
   pair: slot/subslot; dependency

Slot and subslot dependencies
-----------------------------

on (sub-)slotted packages
~~~~~~~~~~~~~~~~~~~~~~~~~
:PG: 0011
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
:PG: 0012
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


.. index::
   single: dependency; dynamic
   pair: dependency; revision bump

Revision bumps on runtime dependency changes
--------------------------------------------
:PG: 0003
:Source: Council
:Reference: https://projects.gentoo.org/council/meeting-logs/20151011-summary.txt
:Reported: no

It must not be assumed that changes to package's dependencies will
be implicitly propagated to users who have installed the package
already.  Whenever the change needs to be propagated (e.g. to prevent
a missing runtime dependency from being cleaned), the package revision
must be increased.

This does not apply to build-time dependencies.

*Rationale*: developers were historically relying on Portage's behavior
called *dynamic dependencies* which caused Portage to implicitly use
dependencies specified in matching ebuilds for installed packages.  This
is non-portable and unreliable.  Users using different package managers,
disabling the feature or simply missing the timeframe during which
the old ebuild version existed had experienced dependency graph breakage
and other problems due to it.

The policy requires developers to explicitly account for that
possibility.  Revision bumps ensure that users who installed the package
from the previous ebuild version rebuild it and get the updated
dependencies as a result.

.. Note::

   The dynamic dependency usage problem has a flip side.  You can't rely
   on in-place dependency changes *not* being propagated either.  For
   example, if you notice that a package linked to libfoo unnecessarily,
   and decide to remove the dependency and code responsible for linking
   to it in place, Portage may apply the former immediately even
   if the package installed by the user still links to libfoo.


.. index::
   pair: USE flags; dependency

USE dependencies
----------------

on packages without the flag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:PG: 0021
:Source: QA (inferred from PMS)
:Reported: by pkgcheck

Whenever a package uses a 2-style USE-dependency on another package,
all package versions matching the dependency must have the flag
in question.  If the dependency matches at least one version missing
the flag, either 4-style USE-dependency (i.e. having ``(-)`` or ``(+)``
indicator) must be used, or the restriction must be refined to match
only versions having the flag.

*Example*::

    # BAD: USE=gtk2 is not supported by v2
    dev-foo/libfrobnicate[gtk2]
    # GOOD: all matching versions have USE=gtk2
    <dev-foo/libfrobnicate-2[gtk2]
    # GOOD: indicate the default
    dev-foo/libfrobnicate[gtk2(-)]

    # BAD: USE=tools is no longer needed with v2
    dev-foo/libbar[tools]
    # GOOD: indicate the default
    dev-foo/libbar[tools(+)]

*Rationale*: according to the PMS section on `2-style and 4-style USE
dependencies`_, it is an error to apply 2-style USE dependency to
a package missing the flag.  Furthermore, checking for this makes it
possible to report whenever USE flags on a package are changed without
updating its reverse dependencies.


.. _GLEP 62: https://www.gentoo.org/glep/glep-0062.html
.. _Paludis: https://paludis.exherbo.org/
.. _2-style and 4-style USE dependencies:
     https://projects.gentoo.org/pms/7/pms.html#x1-790008.2.6.4
