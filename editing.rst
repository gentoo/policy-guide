Editing and publishing updates to this Guide
============================================

Formatting and style
--------------------
While editing the Guide, please respect the existing formatting rules.
Notably:

- wrap lines at 72 characters
- two spaces between sentences (after full stop), one space otherwise
- one empty line between titles and paragraphs, two empty lines between
  text and next section
- indent using spaces, aligning to previous line

When adding a new rule, use the chapter with a fitting topic.  Some
rules match multiple chapters, choose the one that fits it best.  Make
sure to match existing keywords in index.


Getting sources
---------------
The reference repository is hosted at git.gentoo.org, and available
via `proj/policy-guide.git gitweb`_.  To clone it::

    # via https
    git clone https://anongit.gentoo.org/git/proj/policy-guide.git
    # via ssh
    git clone git@git.gentoo.org:proj/policy-guide.git

Non-developers wishing to send pull requests may prefer to fork
the GitHub `gentoo/policy-guide repository`_ and clone their own fork
instead.


Building
--------
A tox-file is provided to build the Guide in a virtualenv, installing
all necessary dependencies.  To build the HTML version, run::

    tox

Another format (as well as other make arguments) can be specified
as a command-line argument, e.g.::

    tox latexpdf


Sending contributions
---------------------
Changes to this document can be either submitted to `Policy Manual
Gentoo Bugzilla component`_ as git-format patches attached to the bugs,
or to `gentoo/policy-guide repository`_ as pull requests.


Merging pull requests
---------------------
The recommended way to merge pull requests is to use
``app-portage/pram``.  To configure the remote before the first use,
run the following command in your checkout::

    git config --replace-all pram.repo gentoo/policy-guide

Afterwards, call the tool to merge pull request by number::

    pram N


Publishing
----------
The built version of Policy Guide is currently published via a git
repository.  The recommended method is to clone the repository
into ``_build/html`` in order to make Sphinx output into the checkout::

    rm -r _build/html
    git clone git@git.gentoo.org:sites/projects/qa/policy-guide.git \
        _build/html

Commit and push all the changes after rebuilding the Guide.


.. _proj/policy-guide.git gitweb:
   https://gitweb.gentoo.org/proj/policy-guide.git/
.. _gentoo/policy-guide repository:
   https://github.com/gentoo/policy-guide
.. _Policy Manual Gentoo Bugzilla component:
   https://bugs.gentoo.org/enter_bug.cgi?product=Documentation&component=Policy+Guide
