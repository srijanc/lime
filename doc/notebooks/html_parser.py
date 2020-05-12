"""
This file will extract all the explaination provided by the LIME
which will then be used for comparision with that of human survey
"""

outfile = open("explained_data/HumanExplainedInstance.txt", "w")

def parsingHTML():
    for i in range(64):
        inputfile = "explained_data/server_data/DataInstance_" + str(i) + ".html"
        with open(inputfile, 'r', encoding='utf-8') as line:
            for hl in line:
                hl = hl.strip()
                if hl.startswith("exp.show_raw_tabular"):
                    # print("Found expression")
                    outfile.write(str(i) + "_" + hl)
                    outfile.write("\n\n")

    # print("Success")
    outfile.close()

def main():
    parsingHTML()

main()
