import json

with open("./iliad.txt") as f:
    lines = f.readlines()

a = []

for line in lines:
    n, text = line.split(" ", 1)
    n = n.replace("[", "").replace("]", "")
    urn = f"urn:cts:greekLit:tlg0012.tlg001:1.{n}"

    a.append({"urn": urn, "text": text.strip()})

with open("./iliad.json", "w") as f:
    json.dump(a, f)
