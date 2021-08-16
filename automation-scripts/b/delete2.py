

lines = open("delete.py", "r").readlines()
ret = []
for _ in lines:

    if len(_) < 5:
        continue

    if "=" not in _ and "|" not in _ and "[" not in _:

        if len(_) > 42:

            x = len(_)//42 - 1

            for ix in range(x):

                
                sliced = _[ix*42 : (ix+1)*42].replace("\n ","").replace("\n","").replace("\\n","").replace("\t","").replace("\\t","").replace("\\","").replace("'","").replace('"',"").replace("\'","").replace("`","").replace("\"","").strip()
                y = sliced.split()

                if "." in y[-1]:
                    z = y
                else:
                    z = y[:-1]
                
                if not y[0][0].isupper():
                    b = z[1:]
                else:
                    b = z
                
                b = " ".join(b)

                if len(b.split(".")) > 1:
                    if len(b.split(".")[0]) > len(b.split(".")[1]):
                        rets = b.split(".")[0]
                    else:
                        rets = " ".join(
                            b.split(".")[1:]
                        )
                else:
                    rets = b

                ret.append(rets)
        else:
            ret.append(_.replace("\n","").replace("\\n","").replace("\t","").replace("\\t","").replace("\\","").replace("'","").replace('"',"").strip())



xdf = open("output.txt", "w")

for _ in ret:
    xdf.write('"')
    xdf.write(
        _.replace("!","").replace(".","").replace("?","").replace(",","").replace(":","").replace(";","").replace("&", "").strip()
    )
    xdf.write('",')
    xdf.write("\n")
xdf.close()
