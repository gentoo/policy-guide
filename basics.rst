Basic information
=================

Goals of policy making
----------------------
The Gentoo policies focus on three aims:

1. *Portability*.  By following the policies, it should be possible
   to package software so that it works on different system setups.
   This includes various supported architectures, basic system
   components, service managers, package managers, combinations
   of compiler and linker flags, etc.

2. *Maintainability*.  The policies aim to provide consistent coding
   practices that make it easy for a different person to co-maintain
   the package or take over after previous maintainer.  This also
   reduces the risk of mistakes experienced by the end users.

3. *End-user experience*.  The policies try to help developers
   in providing a consistent end-user experience.  The same concepts
   applied across different packages make it easier for user to achieve
   his goals and reduce the likeliness of surprising behavior.


Policy compliance checking
--------------------------
Currently, there are two kinds of tools involved in detecting policy
violations:

1. Linting-class tools, including repoman_ and pkgcheck_.  Those tools
   analyze ebuilds and other files in the package repository for known
   policy violations.  They are limited to checking for problems that
   can be detected without running the phase functions.

2. Build- and install-time QA checks, implemented in package managers.
   Those trigger while the ebuilds are executing.  They are limited
   to testing the currently running code path.

Developers are expected to use both kinds of tools before pushing their
commits.  They should both lint the changed ebuilds using repoman_
or pkgcheck_, and test whether their packages build and install
correctly.

Additionally, Gentoo is running pkgcheck_ periodically as `Gentoo CI`_.
All non-trivial violations are reported to the gentoo-automated-testing_
mailing list and to the developers making the relevant commits.  This
supplements the direct use of linting tools by developers with reliable
tree-wide scans.


Policy enforcement
------------------
The Gentoo `QA team`_ is tasked with enforcement of the tree policies.
Its role is governed by `GLEP 48`_.  It focuses on documenting
the policies, resolving doubts regarding them and educating
the developers.

The QA team members can also take direct action in resolving minor
quality problems (i.e. when fixing directly involves far less effort
than if the developer was requested to fix it), or when developer
refuses to resolve policy violations.

Finally, in case of repeated unwillingness to follow policies, the QA
team can issue disciplinary measures against the developer in question.


Policy making, changes and appeals
----------------------------------
The majority of policies are written down and maintained by the `QA
team`_.  Other Gentoo projects also create policies that affect their
specific areas of contributions (e.g. `systemd project`_ created
policies related to installing systemd unit files).

Each policy listed in this document indicates the body maintaining it.
In order to change or abolish the policy, that team should be contacted.
If the project in question disagrees with the change, `QA team`_ can be
asked to override the policy.  All QA decisions and policies can further
be appealed to the Council_.


.. _repoman: https://wiki.gentoo.org/wiki/Repoman
.. _pkgcheck: https://github.com/pkgcore/pkgcheck
.. _Gentoo CI: https://qa-reports.gentoo.org/output/gentoo-ci/output.html
.. _gentoo-automated-testing: https://archives.gentoo.org/gentoo-automated-testing/
.. _QA team: https://wiki.gentoo.org/wiki/Project:Quality_Assurance
.. _GLEP 48: https://www.gentoo.org/glep/glep-0048.html
.. _systemd project: https://wiki.gentoo.org/wiki/Project:Systemd
.. _Council: https://wiki.gentoo.org/wiki/Project:Council
