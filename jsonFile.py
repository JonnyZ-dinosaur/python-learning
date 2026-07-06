import json 

party = [
    {"name": 0 ,
    "extras": [],
    #allows for one person to bring as much people as they want
     "pets": [],
     "gift(s)": [],
     "car": [{"model":0 ,"size":0,"color":0, "year":0, "liscense plate":0}],
     "food": [],
     "allergies": [],
      "comments" : 0,
    },
    {"name": 0,
    "extras": [],
    #allows for one person to bring as much people as they want
     "pets": [],
     "gift(s)": [],
     "car": [{"model":0 ,"size":0,"color":0, "year":0, "liscense plate":0}],
     "food": [],
     "allergies": [],
      "comments" : 0,
    }
]

party[0]["name"] = "Lily"
party[0]["extras"].append("BF")
party[0]["extras"].append("Mom")
party[0]["pets"].append("Dog")
party[0]["gift(s)"].append("Gift one")
party[0]["gift(s)"].append("Gift two")

party[0]["car"][0].update({"model":"Mercedes" ,"size": 20,"color": "blue", "year":2022, "liscense plate":"BDWB24K"})
party[0]["car"].append({"model":"Toyota" ,"size": 5,"color": "red", "year":2023, "liscense plate":"BDKB24K"})

with open("output.json","w") as partyPlan:
    json = json.dump(party, partyPlan)

f = open("output.json","r")
f.read()

