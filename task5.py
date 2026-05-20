class LightNode:
    def inner_html(self):
        pass

    def outer_html(self):
        pass

class LightTextNode(LightNode):
    def __init__(self, text):
        self.text = text

    def inner_html(self):
        return self.text

    def outer_html(self):
        return self.text

class LightElementNode(LightNode):
    def __init__(self, tag, display_type, closure_type, css_classes=None):
        self.tag = tag
        self.display_type = display_type
        self.closure_type = closure_type
        self.css_classes = css_classes if css_classes else []
        self.children = []
        self.events = {}

    def add_child(self, node):
        self.children.append(node)

    def add_event_listener(self, event_type, callback):
        if event_type not in self.events:
            self.events[event_type] = []
        self.events[event_type].append(callback)

    def trigger(self, event_type):
        if event_type in self.events:
            for callback in self.events[event_type]:
                callback()

    def inner_html(self):
        result = ""
        for child in self.children:
            result += child.outer_html()
        return result

    def outer_html(self):
        classes_str = ""
        if self.css_classes:
            classes_str = ' class="' + " ".join(self.css_classes) + '"'

        if self.closure_type == "single":
            return "<" + self.tag + classes_str + "/>"

        start_tag = "<" + self.tag + classes_str + ">"
        end_tag = "</" + self.tag + ">"

        if self.display_type == "block":
            inner = ""
            for child in self.children:
                inner += "\n  " + child.outer_html().replace("\n", "\n  ")
            return start_tag + inner + "\n" + end_tag

        return start_tag + self.inner_html() + end_tag

if __name__ == "__main__":
    button = LightElementNode("button", "inline", "pair", ["btn-submit"])
    button.add_child(LightTextNode("Click Me!"))

    def on_click_handler():
        print("Observer notification: Button was clicked!")

    def on_hover_handler():
        print("Observer notification: Mouse hover detected!")

    button.add_event_listener("click", on_click_handler)
    button.add_event_listener("mouseover", on_hover_handler)

    print("--- Current Button HTML ---")
    print(button.outer_html())

    print("\n--- Simulating User Events ---")
    button.trigger("click")
    button.trigger("mouseover")