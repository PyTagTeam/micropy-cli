# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_pylint_template 1'] = '''[MASTER]
# Loaded Stubs: esp32-micropython-1.11.0, esp8266-micropython-1.9.4
init-hook=\'import sys;sys.path[1:1] = [".micropy/stubs/esp32_test_stub/stubs", ".micropy/stubs/esp8266_test_stub/stubs", ".micropy/stubs/esp32_test_stub/frozen", ".micropy/stubs/esp8266_test_stub/frozen", ".micropy/stubs/fware_test_stub/frozen", ".micropy/stubs/fware_test_stub/frozen"]\'

[MESSAGES CONTROL]
# Only show warnings with the listed confidence levels. Leave empty to show
# all. Valid levels: HIGH, INFERENCE, INFERENCE_FAILURE, UNDEFINED.
confidence=

# Disable the message, report, category or checker with the given id(s). You
# can either give multiple identifiers separated by comma (,) or put this
# option multiple times (only on the command line, not in the configuration
# file where it should appear only once). You can also use "--disable=all" to
# disable everything first and then reenable specific checks. For example, if
# you want to run only the similarities checker, you can use "--disable=all
# --enable=similarities". If you want to run only the classes checker, but have
# no Warning level messages displayed, use "--disable=all --enable=classes
# --disable=W".

disable = missing-docstring, line-too-long, trailing-newlines, broad-except, logging-format-interpolation, invalid-name, empty-docstring,
        no-method-argument, assignment-from-no-return, too-many-function-args, unexpected-keyword-arg
        # the 2nd  line deals with the limited information in the generated stubs.'''

snapshots['test_pylint_template 2'] = '''[MASTER]
# Loaded Stubs: esp32-micropython-1.11.0, esp8266-micropython-1.9.4
init-hook=\'import sys;sys.path[1:1] = [".micropy/stubs/esp32_test_stub/stubs", ".micropy/stubs/esp8266_test_stub/stubs", ".micropy/stubs/esp32_test_stub/frozen", ".micropy/stubs/esp8266_test_stub/frozen", ".micropy/stubs/fware_test_stub/frozen", ".micropy/stubs/fware_test_stub/frozen", ".micropy/foobar/foo"]\'

[MESSAGES CONTROL]
# Only show warnings with the listed confidence levels. Leave empty to show
# all. Valid levels: HIGH, INFERENCE, INFERENCE_FAILURE, UNDEFINED.
confidence=

# Disable the message, report, category or checker with the given id(s). You
# can either give multiple identifiers separated by comma (,) or put this
# option multiple times (only on the command line, not in the configuration
# file where it should appear only once). You can also use "--disable=all" to
# disable everything first and then reenable specific checks. For example, if
# you want to run only the similarities checker, you can use "--disable=all
# --enable=similarities". If you want to run only the classes checker, but have
# no Warning level messages displayed, use "--disable=all --enable=classes
# --disable=W".

disable = missing-docstring, line-too-long, trailing-newlines, broad-except, logging-format-interpolation, invalid-name, empty-docstring,
        no-method-argument, assignment-from-no-return, too-many-function-args, unexpected-keyword-arg
        # the 2nd  line deals with the limited information in the generated stubs.'''