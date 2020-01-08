USE flags
=========

.. index::
   single: USE flags; gtk
   pair: USE flags; Qt
   single: USE flags; versioned

Versioned USE flags
-------------------
:Source: QA
:Reference: https://wiki.gentoo.org/index.php?title=Project:Quality_Assurance/Policies&oldid=109991#Versioned_USE_flags
:Reported: no

If a need arises to create new USE flags responsible for switching
between multiple versions of a specific dependency, it is recommended
that flat, explicitly versioned flags are used (e.g. ``qt4``, ``qt5``).
The hierarchical form used e.g. by GTK+ (``gtk`` meaning 2-or-3,
then optionally ``gtk2`` or ``gtk3`` to switch between both)
is discouraged.

Any future set of USE flags introduced in this way needs to be discussed
with the QA team before introduction.

.. TODO:: rationale

.. Note::

   This policy has historically been defined as an generalization
   of the QA policy on gtk/gtk2/gtk3 flags.  The latter policy has been
   removed since.


.. index:: USE flags; underscore

Underscores in USE flag names
-----------------------------
:Source: Council
:Reference: https://projects.gentoo.org/council/meeting-logs/20191013-summary.txt
:Reported: by pkgcheck

Underscores are reserved for USE_EXPAND flags, and must not be used
within names of newly-defined regular flags.  Existing uses are
considered technically valid, and phasing them out has low priority.

Flags that attempt to resemble USE_EXPAND should be either converted
into proper (global) USE_EXPAND, or made into shorter (unprefixed)
local flags.  In other flags, replacing underscore with hyphen is
recommended.

*Rationale*: a few packages in Gentoo attempted to imitate USE_EXPAND
via local USE flags.  This has no clear advantage, may be confusing
to end users who assume that they will work like USE_EXPAND
and in the end unnecessarily lengthens flag names or even causes
unnecessary mismatches between global flags and local flags.

Extending the rule to all flags containing underscores aims to make
distinguishing USE_EXPAND and regular flags easier.  It also improves
consistency between flag names that historically used hyphens
or underscores depending on developer's personal preference.
