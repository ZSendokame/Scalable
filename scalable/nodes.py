def to_str(iterable: list) -> list[str]:
    return [str(item) for item in iterable]


class Node:
    def __str__(self, tag: str, attrs: dict, text: str = None) -> str:
        result = '<' + tag

        for attr, value in attrs.items():
            attr = attr.replace('_', '-')

            if isinstance(value, list):
                value = ', '.join(
                    str(item) if not isinstance(item, tuple)
                    else ' '.join(to_str(item))
                    for item in value
                )

            result += f' {attr}="{value}"'

        return result + ('>' if text is None else '>' + text) + f'</{tag}>'


class Circle(Node):
    def tag(self, **attrs) -> str:
        return self.__str__('circle', attrs)


class Rectangle(Node):
    def tag(self, **attrs) -> str:
        return self.__str__('rect', attrs)


class Text(Node):
    def tag(self, text: str, **attrs) -> str:
        return self.__str__('text', attrs, text)


class Line(Node):
    def tag(self, **attrs) -> str:
        return self.__str__('line', attrs)


class Polyline(Node):
    def tag(self, **attrs) -> str:
        return self.__str__('polyline', attrs)


class Polygon(Node):
    def tag(self, **attrs) -> str:
        return self.__str__('polygon', attrs)


class Ellipse(Node):
    def tag(self, **attrs) -> str:
        return self.__str__('ellipse', attrs)


class Tspan(Node):
    def tag(self, text: str, **attrs) -> str:
        return self.__str__('tspan', attrs, text)
