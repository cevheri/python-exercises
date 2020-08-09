# python sys module

import sys

print(dir(sys))
"""['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__',
 '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework', '_getframe', '_git', '_home', '_xoptions',
 'abiflags', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook',
 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode',
 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getcheckinterval',
 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion',
 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks',
 'set_coroutine_origin_tracking_depth', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version',
 'version_info', 'warnoptions']
"""

# sys.exit()

sayı = 0

if int(sayı) < 0:
    print('çıkılıyor...')
    sys.exit()

else:
    print(sayı)

print(sys.argv)

# exapmle
import sys


def custom_exit():
    print('You did not enter the required parameters!')
    # sys.exit()


if len(sys.argv) < 2:
    print('You entered too many parameters!')
    custom_exit()
elif len(sys.argv) > 2:
    print('You entered too many parameters!')
    custom_exit()
elif sys.argv[1] in ['-v', '-V']:
    print('Program version: 0.8')
else:
    message = 'The parameter ({}) you entered could not be understood!'
    print(message.format(sys.argv[1]))
    custom_exit()

print()
#######################333
print("sys.executable")
print(sys.executable)
print()
############################3
print("sys.getwindowsversion()")  # for windows
# print(sys.getwindowsversion())

print()
print("sys.platform")
print(sys.platform)  # linux

print()
print(sys.prefix)
# /home/cevher/anaconda3/envs/python-exercises


print()
print(sys.version)
# 3.8.3 (default, Jul  2 2020, 16:21:59)
# [GCC 7.3.0]

print(sys.version_info)
# sys.version_info(major=3, minor=8, micro=3, releaselevel='final', serial=0)
print()

print(sys.stdout)
# <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>

f = open('output.txt', 'w')
print('Hello World', file=f)
# or

f = open('output.txt', 'w')
# sys.stdout = f
sys.stdout.write('Hello World')

f = open('errors.txt', 'w')
sys.stderr = f
# sys.stderr.write(1 / 0)

outputs = open('outputs.txt', 'w')
errors = open('errors.txt', 'w')
sys.stdout = outputs
sys.stderr = errors

print('Hello World')
# print('Exception Message: ', 1 / 0)

# sys.stdout = None

print("sys.stdin.read() === input()")

import sys

# with open('outputs.txt', 'w') as records:
#     while True:
#         lines = sys.stdin.readline()
#         if lines.strip() == ':q':
#             break
#         else:
#             records.write(lines)
