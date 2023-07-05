with open("/home/lpreimesberger/Desktop/Adjectives.csv", "rt") as handle:
    lines =handle.readlines()
    for line in lines:
        try:
            line = line.strip().split(', ')[1]
            print(f"\t'{line}',")
        except:
            pass
