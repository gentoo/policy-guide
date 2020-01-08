Other metadata variables
========================

.. index:: slot/subslot; dynamic
.. index:: USE flags; multislot

Dynamic slots (multislot flag)
------------------------------
:Source: QA (inferred from PMS)
:Reference: https://wiki.gentoo.org/index.php?title=Project:Quality_Assurance/Policies&oldid=109991#multislot.2FUSE-dependent_SLOT
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


.. _metadata invariance: https://projects.gentoo.org/pms/7/pms.html#x1-600007.1
