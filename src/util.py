from pyquery import PyQuery
import urllib3
urllib3.disable_warnings()

member_names = []
url = 'https://www.un.org/en/member-states/'
doc = PyQuery(url, verify=False)
for elem in doc('span.member-state-name'):
    if len(elem.text):
        member_names.append(elem.text)
# info = wb.source.info()
print(member_names)