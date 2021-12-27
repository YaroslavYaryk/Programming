class Editor(object):

    def view_document(self):
        return f"View Document"

    def edit_document(self):
        return f"it's impossible to see"

class ProEditor(Editor):
    def edit_document(self):
        return f"you can see the text"


def main(u):
    if u == 111:
        editor = ProEditor()

    else:
        editor = Editor()
    print(editor.edit_document())

if __name__ == '__main__':
    u = int(input(":"))

    main(u)