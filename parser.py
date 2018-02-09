from collections import defaultdict
import json

data = defaultdict(lambda: defaultdict(list))

with open("query.json") as in_file:
	query_results = json.load(in_file)

for r in query_results:
   data[r["linked_movie"]][r["linked_prop"]].append(
	{"name": r["linked_prop_obj"], "image": r["linked_prop_obj_image"]}
   )

   data[r["linked_movie"]]["image"] = r["linked_movie_image"]

ref_data = []

for k in data.keys():
    ref_data.append({
	"name": k,
	"image": data[k]["image"],
		"children": [
			{"name": prop, "children": data[k][prop]}
			for prop in data[k].keys() if prop != "image"
		]
    })

with open("d3_query.json", mode="w") as out_file:
	json.dump(ref_data, out_file)

