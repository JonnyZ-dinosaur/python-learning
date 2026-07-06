import json

party = json.load(open("output.json","r"))
print(party)

party[1]["name"] = "Timothy"
party[1]["extras"].append("Dad")
party[1]["extras"].append("GF")
party[1]["gift(s)"].append("Gift 1")
party[1]["car"][0].update({"model": "Tesla","size": 4, "color": "purple", "year": 2017, "liscence plate": "BDHIA284H"})

print(party)

with open("output.json","w") as partyPlan:
    json = json.dump(party,partyPlan)

 