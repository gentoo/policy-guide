# Handle :PG: policy identifiers for Policy Guide
# (c) 2020 Michał Górny
# 2-clause BSD license

from docutils import nodes

from sphinx.util import logging


logger = logging.getLogger(__name__)


def find_pg_id(section):
    # first child should be title
    title = section.children[0]
    assert isinstance(title, nodes.title)
    # second child should be field list
    cl = section.children[1]
    if not isinstance(cl, nodes.field_list):
        return None

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
            return iv

    logger.warning('%s: no PG identifier found', title.astext())


def on_doctree_read(app, doctree):
    for node in doctree.traverse(nodes.section):
        pg_id = find_pg_id(node)
        if pg_id is not None:
            node['ids'].insert(0, 'pg' + pg_id)


def setup(app):
    app.connect('doctree-read', on_doctree_read)
    return {
        'version': '0',
    }
