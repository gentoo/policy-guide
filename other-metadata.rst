Other metadata variables
========================

.. index:: slot/subslot; dynamic
.. index:: USE flags; multislot

Dynamic slots (multislot flag)
------------------------------
:PG: 0701
:Source: QA (inferred from PMS)
:Reference: https://wiki.gentoo.org/index.php?title=Project:Quality_Assurance/Policies&oldid=109991#multislot.2FUSE-dependent_SLOT, https://bugs.gentoo.org/174407
:Reported: ``use`` in global scope triggers fatal error

The use of ``multislot`` to alter ``SLOT`` values (as well as any other
USE-dependent slot values) in the Gentoo repository is forbidden.
Such a feature can be used in overlays, and it is acceptable to provide
such support in eclasses as long as it is not used in ::gentoo.

This policy has been explicitly declared in response to historical
(pre-2016) use of ``USE=multislot`` in toolchain ebuilds.  When the flag
was disabled, all package versions used the same slot, and upgrades were
handled as for non-slotted packages.  When the flag was enabled, each
version used a separate slot, permitting multiple versions being
installed simultaneously.  This allowed the user to choose between
the two options.

The original violation has been resolved by unconditionally slotting
the packages.  This permitted the users to install multiple versions
in parallel, while removal of old versions was to be handled via
``emerge --depclean``.

*Rationale*: this feature was in direct violation of PMS `metadata
invariance`_ requirements.  It caused the cached slot value to depend
on the state of querying the USE flag (which in turn could technically
depend on slot, via ``package.use``).  This caused undefined package
manager behavior which could include use of unpredictable slot, cache
invalidation or explicit errors.


.. index::
   single: homepage; meaningful value
   pair: homepage; gentoo.org

HOMEPAGE value must be meaningful
---------------------------------
:PG: 0702
:Source: QA
:Reference: https://archives.gentoo.org/gentoo-dev/message/83cc5bbd7bbe8bdf04dd3c3bc7f8a035
:Reported: known bad values are reported by pkgcheck

The HOMEPAGE specified for the package should either be dedicated
to the package in question or make it easy to find dedicated
information.  Packages must not use ``https://www.gentoo.org/``
or a similar generic homepage.  If no homepage is available, the special
value of ``https://wiki.gentoo.org/wiki/No_homepage`` must be used.

*Rationale*: The homepage specified in ebuilds is normally used to
locate information about the upstream project, e.g. downloads, source
code repository, bug tracker, documentation.  Homepages that make it
hard to locate information about a specific project have little value,
and the Gentoo homepage generally does not do a good job at linking even
major Gentoo projects.  Furthermore, many of the projects did not even
have a single dedicated subpage anywhere in Gentoo web space.  In all
those cases, using the explicit No_homepage marker at least makes it
easy to identify such packages.


.. index::
   single: restrict; test; USE=-test
   single: USE flags; test; restrict

RESTRICT=test for USE=-test
---------------------------
:PG: 0703
:Source: QA
:Reported: by pkgcheck

Whenever the package uses ``test`` flag to control test prerequisites
(or another flag with a similar purpose), it must explicitly restrict
tests when the flag is unset.

*Example*::

    IUSE="test"
    RESTRICT="!test? ( test )"

*Rationale*: contrary to common assumption, ``test`` flag is not special
and the package manager can execute tests when the flag is disabled.
The explicit restriction guarantees that tests will be skipped under
this circumstance, and they will not fail for users.

.. Note::
   Technically there are packages that do not strictly require this
   restriction since they handle missing test prerequisites gracefully
   (e.g. by skipping the tests).  However, we enforce the rule for all
   packages since omitting the restriction by mistake is much more
   common, and there is little harm in overspecifying it.


.. index:: license

LICENSE
-------
:PG: 0704
:Source: QA
:Reported: no

The ``LICENSE`` variable must explicitly list all licenses pertaining
to the "corresponding source" of the files installed by the package.
This includes all their source code, but also all scripts used to
control compilation and installation.  If some of the applicable
licenses are conditional to USE flags, appropriate USE conditionals
need to be expressed in the variable.

If a package bundles any dependencies that are either installed,
statically linked or in any other way combined with installed files,
the licenses of these dependencies need to be listed as well.  This
is not presently required when statically linking to dependencies
installed by separate packages in the repository.

The licenses for files that are neither installed nor used at build
time shall not be listed.

*Rationale*: the primary purpose of the license support in the package
manager is to provide the users with ability to decide on acceptable
licenses for their installed systems (and binary packages).  In order
for this to work effectively, the packages must provide a correct
and complete license list.

Static linking combines code from multiple packages, potentially covered
by different licenses.  Listing all licenses is the simplest way
of ensuring that nothing is missed, as well as protecting against wrong
derivative work licenses stated upstream (i.e. when a less restrictively
licensed package links to a more restrictively licensed dependency).

Listing of licenses is enforced for bundled dependencies but not for
static linking to other packages, as in the latter case it is
non-trivial to implement and the package manager already verifies
the license while building dependencies (but not when installing binary
packages).

.. Note::
   Please remember to include the licenses of support files provided
   by the ebuild, e.g. init.d scripts (usually GPL-2).


.. _metadata invariance: https://projects.gentoo.org/pms/7/pms.html#x1-600007.1
