{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import urllib2\n",
    "import sys\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "def phenotype(s):\n",
    "\n",
    "    iName = re.search(\"\\w.+\",s[1])\n",
    "\n",
    "    return iName.group()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def mutation(s):\n",
    "\n",
    "    mut = re.search(\"\\w.+\",s[2]).group().split(\", \")\n",
    "        \n",
    "    if str(mut).find(\"span\") == -1:\n",
    "\n",
    "        mut2 = mut[1].split()\n",
    "    \n",
    "        data = [mut[0],mut2[0]]\n",
    "        \n",
    "        return data\n",
    "    else:\n",
    "        return \"ERROR\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def SNP(s):\n",
    "\n",
    "    init_snp = s[3].find(\"rs\")\n",
    "    final_snp = s[3].find(\";\",init_snp)\n",
    "\n",
    "    init_clinvar = s[5].find(\"RCV\")\n",
    "    final_clinvar = s[5].find(\"\\\"\",init_clinvar)\n",
    "\n",
    "    clinvar = s[5][init_clinvar:final_clinvar]\n",
    "\n",
    "    if clinvar.find(\"OR\") != -1:\n",
    "        return [s[3][init_snp:final_snp], clinvar.split()[0]]\n",
    "    else:\n",
    "        return [s[3][init_snp:final_snp], clinvar]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LRRK2\trs33939927\tRCV000002013\tARG1441GLY\tPARKINSON DISEASE 8, AUTOSOMAL DOMINANT\n",
      "LRRK2\trs35801418\tRCV000002014\tTYR1699CYS\tPARKINSON DISEASE 8, AUTOSOMAL DOMINANT\n",
      "LRRK2\trs33939927\tRCV000002015\tARG1441CYS\tPARKINSON DISEASE 8, AUTOSOMAL DOMINANT\n",
      "LRRK2\trs34805604\tRCV000002016\tILE1122VAL\tPARKINSON DISEASE 8, AUTOSOMAL DOMINANT\n",
      "LRRK2\trs34637584\tRCV000325492\tGLY2019SER\tPARKINSON DISEASE 8, AUTOSOMAL DOMINANT\n",
      "LRRK2\trs35870237\tRCV000002018\tILE2020THR\tPARKINSON DISEASE 8, AUTOSOMAL DOMINANT\n",
      "LRRK2\trs34995376\tRCV000002019\tARG1441HIS\tPARKINSON DISEASE 8, AUTOSOMAL DOMINANT\n",
      "LRRK2\trs34778348\tRCV000032508\tGLY2385ARG\tPARKINSON DISEASE 8, SUSCEPTIBILITY TO\n"
     ]
    }
   ],
   "source": [
    "def ShowVariant(ID):\n",
    "    site= \"https://www.omim.org/allelicVariant/\" + ID\n",
    "    hdr = {'User-Agent': 'Mozilla/5.0'}\n",
    "    req = urllib2.Request(site,headers=hdr)\n",
    "    page = urllib2.urlopen(req)\n",
    "\n",
    "    code = page.read()\n",
    "\n",
    "    init = code.split(\"<a name=\\\"\")\n",
    "\n",
    "    for i in init[1:]:\n",
    "        sub = i.split(\"<span class=\\\"mim-font\\\">\")\n",
    "    \n",
    "        two_data = mutation(sub)\n",
    "    \n",
    "        if two_data != \"ERROR\":\n",
    "    \n",
    "            print two_data[0] + \"\\t\",\n",
    "            print SNP(sub)[0] + \"\\t\",\n",
    "            print SNP(sub)[1] + \"\\t\",\n",
    "            print two_data[1] + \"\\t\",\n",
    "            print phenotype(sub)\n",
    "        \n",
    "    page.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "infile = open(sys.argv[1])\n",
    "\n",
    "for i in infile.readlines():\n",
    "    ShowVariant(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": false,
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['rs201106962', 'RCV000149507']\n"
     ]
    }
   ],
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
