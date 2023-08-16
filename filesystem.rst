File system layout
==================

.. index:: file system; installation paths

Installation paths
------------------
:PG: 0201
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

There must be no subdirectories in /bin and /sbin.

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

There must be no subdirectories in /usr/bin and /usr/sbin.

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


.. index:: file system; separate /usr

Support for separate /usr
-------------------------
:PG: 0202
:Source: QA
:Reference: https://projects.gentoo.org/council/meeting-logs/20130813-summary.txt
            https://projects.gentoo.org/council/meeting-logs/20130924-summary.txt
:Reported: no

Developers are not required to support using separate /usr filesystem
without an initramfs.

*Rationale*: upstream software (as of 2013) is already making support
for early boot without /usr mounted difficult, and whenever it is still
works, it is either subtly broken or relying on hacks (udev).  In setups
using initramfs, some of the boot and repair functionality can be moved
from rootfs to initramfs.


.. index:: file system; multilib-strict

Strict multilib layout
----------------------
:PG: 0203
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


.. index::
   pair: file system; static library
   pair: file system; libtool file

Static libraries and libtool files
----------------------------------
:PG: 0204
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


.. index::
   pair: file system; games

Game install locations and ownership
------------------------------------
:PG: 0205
:Source: Council, clarified by QA
:Reference: https://projects.gentoo.org/council/meeting-logs/20151213-summary.txt
            https://projects.gentoo.org/council/meeting-logs/20151011-summary.txt
:Reported: via install-qa-check.d

The historical game install locations (/usr/games and /etc/games) must
not be used anymore.  Instead, games should follow normal guidelines
for install locations.  As an exception, /usr/share/games can be used
if this location is used upstream, and /var/games can be used for shared
game files (e.g. high scores, game state files).

The historical games group must no longer be used.  Games must work
for users that are not in this group.  The aforementioned install
locations must therefore be owned by root and be world-readable.

If games need privileged access to shared files, the group gamestat
can be used for this purpose.  The game executables should be owned
by that group and made setgid.  The shared files must be installed
into /var/games hierarchy, and writable to gamestat group.

*Rationale*: there is no technical reason to isolate games from other
applications on the system, or to restrict access to them.  The boundary
between game and non-game packages is very blurry on modern systems,
especially due to web browsers.

The historical use of games group on Gentoo to control access is
inconsistent with the use in other distributions where it was used to
share data files.  Since the latter implied users must not be added
to the games group, a new group (gamestat) needed to be created to
fulfill that purpose.


.. index:: symbolic link; absolute target

Absolute symbolic link targets
------------------------------
:PG: 0206
:Source: QA
:Reported: by repoman and pkgcheck (when ebuild-generated)

Packages must not install symbolic links with absolute targets.
Instead, relative paths must be used.  An exception is granted
for symlinks to specially mounted filesystems (such as /proc, /run)
when symlinks are supposed to always reference the running host system.

*Example*::

    # BAD:
    dosym /usr/lib/frobnicate/frobnicate /usr/bin/frobnicate
    # GOOD:
    dosym ../lib/frobnicate/frobnicate /usr/bin/frobnicate
    # ACCEPTABLE EXCEPTION:
    dosym /proc/self/mounts /etc/mtab

*Rationale*: absolute symlinks work correctly only when the root
filesystem is mounted at /.  They point at the wrong location whenever
it is mounted in another location, e.g. for the purposes of recovery.
