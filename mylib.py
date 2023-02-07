import re

def drop_teg(teg, data):
    """
    params: teg = str, data = str
    enter <, >, / without symbols in the tag parameter
    """

    match = f"<{teg}.*</{teg}>"
    indexs = re.search(match, data)
    try:
        indexs = list(indexs.span())
        return data.replace(data[indexs[0] : indexs[1]], "")
    except:
        return data



# data = "The ozone layer absorbs 97 to 99 percent of the Sun's medium-frequency ultraviolet light (from about 200&nbsp;[[nanometer|nm]] to 315&nbsp;nm [[wavelength]]), which otherwise would potentially damage exposed life forms near the surface.<ref name="NASA">{{cite web|url=http://www.nas.nasa.gov/About/Education/Ozone/ozonelayer.html |title=Ozone layer|access-date=2007-09-23}}</ref>_______"
# print(drop_teg("ref", data))


def drop_tegs(tegs, data):
    """
    params: teg = str, data = str
    enter <, >, / without symbols in the tag parameter
    """
    for teg in tegs:
        match = f"<{teg}.*</{teg}>"
        indexs = re.search(match, data)
        try:
            indexs = list(indexs.span())
            data = data.replace(data[indexs[0] : indexs[1]], "")
        except:
            continue
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



def replaces(replaces, put, data):
    """
    params: replaces = list, put = str, data = str;
    This functio can replace many elements;
    """
    for rep in replaces:
        data = data.replace(rep, put)
    return data