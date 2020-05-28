Installed files
===============

.. index::
   single: installed files; small files
   single: USE flags; small files

Installation of small files
---------------------------
:PG: 0301
:Source: QA
:Reported: no

Ebuilds must not introduce USE flags to control installing files that
are small in size, require no additional dependencies and not cause any
negative consequences to the program behavior by being installed.  Such
files must be installed unconditionally.  Examples include shell
completion files, systemd service units, localization files.

Users wishing to strip unnecessary files of this category should use
INSTALL_MASK to do so.

*Rationale*: the goal of this policy is to avoid unnecessary rebuilds
of packages when the cost of installing additional files is much smaller
than the cost of rebuild.  It has been specifically brought in context
of bash completions in LibreOffice -- a user who did not notice that he
did not enable the flag should not be required to spend hours rebuilding
such a huge package in order to install one tiny file.

.. Note::

   While technically e.g. ``app-shells/bash-completion`` could be
   considered a dependency of installed bash completions, it is not
   applicable here since this package needs to be installed by the user
   if he wishes to use completions in the first place, and if it is not
   installed, completion files are not used at all.


.. index::
   pair: installed files; static library

Installation of static libraries
--------------------------------
:PG: 0302
:Source: QA
:Reported: no

Packages must not install static libraries unless they are explicitly
required, either by themselves or their reverse dependencies.  If both
shared and static libraries are supported, shared libraries must be
installed by default and ``USE=static-libs`` may be added for static
libraries if they are necessary.

*Rationale*: static linking is strongly discouraged as it makes security
support for packages practically impossible.  It may be used whenever
really necessary (e.g. for recovery tools) but otherwise proliferating
it is considered harmful.  There is no point in installing static
libraries if they are never going to be used.

.. Note::

   If the package's build system does not support disabling static
   library build, it is recommended to patch it and submit the patch
   upstream.  However, if that is not feasible and building both shared
   and static libraries does not require compiling source files twice,
   it is acceptable to strip static libraries in ``src_install()``.


.. index::
   pair: installed files; libtool file

Installation of libtool (.la) files
-----------------------------------
:PG: 0303
:Source: QA
:Reported: no

Packages must not install libtool .la files unless they are explicitly
required.  Generally, they might be required if:

a. the package is using a plugin loader that requires .la files in order
   to locate plugins and does not have .so fallback (very uncommon),

b. the package is installing static libraries that have additional
   dependencies and no pkg-config files or other tools that provide
   the list of dependencies to build systems.

It is recommended to use the following one-liner to remove .la files::

    find "${ED}" -name '*.la' -remove || die

*Rationale*: libtool files were historically introduced as an attempt
to supplement static library archives with dependent library list.
However, they were only supported by libtool-based (autotools) projects
and caused many issues, in particular due to hardcoding full paths.
Today they are practically replaced by more portable pkg-config files,
and while libtool keeps generating them, they are considered
unnecessary and potentially harmful.
