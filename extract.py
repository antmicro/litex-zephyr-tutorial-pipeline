import tuttest
import sys
snippets = tuttest.get_snippets(sys.argv[1])

code = []
setup = snippets['setup']['text']
import os
if os.path.exists('litex-buildenv'):
    setup = "\n".join(setup.split('\n')[1:])

code.append(setup)
code.append("export HDMI2USB_UDEV_IGNORE=1 SKIP_IMAGE=1")
enter_and_build = snippets['enter and build']['text'].split('\n')
code.append("\n".join(enter_and_build[:-1]))
code.append("make firmware && make bios")
code.append(enter_and_build[-1])

# not testing any other app for now

code.append("export RENODE_NETWORK=none")
code.append(snippets['simulate']['text'] + " --disable-xwt -e s -e 'sleep 20' -e q")

print("\n\n".join(code))
