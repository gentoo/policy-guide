Package Maintainers
===================

.. index:: maintainer; adding

Adding new maintainers
----------------------
:Source: QA
:Reported: no

Developers must not add other developers as package maintainers, unless
the developers in question consent to that.  Developers must not add
projects that they are not members of as package maintainers, unless
one of the project members explicitly agrees to that or the project
policy explicitly permits it.

*Rationale*: this policy aims to prevent package maintainers being added
as backup maintainers without their consent or knowledge.  What's worse,
once the original maintainer resigns the packages frequently drop
to backup maintainers who are neither interested in maintaining them,
nor often aware why they are listed as maintainers.

For example, developers used to frequently add Python team as a backup
maintainer to various packages not fitting the project's profile.  This
includes various end-user programs written in Python.  Many of those
packages ended up being maintained solely by Python, and distinguishing
them from packages actually within project's profile was hard.


.. index:: maintainer; new packages without

New packages without a maintainer
---------------------------------
:Source: QA
:Reported: no

It is explicitly forbidden to add new packages without a dedicated
maintainer.  This does not apply if the package in question is not
technically a new one but merely split out of unmaintained package.

*Rationale*: Gentoo is currently suffering from a very large number
of packages without a maintainer.  There is a small group of developers
trying to fix them as necessary.  It is unfair and inappropriate
to increase their maintenance burden by adding new packages and refusing
to take care of them.


.. index:: maintainer; removing
.. index:: up for grabs

Removing package maintainers
----------------------------
:Source: QA
:Reported: no

When removing maintainers from a package, the developer must reassign
all bugs filed for it.  Furthermore, when removing the last maintainer
for a package, the developer must add the following comment
to ``metadata.xml``::

    <!-- maintainer-needed -->

Furthermore, the developer must send an 'up for grabs' mail
to gentoo-dev mailing list, containing the list of packages with
no maintainer.  If possible, please include any information that could
be helpful to future maintainers.

*Rationale*: reassigning bugs is necessary to make sure that old bugs
are not lost assigned to developers who are no longer interested
in them.  The maintainer-needed comment is meant to make it possible
to easily grep for unmaintained packages.  The 'up for grabs' mails aim
to increase the chances of packages finding a new maintainers (compared
to them silently becoming maintainer-needed).
