Deprecations
============


.. index:: EAPI; deprecated

Deprecated EAPIs
----------------
:PG: 1001
:Source: Council
:Reference: https://gitweb.gentoo.org/repo/gentoo.git/tree/metadata/layout.conf
:Reported: by pkgcheck and repoman

Deprecated EAPIs should not be used in new ebuilds.  Existing packages
should be migrated to newer EAPIs on version bumps, or proactively when
no version bumps are expected.

The current list of deprecated EAPIs is stored as ``eapis-deprecated``
in ``metadata/layout.conf``.


.. index:: EAPI; banned

Banned EAPIs
------------
:PG: 1002
:Source: Council
:Reference: `Council-approved EAPIs`_
:Reported: by pkgcheck and repoman

Banned EAPIs must not be used by any new ebuilds.  Existing packages
should proactively be migrated to new EAPIs.  The only allowed exception
is when the new ebuild is a result of revision bump due to dependency
change or an important bug fix.

The authoritative source for banned EAPIs are Council meeting summaries.
The PMS project maintains a list of `Council-approved EAPIs`_.


.. _Council-approved EAPIs:
   https://wiki.gentoo.org/wiki/Project:Package_Manager_Specification#Council_approval_and_use_in_Gentoo_repository
