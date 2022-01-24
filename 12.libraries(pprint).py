from pprint import pprint
import json

f_name = 'bemor.json'

with open(f_name) as f:
    bemor = json.load(f)

#pprint(bemor)

import re 

word1 = 'temir'
word2 = 'tomir'
word3 = 'tulpor'

andoza = '^t...r$'

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))

text = """We are still working out the disposition of those helicopters.
 I do not have an update on any decisions about how they will be handled, but I think
 its safe to assume that they will not be sent into Afghanistan to be used by the Taliban, 
 He also added that a decision on where the equipment will be sent and who will own them is yet to be made.
“As to what they end up doing and where they end up going and who ends up with them, 
we are still working our way through that decision-making process,” the official concluded."""

andoza = '^will$'

will = re.findall(andoza, text)
print(will)
