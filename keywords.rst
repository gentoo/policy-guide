Keywording and stabilization
============================

.. index:: keywords; rekeywording

Rekeywording on dropped keywords
--------------------------------
:PG: 0401
:Source: QA
:Reported: by pkgcheck and repoman

The developer removing keywords from a package (e.g. due to new
dependencies) must file a rekeywording bug asking for the package being
retested.  This rule can be exempted if the package is known not to work
(anymore) on the arch in question.

*Rationale*: rekeywording on minor architectures often takes a long
time.  If a developer neglects to request it immediately, it negatively
affects other developers who in the future either want to stabilize
a new version or to remove an old version.


.. index:: keywords; stabilizing new versions

Stabilizing new versions
------------------------
:PG: 0402
:Source: QA
:Reported: by pkgcheck

Whenever requesting a stabilization of a new version of the package,
the developer must CC *all* arches that had at least one previous stable
version of the package in question, and that still have ~arch keywords
in the stabilized version.  This applies to experimental architectures
as well.

The stabilization request can be closed and old stable version removed
once all non-experimental architectures have processed the stabilization
request.  However, the remaining arch teams should be kept CC-ed in case
they wanted to process the bug.

*Rationale*: there were some cases of developers requesting
stabilization only of a subset of architectures they were personally
interested in.  This meant some other developer had to independently
request stabilization on remaining architectures which only meant
a duplication of effort and unnecessary confusion over which version
is stable and whether arch teams are slacking or stabilization was not
requested on remaining architectures in the first place.


.. index:: keywords; removing stable

Removing stable keywords
------------------------
:PG: 0403
:Source: QA
:Reference: https://wiki.gentoo.org/index.php?title=Project:Quality_Assurance/Policies&oldid=126033#Dropping_Stable_KEYWORDs
:Reported: n/a

Stable keywords (or the last stable version) can be removed from
a package if the relevant arch team does not respond within 90 days.
If the removal causes a breakage of dependency graph, the developer
must work with maintainers of the depending packages before proceeding
with it.

The policy for removing a package must be followed here, with exception
of last rite mails.

.. TODO:: rationale
