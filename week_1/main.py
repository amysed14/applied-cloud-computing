import re
 
file = open("fb_sub.csv","r")
reader = file.read()
company = re.search(r'\w*\sINC\b', reader).group(0)
fout = open("company.txt",'w')
fout.write(company)

file.close()
fout.close()