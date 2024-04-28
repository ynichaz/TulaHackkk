from pyvis.network import Network

net = Network()  # создаём объект графа

# добавление узлов
net.add_nodes(
    [1, 2, 3, 4, 5, 6, 7],  # node ids
    label=['Node #1', 'Node #2', 'Node #3', 'Node #4', 'Node #5', "6", "7"],  # node labels
    # node titles (display on mouse hover)
    title=['Main node', 'Just node', 'Just node', 'Just node', 'Node with self-loop', 'Just node', 'Just node'],
    color=['#d47415', '#22b512', '#42adf5', '#4a21b0', '#e627a3', '#e627a3', '#e627a3']  # node colors (HEX)
)
# добавляем тот же список узлов, что и в предыдущем примере
net.add_edge(1, 2, title="fcfc")
net.add_edges([(1, 3), (2, 4), (3, 5), (2, 6), (3, 7)])
net.set_options("""
const options = {
  "nodes": {
    "borderWidth": 2,
    "borderWidthSelected": 3,
    "opacity": 1,
    "size": 5
  },
  "edges": {
    "color": {
      "inherit": true
    },
    "selfReferenceSize": null,
    "selfReference": {
      "angle": 0.7853981633974483
    },
    "smooth": false
  },
  "layout": {
    "hierarchical": {
      "enabled": true,
      "sortMethod": "directed"
    }
  },
  "physics": {
    "hierarchicalRepulsion": {
      "centralGravity": 0,
      "avoidOverlap": null
    },
    "minVelocity": 0.75,
    "solver": "hierarchicalRepulsion"
  }
}""")
# net.show_buttons()

net.show('graph.html', notebook=False)

print(net)
p = str(net)



# import sqlite3
#
# #создание бд и таблицы опроса
# with sqlite3.connect('/Users/varya_kurkubet/Desktop/database.db') as db:
#     cursor = db.cursor()
#     query = """ CREATE TABLE IF NOT EXISTS opros (id INTEGER PRIMARY KEY, admin_id INTEGER, graph TEXT NOT NULL) """
#     cursor.execute(query)
#     cursor.execute('INSERT INTO opros (graph) VALUES (?)', (p,))
#
# db.close()



