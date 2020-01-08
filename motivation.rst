Motivation and history
======================

Historical state of policy documentation
----------------------------------------
At the time, Gentoo was lacking a clear and focused document listing all
development-related policies in a concise and clear way.

PMS_ provided a technical specification for the ebuild files but did
not provide a sufficient explanation on how to use it.  Furthermore, PMS
was focused on wider usage of the ebuild files than intended for
the Gentoo repository, and therefore was partially restricted via tree
policies.

Past Council decisions can be found in the `Council meeting logs`_.
However, their form makes it hard to find any particular decision,
not to mention establishing a complete list of policies.

At some point, the QA team started listing `QA policies`_ on its wiki
page.  Only eight policies were listed so far.  The policies were written
out as a flat list with no particular order which is not going to scale
well.

Finally, there was an attempt to turn devmanual_ into a source of
reference policies.  It was rejected by its maintainers as explicitly
against the original purpose of this document.  Furthermore, a large
amount of stale information combined with ability to edit by every
developer would make it unclear which parts are applicable policies,
and which are obsolete or non-binding tips.

There are also project policies, scattered across wiki pages and other
project documentation, and a lot of de facto policies that were
established less or more formally in the past but were never really
written down.


Purpose of the Policy Guide
---------------------------
The Policy Guide was created in order to address aforementioned
documentation deficiencies.  Its primary purpose is to collect all
applicable policies from various sources and combine them into a single
logically organized document.

Along with a wording of each policy, its rationale should be provided
(if available) and an indication of which body set the policy.
The former should make it possible to better understand the policy,
and apply it in spirit rather than requiring very precise wording.
The latter should make it clear who can be queried for additional
information, and how the policy can be updated if need arises.

This Guide is going to replace the QA team policies page.  All new QA
policies will be documented directly in it.  Other documentation (e.g.
devmanual) should conform to policies stated here.


.. _PMS: https://projects.gentoo.org/pms/latest/pms.html
.. _Council meeting logs: https://wiki.gentoo.org/wiki/Project:Council/Meeting_logs
.. _QA policies: https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Policies
.. _devmanual: https://devmanual.gentoo.org/
