import re
snt, sub = input(), input()
matches = list(re.finditer(r'(?={})'.format(sub), snt))
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(sub) - 1)) for match in matches))
else:
    print('(-1, -1)')