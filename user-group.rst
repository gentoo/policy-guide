Users and groups
================

.. index:: user
.. index:: group

User and group account policy
-----------------------------
:PG: 0901
:Source: QA
:Reference: https://bugs.gentoo.org/702460
:Reported: by repoman and pkgcheck (as deprecated eclass)

All new user/group accounts must be created via `GLEP 81`_ packages.
The existing packages should be migrated on the next version bump or
major update.

Existing and historical fixed UIDs/GIDs in range 0..499 (used
in baselayout or via user.eclass) as listed in uid-gid.txt can be reused
as-is in acct-* packages.

UIDs and GIDs in range 0..100 are reserved for important system
accounts.  New assignments in that range need to be explicitly approved
by the QA lead, in response to a justified request from the developer.

The range 101..749 is provided for regular use by packages.
The assignments from this range follow the following rules:

1. A developer can select an arbitrary free UID/GID from this range.
   If in doubt, it is recommended to select successive numbers from 101
   upwards.

2. Unless there is a very good reason not to, matching users and groups
   should use the same number.  It is acceptable to leave gaps
   in assignments as a result of that.

3. Before pushing the new acct-* packages, the developer must push
   an update to uid-gid.txt adding the 'acct' entry for the desired
   UID/GID.  This serves as a synchronization primitive to prevent
   collisions.

Further UID/GID ranges will be open in the future as the need arises.

*Rationale*: this is the second version of the policy for GLEP 81
packages.  It simplifies the process to aid rapid adoption of the new
system.  Review requirement and pointless cross-distro syncing were
removed, in favor of a simple process of allocating the next free number
and using it.

The ranges have been chosen to delay the imminent collision between
explicitly reserved UIDs / GIDs and the ones allocated dynamically by
user.eclass (starting from 999 downwards).  The lowest GID range has
been reserved for true system users and groups.


.. _GLEP 81: https://www.gentoo.org/glep/glep-0081.html
