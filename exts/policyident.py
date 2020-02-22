# Handle :PG: policy identifiers for Policy Guide
# (c) 2020 Michał Górny
# 2-clause BSD license

import collections

from docutils import nodes

from sphinx.domains import Index
from sphinx.util import logging


logger = logging.getLogger(__name__)

Policy = collections.namedtuple('Policy', ('id', 'title', 'docname',
                                           'chapter'))


class PolicyIndex(Index):
    name = 'policy-index'
    localname = 'Policy Index'
    shortname = 'Policy Index'

    def generate(self, docnames=None):
        env = self.domain.env
        if not hasattr(env, 'policy_index'):
            env.policy_index = []

        entries = collections.defaultdict(list)
        for p in env.policy_index:
            if docnames is not None and p.docname not in docnames:
                continue
            entries[p.chapter].append(('PG' + p.id,  # name
                                       0,            # subtype
                                       p.docname,    # docname
                                       'pg' + p.id,  # anchor
                                       p.title,      # extra
                                       '',           # qualifier
                                       ''))          # descr

        return ([(k, sorted(v)) for k, v in entries.items()], False)


def find_pg_id(section):
    # first child should be title
    title = section.children[0]
    assert isinstance(title, nodes.title)
    # second child should be field list
    cl = section.children[1]
    if not isinstance(cl, nodes.field_list):
        return None, title.astext(), None

    for f in cl.traverse(nodes.field):
        fn = next(iter(f.traverse(nodes.field_name)))
        fv = next(iter(f.traverse(nodes.field_body)))
        if fn.astext().upper() == 'PG':
            if fn.astext() != 'PG':
                raise RuntimeError('PG field must be uppercase')
            iv = '{:04d}'.format(int(fv.astext(), 10))
            if fv.astext() != iv:
                raise RuntimeError('PG value must be 4 digits, zero-padded ({})'
                                   .format(iv))

            el = section
            titles = []
            while el.parent is not None:
                title = el.children[0]
                assert isinstance(title, nodes.title)
                titles.append(title.astext())
                el = el.parent
            # combine all section titles up to but excluding
            # the chapter title
            title = ': '.join(reversed(titles[:-1]))

            return iv, title, titles[-1]

    logger.warning('%s: no PG identifier found', title.astext())
    return None, title.astext(), None


def on_doctree_read(app, doctree):
    env = app.builder.env
    if not hasattr(env, 'policy_index'):
        env.policy_index = []

    for node in doctree.traverse(nodes.section):
        pg_id, title, chapter = find_pg_id(node)
        if pg_id is not None:
            node['ids'].insert(0, 'pg' + pg_id)
            env.policy_index.append(Policy(pg_id, title, env.docname,
                                           chapter))


def on_env_purge_doc(app, env, docname):
    if not hasattr(env, 'policy_index'):
        return

    env.policy_index = [p for p in env.policy_index
                        if p.docname != docname]


def on_env_merge_info(app, env, docnames, other):
    if not hasattr(other, 'policy_index'):
        return
    if not hasattr(env, 'policy_index'):
        env.policy_index = []

    env.policy_index.extend(other.policy_index)


def setup(app):
    app.connect('doctree-read', on_doctree_read)
    app.connect('env-purge-doc', on_env_purge_doc)
    app.connect('env-merge-info', on_env_merge_info)
    app.add_index_to_domain('std', PolicyIndex)
    return {
        'version': '0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
