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


.. index:: eclass; deprecated

Deprecated eclasses
-------------------
:PG: 1003
:Source: individual eclass maintainers
:Reported: by pkgcheck and repoman

Deprecated eclasses should not be used in new ebuilds.  Existing
packages should be updated not to use these eclasses on version bumps,
or proactively when no version bumps are expected.

Deprecations are indicated using the ``@DEPRECATED`` eclassdoc tag
inside the eclass files.
