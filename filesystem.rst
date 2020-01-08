File system layout
==================

.. index:: file system; installation paths

Installation paths
------------------
:Source: QA
:Reference: https://gitweb.gentoo.org/repo/gentoo.git/tree/metadata/install-qa-check.d/08gentoo-paths
:Reported: via install-qa-check.d

Gentoo packages may only install into one of the following top-level
directories:

.. hlist::
   :columns: 5

   - /bin
   - /boot
   - /dev
   - /etc
   - /lib*
   - /opt
   - /sbin
   - /srv
   - /usr
   - /var

Furthermore, only the following subdirectories of /usr are permitted:

.. hlist::
   :columns: 4

   - /usr/bin
   - /usr/include
   - /usr/lib*
   - /usr/libexec
   - /usr/sbin
   - /usr/share
   - /usr/src
   - /usr/<triplet>

Furthermore, within /usr/share/doc hierarchy only a subdirectory named
after full package name and version with revision (PF) is permitted.

In the aforementioned lists, 'lib*' indicates lib and its appropriate
suffixed variants for the architecture in question.  '<triplet>'
indicates either CHOST or CTARGET value, as used by toolchain packages.

Additional exceptions can be granted by the QA team.  Currently those
exceptions are:

- /gnu for the guix package manager
- /nix for the nix package manager

.. TODO:: rationale


.. index:: file system; multilib-strict

Strict multilib layout
----------------------
:Source: QA
:Reference: https://gitweb.gentoo.org/proj/portage.git/tree/bin/install-qa-check.d/80multilib-strict
:Reported: via install-qa-check.d, fatal

Libraries must be installed into an appropriate /lib* or /usr/lib*
directory corresponding to their ABI.  For example, 64-bit libraries
on amd64 must be installed into lib64 and not lib.

Libraries installed as a part of larger software package can be
installed along with it into a subdirectory of lib.

*Rationale*: historically, Gentoo has been symlinking /lib to /lib64
in order to maintain compatibility with old packages hardcoding /lib
path.  With modern Gentoo profiles, this is no longer the case
and packages must install libraries into appropriate directory for them
to be correctly found by the dynamic loader.


.. index:: file system; static library
.. index:: file system; libtool file

Static libraries and libtool files
----------------------------------
:Source: QA
:Reference: https://gitweb.gentoo.org/proj/portage.git/tree/bin/install-qa-check.d/80libraries
:Reported: via install-qa-check.d, fatal

Static libraries and libtool files (.la) must be installed into /usr
hierarchy and never to root filesystem (/lib*).  If an additional shared
version of the library is installed to /lib*, a .so linker script must
be installed into /usr/lib* in order to ensure correct linking.

*Rationale*: historically, the purpose of root filesystem was to hold
files strictly needed at boot.  For this reason, many old Gentoo
installations may still use small / partition.  Static libraries are
used only during package builds, and installing them to rootfs would
be a waste of space.
