f = open('tree.ged', encoding='utf-8')
FamilyList = {}
Person = dict.fromkeys(['name', 'sex'])
for line in f:
    parts = line.split()
    if parts[0] == '0' and parts[-1] == 'INDI':
        key = parts[1]
        FamilyList[key] = dict.copy(Person)
    if parts[0] == '1' and parts[1] == 'NAME':
        Person['name'] = parts[2]
    if parts[0] == '1' and parts[1] == 'SEX':
        Person['sex'] = parts[2]
        FamilyList[key] = dict.copy(Person)
    if parts[0] == '0' and parts[-1] == 'FAM':
        keys = []
    if parts[0] == '1' and parts[1] == 'HUSB':
        keys.append(parts[-1])
    if parts[0] == '1' and parts[1] == 'WIFE':
        keys.append(parts[-1])
    if parts[0] == '1' and parts[1] == 'CHIL':
        child = (FamilyList[parts[2]]['name'])
        for i in keys:
            if 'children' not in FamilyList[i]:
                FamilyList[i]['children'] = list()
            FamilyList[i]['children'].append(child)
f.close()
output = open('tree.pl', 'w', encoding='utf-8')
for i in FamilyList.keys():
    if 'children' in FamilyList[i]:
        for x in FamilyList[i]['children']:
            if FamilyList[i]['sex'] == 'M':
                output.write("father(" + FamilyList[i]['name'].lower() + "," + x.lower() + ").\n")
            else:
                output.write("mother(" + FamilyList[i]['name'].lower() + "," + x.lower() + ").\n")

output.close()

