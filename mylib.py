import re

def drop_tegs(tegs, data):

    index = 0
    while True:
        if index != len(tegs):
            teg = tegs[index]
            match = f"<{teg}.*</{teg}>"
            loc = re.search(match, data)
            if loc:
                loc = list(loc.span())
                data = data.replace(data[loc[0] : loc[1]], "")
            else:
                index+=1
        else:
            break
    return data


def drop_ab(abdict, data):
    """
    params: abdict = list[dict], data = str ;
    This is function replace characters from a to b;
    """
    for key in abdict.keys():
        match = f"{key}.*{abdict[key]}"
        indexs = re.search(match, data)

        try:
            indexs = list(indexs.span())
            data = data.replace(data[indexs[0] : indexs[1]], "")
        except:
            continue

    return data



# txt = "|||||AAA____________________BBB|||||||||VVV_____________________VVV|||||"
# params = {"AAA" : "BBB", "VVV" : "VVV"}
# print(drop_ab(params, txt))



def drops(elements, put, data):
    for rep in elements:
        data = data.replace(rep, put)
    return data
