from jinja2 import Environment, PackageLoader
from html2text import html2text
from graphviz.backend import ExecutableNotFound


env = Environment(
    loader=PackageLoader('dephell', 'templates'),
)


def analize_conflict(resolver):
    try:
        resolver.graph.draw()
    except ExecutableNotFound:
        print('GraphViz is not installed yet.')

    template = env.get_template('state.html.j2')
    content = template.render(
        conflict=resolver.graph.conflict,
        graph=resolver.graph,
        mutator=resolver.mutator,
    )
    return html2text(content)
