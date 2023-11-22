from graph import Graph

from ui import UI


def main():
    graph = Graph(0)
    ui = UI(graph)
    ui.start_app()


main()
