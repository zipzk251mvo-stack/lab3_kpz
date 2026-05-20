import sys


class LightElementState:
    def __init__(self, tag, display_type, closure_type):
        self.tag = tag
        self.display_type = display_type
        self.closure_type = closure_type


class LightNodeFactory:
    _types = {}

    @classmethod
    def get_element_type(cls, tag, display_type, closure_type):
        key = (tag, display_type, closure_type)
        if key not in cls._types:
            cls._types[key] = LightElementState(tag, display_type, closure_type)
        return cls._types[key]


class FlyweightLightElementNode:
    def __init__(self, tag, display_type, closure_type, text):
        self.state = LightNodeFactory.get_element_type(tag, display_type, closure_type)
        self.text = text

    def outer_html(self):
        if self.state.closure_type == "single":
            return "<" + self.state.tag + "/>"

        start_tag = "<" + self.state.tag + ">"
        end_tag = "</" + self.state.tag + ">"

        if self.state.display_type == "block":
            return start_tag + "\n  " + self.text + "\n" + end_tag
        return start_tag + self.text + end_tag


class StandardLightElementNode:
    def __init__(self, tag, display_type, closure_type, text):
        self.tag = tag
        self.display_type = display_type
        self.closure_type = closure_type
        self.text = text

    def outer_html(self):
        start_tag = "<" + self.tag + ">"
        end_tag = "</" + self.tag + ">"
        if self.display_type == "block":
            return start_tag + "\n  " + self.text + "\n" + end_tag
        return start_tag + self.text + end_tag


if __name__ == "__main__":
    book_lines = [
        "ROMEO AND JULIET",
        "ACT V",
        "Scene I. Mantua. A Street.",
        "  Enter ROMEO.",
        "If I may trust the flattering truth of sleep,",
        "My dreams presage some joyful news at hand."
    ]

    standard_nodes = []
    for i, line in enumerate(book_lines):
        if i == 0:
            node = StandardLightElementNode("h1", "block", "pair", line)
        elif len(line) < 20:
            node = StandardLightElementNode("h2", "block", "pair", line)
        elif line.startswith(" ") or line.startswith("\t"):
            node = StandardLightElementNode("blockquote", "block", "pair", line.strip())
        else:
            node = StandardLightElementNode("p", "block", "pair", line)
        standard_nodes.append(node)

    flyweight_nodes = []
    for i, line in enumerate(book_lines):
        if i == 0:
            node = FlyweightLightElementNode("h1", "block", "pair", line)
        elif len(line) < 20:
            node = FlyweightLightElementNode("h2", "block", "pair", line)
        elif line.startswith(" ") or line.startswith("\t"):
            node = FlyweightLightElementNode("blockquote", "block", "pair", line.strip())
        else:
            node = FlyweightLightElementNode("p", "block", "pair", line)
        flyweight_nodes.append(node)

    print("--- HTML Output Example ---")
    print(flyweight_nodes[2].outer_html())

    print("\n--- Memory Benchmarks ---")
    standard_memory = sum(sys.getsizeof(n) + sys.getsizeof(n.__dict__) for n in standard_nodes)
    flyweight_memory = sum(sys.getsizeof(n) + sys.getsizeof(n.__dict__) for n in flyweight_nodes)

    print("Standard nodes memory usage: " + str(standard_memory) + " bytes")
    print("Flyweight nodes memory usage: " + str(flyweight_memory) + " bytes")