import math
inputfile = open("day19.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

blueprints = []
for x in lines:
    x = x.split(" ")
    toadd = {}
    toadd["ore"] = int(x[6])
    toadd["clay"] = int(x[12])
    toadd["obsidian"] = int(x[18])
    toadd["geode"] = int(x[27])
    toadd["clayForObsidian"] = int(x[21])
    toadd["obsidianForGeode"] = int(x[30])
    blueprints.append(toadd)
stuff = ("ore","clay","obsidian","geode")

state = ({"ore":1,"clay":0,"obsidian":0,"geode":0},{"ore":0,"clay":0,"obsidian":0,"geode":0},0) # ({robots},{materials},minute)
def findMostGeodes(state):
    global prevbest
    materials = state[1]
    robots = state[0]
    minute = state[2]
    times = {}
    times["ore"] = math.ceil((blueprints[n]["ore"]-materials["ore"])/robots["ore"])+1+minute if robots["ore"]<maxore else 100
    times["clay"] = math.ceil((blueprints[n]["clay"]-materials["ore"])/robots["ore"])+1+minute if robots["clay"]<blueprints[n]["clayForObsidian"] else 100
    times["obsidian"] = max(math.ceil((blueprints[n]["obsidian"]-materials["ore"])/robots["ore"])+1,math.ceil((blueprints[n]["clayForObsidian"]-materials["clay"])/robots["clay"])+1)+minute if robots["clay"]>0 and robots["obsidian"]<blueprints[n]["obsidianForGeode"] else 100
    times["geode"] = max(math.ceil((blueprints[n]["geode"]-materials["ore"])/robots["ore"])+1,math.ceil((blueprints[n]["obsidianForGeode"]-materials["obsidian"])/robots["obsidian"])+1)+minute if robots["obsidian"]>0 else 100
    if materials["geode"] + (robots["geode"]+robots["geode"]+(24-minute))/2*(24-minute) <= prevbest:
        times["ore"] = 100
        times["clay"] = 100
        times["obsidian"] = 100
        times["geode"] = 100
    for time in times:
        if times[time] < minute+1:
            times[time] = minute + 1
    geodes = []
    for option in times:
        if times[option] < 25:
            toadd = ({"ore":robots["ore"],"clay":robots["clay"],"obsidian":robots["obsidian"],"geode":robots["geode"]},{"ore":materials["ore"],"clay":materials["clay"],"obsidian":materials["obsidian"],"geode":materials["geode"]},times[option])
            toadd[0][option] += 1
            for i in toadd[1]:
                toadd[1][i] += robots[i]*(times[option]-minute)
            toadd[1]["ore"] -= blueprints[n][option]
            toadd[1]["clay"] = toadd[1]["clay"] - blueprints[n]["clayForObsidian"] if option == "obsidian" else toadd[1]["clay"]
            toadd[1]["obsidian"] = toadd[1]["obsidian"] - blueprints[n]["obsidianForGeode"] if option == "geode" else toadd[1]["obsidian"]
            geodes.append(findMostGeodes(toadd))
        else:
            geodes.append(materials["geode"] + (24-minute)*robots["geode"])
    best = max(geodes)
    if best>prevbest:
        prevbest=best
    return best

results = []
for n in range(len(lines)):
    maxore = max([blueprints[n][a] for a in stuff])
    prevbest = 0
    results.append(findMostGeodes(state))

result = 0
for i,j in enumerate(results):
    result += (i+1)*j
print(result)