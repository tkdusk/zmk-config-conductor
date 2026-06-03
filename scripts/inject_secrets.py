import os
import sys

secret = os.environ.get('ENTER_PASS_BINDINGS', '')
if not secret:
    print('ERROR: ENTER_PASS_BINDINGS secret is not set', file=sys.stderr)
    sys.exit(1)

path = 'config/monokey.keymap'
with open(path) as f:
    content = f.read()

if 'ENTER_PASS_PH' not in content:
    print('ERROR: placeholder ENTER_PASS_PH not found in keymap', file=sys.stderr)
    sys.exit(1)

with open(path, 'w') as f:
    f.write(content.replace('ENTER_PASS_PH', secret))

print('Secret macro injected.')
