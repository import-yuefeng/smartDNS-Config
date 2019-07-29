import re

domain_china = open("accelerated-domains.china.conf", "r")
context = domain_china.read()
domains = re.findall(r"\/([\d\s\w\.]+)\/", context)

domain_primary = open("domain_primary", "w+")
for i in domains:
    if 'google' not in i:
        domain_primary.write(i+'\n')
domain_primary.close()
