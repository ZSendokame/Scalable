from .nodes import *


class SVG:
    def __init__(self, output: str = None, height=500, width=500):
        self.output = output
        self.svg = f'<svg height="{height}" width="{width}">\n'

    def circle(self, **attrs) -> Circle:
        node = Circle()
        self.svg += node.tag(**attrs) + '\n'

        return node

    def rectangle(self, **attrs) -> Rectangle:
        node = Rectangle()
        self.svg += node.tag(**attrs) + '\n'

        return node

    def text(self, text: str, **attrs) -> Text:
        node = Text()
        self.svg += node.tag(text, **attrs) + '\n'

        return node

    def line(self, **attrs) -> Line:
        node = Line()
        self.svg += node.tag(**attrs) + '\n'

        return node

    def polyline(self, **attrs) -> Polyline:
        node = Polyline()
        self.svg += node.tag(**attrs) + '\n'

        return node

    def ellipse(self, **attrs) -> Ellipse:
        node = Ellipse()
        self.svg += node.tag(**attrs) + '\n'

        return node

    def save(self) -> None:
        self.svg += '</svg>'

        if self.output is not None:
            with open(self.output, 'w') as output:
                output.write(self.svg)

        return self.svg
