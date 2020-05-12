"""
This is to extract the data from the explanation provided by LIME
for the data which were given in survey for the users to provide
feedback for.
"""

import ast
import collections

infile = "explained_data/HumanExplainedInstance.txt"
outfile = open("explained_data/LimeExplainHuman.csv", "w")

def parsingValues():
  with open(infile, 'r', encoding='utf-8') as surveyLine:
    for i in surveyLine:
      # print(i)
      keyval = {}
      if i == "\n":
        continue

      else:
        for j in ast.literal_eval(str(i).strip("\r\n")):
          # print(j[0] + " ---- " + str(j[2]))
          if "Age" in j[0]:
            # print("Age")
            keyval["Age"] = j[2]

          elif "Workclass" in j[0]:
            # print("Work Class")
            keyval["Work Class"] = j[2]

          elif "Education-Num" in j[0]:
            # print("Education-Num")
            keyval["Education-Num"] = j[2]

          elif "Education" in j[0]:
            # print("Education")
            keyval["Education"] = j[2]

          elif "Marital Status" in j[0]:
            # print("Marital Status")
            keyval["Marital Status"] = j[2]

          elif "Occupation" in j[0]:
            # print("Occupation")
            keyval["Occupation"] = j[2]

          elif "Relationship" in j[0]:
            # print("Relationship")
            keyval["Relationship"] = j[2]

          elif "Capital Gain" in j[0]:
            # print("Capital Gain")
            keyval["Capital Gain"] = j[2]

          elif "Hours per week" in j[0]:
            # print("HoursWeek")
            keyval["HoursWeek"] = j[2]

        odKV = collections.OrderedDict(sorted(keyval.items()))

        for k, v in odKV.items():
          # print(k, v)
        # print()
          outfile.write(str(v))
          outfile.write(",")

        outfile.write("\n")

  outfile.close()
  surveyLine.close()

def main():
  outfile.write("Age,Capital Gain,Education,Education-Num,HoursWeek,Marital Status,Occupation,Relationship,Work Class")
  outfile.write("\n")

  parsingValues()

main()