"""Step generator script for the annotated Toolkit builders.

For more information, see scripts/slave/annotated_run.py in
https://chromium.googlesource.com/chromium/tools/build/"""

import sys

def GetSteps(api, _factory_properties, build_properties):
  steps = api.Steps(build_properties)
  test_cmd = ['grunt', 'test-buildbot']
  if sys.platform.startswith('linux2'):
    test_cmd = ['xvfb-run'] + test_cmd
  return [
    steps.step('mktmp',
               ['mkdir', '.tmp'],
               cwd=api.checkout_path()),
    steps.step('update-install',
               ['npm', 'install', '--tmp', '.tmp'],
               cwd=api.checkout_path()),
    steps.step('test',
               test_cmd,
               cwd=api.checkout_path()),
  ]
