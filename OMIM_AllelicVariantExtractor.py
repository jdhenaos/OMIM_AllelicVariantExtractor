
# coding: utf-8

# In[1]:

import urllib2
import sys
import re


# In[2]:

def phenotype(s):

    iName = re.search("\w.+",s[1])

    return iName.group()


# In[3]:

def mutation(s):

    mut = re.search("\w.+",s[2]).group().split(", ")
        
    if str(mut).find("span") == -1:

        mut2 = mut[1].split()
    
        data = [mut[0],mut2[0]]
        
        return data
    else:
        return "ERROR"


# In[4]:

def SNP(s):

    init_snp = s[3].find("rs")
    final_snp = s[3].find(";",init_snp)

    init_clinvar = s[5].find("RCV")
    final_clinvar = s[5].find("\"",init_clinvar)

    clinvar = s[5][init_clinvar:final_clinvar]

    if clinvar.find("OR") != -1:
        return [s[3][init_snp:final_snp], clinvar.split()[0]]
    else:
        return [s[3][init_snp:final_snp], clinvar]


# In[7]:

def ShowVariant(ID):
    site= "https://www.omim.org/allelicVariant/" + ID
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site,headers=hdr)
    page = urllib2.urlopen(req)

    code = page.read()

    init = code.split("<a name=\"")

    for i in init[1:]:
        sub = i.split("<span class=\"mim-font\">")
    
        two_data = mutation(sub)
    
        if two_data != "ERROR":
    
            print two_data[0] + "\t",
            print SNP(sub)[0] + "\t",
            print SNP(sub)[1] + "\t",
            print two_data[1] + "\t",
            print phenotype(sub)
        
    page.close()


# In[ ]:

infile = open(sys.argv[1])

for i in infile.readlines():
    ShowVariant(i)


# In[45]:



