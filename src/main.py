from models.bfs_community_graph import BfsCommunityGraph


people = ["Patryk", "Kasia", "Kajetan", "Ania", "Artur", "Karolina", "Tomek", "Klaudia", "Krzysiek", "Asia"]

connections = [
    ("Patryk", "Kasia"),
    ("Patryk", "Kajetan"),
    ("Patryk", "Ania"),
    ("Patryk", "Artur"),
    ("Kasia", "Karolina"),
    ("Kasia", "Tomek"),
    ("Kajetan", "Klaudia"),
    ("Kajetan", "Krzysiek"),
    ("Ania", "Asia"),
    ("Ania", "Krzysiek"),
    ("Artur", "Karolina"),
    ("Artur", "Tomek"),
    ("Karolina", "Klaudia"),
    ("Klaudia", "Krzysiek"),
    ("Krzysiek", "Asia")
]

spread_graph = BfsCommunityGraph(debug=True)
spread_graph.make_graph(people, connections)
# spread_graph.random_community(20, 0.2)
order = spread_graph.run()
# spread_graph.draw_connections()
spread_graph.draw_compare()
# spread_graph.draw_spread()
