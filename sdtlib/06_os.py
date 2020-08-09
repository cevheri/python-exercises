# os module
import os

print(dir(os))
# ['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'DirEntry',
# 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST',
# 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR',
# 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL',
# 'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK', 'F_TEST',
# 'F_TLOCK', 'F_ULOCK', 'MutableMapping', 'NGROUPS_MAX', 'O_ACCMODE',
# 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECT', 'O_DIRECTORY',
# 'O_DSYNC', 'O_EXCL', 'O_LARGEFILE', 'O_NDELAY', 'O_NOATIME', 'O_NOCTTY',
# 'O_NOFOLLOW', 'O_NONBLOCK', 'O_RDONLY', 'O_RDWR', 'O_RSYNC', 'O_SYNC',
# 'O_TRUNC', 'O_WRONLY', 'POSIX_FADV_DONTNEED', 'POSIX_FADV_NOREUSE',
# 'POSIX_FADV_NORMAL', 'POSIX_FADV_RANDOM', 'POSIX_FADV_SEQUENTIAL',
# 'POSIX_FADV_WILLNEED', 'POSIX_SPAWN_CLOSE', 'POSIX_SPAWN_DUP2',
# 'POSIX_SPAWN_OPEN', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL',
# 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'PathLike',
# 'RTLD_DEEPBIND', 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE',
# 'RTLD_NOLOAD', 'RTLD_NOW', 'R_OK', 'SCHED_BATCH', 'SCHED_FIFO',
# 'SCHED_IDLE', 'SCHED_OTHER', 'SCHED_RESET_ON_FORK', 'SCHED_RR', 'SEEK_CUR',
# 'SEEK_END', 'SEEK_SET', 'ST_APPEND', 'ST_MANDLOCK', 'ST_NOATIME', 'ST_NODEV',
# 'ST_NODIRATIME', 'ST_NOEXEC', 'ST_NOSUID', 'ST_RDONLY', 'ST_RELATIME',
# 'ST_SYNCHRONOUS', 'ST_WRITE', 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED',
# 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG',
# 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'XATTR_CREATE',
# 'XATTR_REPLACE', 'XATTR_SIZE_MAX', 'X_OK', '_Environ', '__all__', '__builtins__',
# '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
# '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_fwalk',
# '_get_exports_list', '_putenv', '_spawnvef', '_unsetenv', '_wrap_close', 'abc',
# 'abort', 'access', 'altsep', 'chdir', 'chmod', 'chown', 'chroot', 'close',
# 'closerange', 'confstr', 'confstr_names', 'cpu_count', 'ctermid', 'curdir',
# 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'environb',
# 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp',
# 'execvpe', 'extsep', 'fchdir', 'fchmod', 'fchown', 'fdatasync', 'fdopen', 'fork',
# 'forkpty', 'fpathconf', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fstatvfs',
# 'fsync', 'ftruncate', 'fwalk', 'get_blocking', 'get_exec_path', 'get_inheritable',
# 'get_terminal_size', 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid',
# 'getgid', 'getgrouplist', 'getgroups', 'getloadavg', 'getlogin', 'getpgid',
# 'getpgrp', 'getpid', 'getppid', 'getpriority', 'getresgid', 'getresuid', 'getsid',
# 'getuid', 'getxattr', 'initgroups', 'isatty', 'kill', 'killpg', 'lchown', 'linesep', '
# link', 'listdir', 'listxattr', 'lockf', 'lseek', 'lstat', 'major', 'makedev',
# 'makedirs', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty',
# 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'pipe2', 'popen',
# 'posix_fadvise', 'posix_fallocate', 'posix_spawn', 'posix_spawnp', 'pread', 'preadv',
# 'putenv', 'pwrite', 'pwritev', 'read', 'readlink', 'readv', 'register_at_fork', 'remove',
# 'removedirs', 'removexattr', 'rename', 'renames', 'replace', 'rmdir', 'scandir',
# 'sched_get_priority_max', 'sched_get_priority_min', 'sched_getaffinity', 'sched_getparam',
# 'sched_getscheduler', 'sched_param', 'sched_rr_get_interval', 'sched_setaffinity',
# 'sched_setparam', 'sched_setscheduler', 'sched_yield', 'sendfile', 'sep', 'set_blocking',
# 'set_inheritable', 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp',
# 'setpriority', 'setregid', 'setresgid', 'setresuid', 'setreuid', 'setsid', 'setuid',
# 'setxattr', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp',
# 'spawnvpe', 'st', 'stat', 'stat_result', 'statvfs', 'statvfs_result', 'strerror',
# 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd',
# 'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names',
# 'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate',
# 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime',
# 'wait', 'wait3', 'wait4', 'waitid', 'waitid_result', 'waitpid', 'walk', 'write', 'writev']


print(os.name)  # posix
print(os.sep)  # /

# get current directory
print(os.getcwd())  # /home/cevher/projects/python-projects/python-exercises/sdtlib

# change directory
# os.chdir("/usr/bin")

# list current directory and files
print(os.listdir(os.getcwd()))
print(os.listdir('.'))
print(os.listdir(os.curdir))
# ['06_os.py', '04_random.py', '01_regular_expressions_2.py',
# '05_sqlite.py', '02_datetime.py', '01_regular_expressions.py',
# 'data', '03_math.py']

# parent directory
print(os.listdir('..'))
print(os.listdir(os.pardir))

# list of "*.py"
for i in os.listdir(os.getcwd()):
    if i.endswith('.py'):
        print(i)

# for windows
"""
os.startfile(os.getcwd())
os.startfile('.')
os.startfile(os.curdir)

os.startfile('test.docx')
os.startfile('test.txt')

os.startfile(os.pardir)
os.startfile('..')
os.startfile(r"C:\Documents and Settings\cevher")
os.startfile('www.python.com')
"""

# create directory
# os.mkdir("test")
# os.mkdir('/home/cevher/Desktop/test')

# create parent and sub directories
# os.mkdir('/home/cevher/Desktop/test/test1/tes2')

# rename directory
# os.rename("test", "new test")
# os.replace("new test","test")

# remove files
# os.remove("test.txt")

# remove blank directory
# os.rmdir("new test")

# remove all directory
# os.removedirs("test")

f = os.stat("06_os.py")
print(f)
# os.stat_result(
# st_mode=33204,
# st_ino=11176438,
# st_dev=66314,
# st_nlink=1,
# st_uid=1000,
# st_gid=1000,
# st_size=5792,
# st_atime=1596907665,
# st_mtime=1596907665,
# st_ctime=1596907665)
dir(f)
f.st_size
# st_atime : fileya en son erişilme tarihi
# st_ctime : filenın oluşturulma tarihi (Windows’ta)
# st_mtime : filenın son değiştirilme tarihi
# st_size  : filenın boyutu

# open app
# os.system("gedit")
# os.system("notepad.exe")

# random byte array
print(os.urandom(12))  # b'bWa\x8d~T\x1fF\x88\x1a\xce\xac'


# list nested directories
# bad way
def scan(directory):
    start = os.pardir
    files = []
    os.chdir(directory)

    for element in os.listdir(os.curdir):
        if not os.path.isdir(element):
            files.append(element)
        else:
            files.extend(scan(element))
    os.chdir(start)
    return files


print(scan("."))
print()
################
# os.walk()
# +main_directory
#     |file.txt
#     |file.doc
#     |file.xls
#     |file.jpeg
#     +images
#         |resim1.jpeg
#         |resim2.jpeg
#         |resim3.jpeg
#         |resim4.jpeg
#         +other_files
#             |file.pdf
#             |file.zip
#             |file.mp3
#             |file.ogg
#             |file.jpeg

# create the template above
# file_types = ['txt', 'doc', 'xls',
#               'jpeg', 'pdf', 'zip',
#               'mp3', 'ogg', 'jpeg']
#
# template1 = ['{}.{}'.format('file', i) for i in file_types[:4]]
# template2 = ['image{}.{}'.format(i, file_types[-1]) for i in range(1, 5)]
# template3 = ['{}.{}'.format('file', i) for i in file_types[4:]]
#
# files = [('main_directory', template1),
#          ('images', template2),
#          ('other_files', template3)]
#
# os.makedirs(os.sep.join([file[0] for file in files]))
#
# for directory, template in files:
#     for s in template:
#         open(os.sep.join([directory, s]), 'w')
#     os.chdir(directory)

for i in os.walk('main_directory'):
    print(i)
# ('main_directory', ['images'], ['file.jpeg', 'file.doc', 'file.txt', 'file.xls'])
# ('main_directory/images', ['other_files'], ['image1.jpeg', 'image3.jpeg', 'image4.jpeg', 'image2.jpeg'])
# ('main_directory/images/other_files', [], ['file.pdf', 'file.mp3', 'file.jpeg', 'file.zip', 'file.ogg'])

for root_dir, sub_dir, files in os.walk("main_directory"):
    print(files)
# ['file.jpeg', 'file.doc', 'file.txt', 'file.xls']
# ['image1.jpeg', 'image3.jpeg', 'image4.jpeg', 'image2.jpeg']
# ['file.pdf', 'file.mp3', 'file.jpeg', 'file.zip', 'file.ogg']

for root_dir, sub_dir, files in os.walk("main_directory"):
    print(root_dir)
# main_directory
# main_directory/images
# main_directory/images/other_files

for root_dir, sub_dir, files in os.walk("main_directory"):
    print(sub_dir)
# ['images']
# ['other_files']
# []

for root_dir, sub_dir, files in os.walk("main_directory"):
    for f in files:
        print(os.sep.join([root_dir, f]))  # TODO : yol > kökdizin

# main_directory/file.jpeg
# main_directory/file.doc
# main_directory/file.txt
# main_directory/file.xls
# main_directory/images/image1.jpeg
# main_directory/images/image3.jpeg
# main_directory/images/image4.jpeg
# main_directory/images/image2.jpeg
# main_directory/images/other_files/file.pdf
# main_directory/images/other_files/file.mp3
# main_directory/images/other_files/file.jpeg
# main_directory/images/other_files/file.zip
# main_directory/images/other_files/file.ogg


for root_dir, sub_dir, files in os.walk("main_directory"):
    for f in files:
        if f.endswith(".jpeg"):
            print(f)
# file.jpeg
# image1.jpeg
# image3.jpeg
# image4.jpeg
# image2.jpeg
# file.jpeg

# operation system environment
# !!! differs in operating systems

for k, v in os.environ.items():
    print(k.ljust(10), v)

# PATH       /home/cevher/anaconda3/envs/python-exercises/bin:/home/cevher/anaconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/cevher/.dotnet/tools
# LC_MEASUREMENT tr_TR.UTF-8
# XAUTHORITY /home/cevher/.Xauthority
# LC_TELEPHONE tr_TR.UTF-8
# XDG_DATA_DIRS /usr/share/cinnamon:/usr/share/gnome:/home/cevher/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share:/usr/share:/var/lib/snapd/desktop
# GDMSESSION cinnamon
# MANDATORY_PATH /usr/share/gconf/cinnamon.mandatory.path
# CONDA_DEFAULT_ENV python-exercises
# DBUS_SESSION_BUS_ADDRESS unix:path=/run/user/1000/bus
# DEFAULTS_PATH /usr/share/gconf/cinnamon.default.path
# XDG_CURRENT_DESKTOP X-Cinnamon
# CONDA_PREFIX /home/cevher/anaconda3/envs/python-exercises
# INSIDE_NEMO_PYTHON
# SSH_AGENT_PID 2235
# LC_PAPER   tr_TR.UTF-8
# SESSION_MANAGER local/NT00782:@/tmp/.ICE-unix/2166,unix/NT00782:/tmp/.ICE-unix/2166
# LOGNAME    cevher
# PWD        /home/cevher/projects/python-projects/python-exercises/sdtlib
# PYCHARM_HOSTED 1
# LANGUAGE   en_US
# PYTHONPATH /home/cevher/projects/python-projects/python-exercises:/home/cevher/app/pycharm/plugins/python/helpers/pycharm_matplotlib_backend:/home/cevher/app/pycharm/plugins/python/helpers/pycharm_display
# SHELL      /usr/bin/zsh
# LC_ADDRESS tr_TR.UTF-8
# GIO_LAUNCHED_DESKTOP_FILE /home/cevher/Desktop/pycharm.desktop
# OLDPWD     /home/cevher/app/pycharm/bin
# GNOME_DESKTOP_SESSION_ID this-is-deprecated
# GTK_MODULES gail:atk-bridge
# XDG_SESSION_PATH /org/freedesktop/DisplayManager/Session0
# CONDA_PROMPT_MODIFIER (python-exercises)
# XDG_SESSION_DESKTOP cinnamon
# SHLVL      0
# LC_IDENTIFICATION tr_TR.UTF-8
# LC_MONETARY tr_TR.UTF-8
# XDG_CONFIG_DIRS /etc/xdg/xdg-cinnamon:/etc/xdg
# LANG       en_US.UTF-8
# XDG_SEAT_PATH /org/freedesktop/DisplayManager/Seat0
# XDG_SESSION_ID c2
# XDG_SESSION_TYPE x11
# DISPLAY    :0
# LC_NAME    tr_TR.UTF-8
# CONDA_SHLVL 1
# PYCHARM_DISPLAY_PORT 63342
# XDG_SESSION_CLASS user
# GDM_LANG   en_US
# PYTHONIOENCODING UTF-8
# XDG_GREETER_DATA_DIR /var/lib/lightdm-data/cevher
# GPG_AGENT_INFO /run/user/1000/gnupg/S.gpg-agent:0:1
# DESKTOP_SESSION cinnamon
# USER       cevher
# GIO_LAUNCHED_DESKTOP_FILE_PID 5178
# QT_ACCESSIBILITY 1
# LC_NUMERIC tr_TR.UTF-8
# SSH_AUTH_SOCK /run/user/1000/keyring/ssh
# XDG_SEAT   seat0
# PYTHONUNBUFFERED 1
# GTK_OVERLAY_SCROLLING 1
# QT_QPA_PLATFORMTHEME qt5ct
# XDG_VTNR   7
# XDG_RUNTIME_DIR /run/user/1000
# HOME       /home/cevher

#
#
#
# os.path....
# os.path.abspath()
print(os.path.abspath("05_sqlite.py"))
# /home/cevher/projects/python-projects/python-exercises/06_os.py

print(os.path.dirname('/home/cevher/projects/python-projects/python-exercises/README.md'))
# /home/cevher/projects/python-projects/python-exercises

print(os.path.dirname(os.path.abspath("06_os.py")))
# /home/cevher/projects/python-projects/python-exercises

print(os.path.exists("/home/cevher/projects/python-projects/python-exercises"))  # True
print(os.path.exists("/home/cevher/projects/python-projects/python-exercises/README.md"))  # True

print(os.path.expanduser('~'))  # /home/cevher

print(os.path.isdir("/home/cevher"))  # True
print(os.path.isfile("/home/cevher/.bashrc"))  # True

print(os.path.join("dir1", "dir2", "dir3"))  # dir1/dir2/dir3

print(os.path.split("/home/cevher/projects"))
# ('/home/cevher', 'projects')
dir_, f_ = os.path.split("/home/cevher/app/Python-3.8.3.tar.xz")
print(dir_, f_)  # ('/home/cevher/app', 'Python-3.8.3.tar.xz')

f, f_type = os.path.splitext("06_os.py")
print(f,f_type) # ('06_os', '.py')

print(os.__file__) # /home/cevher/anaconda3/envs/python-exercises/lib/python3.8/os.py
print(os.path.__file__)
# GNU/Linux : /home/cevher/anaconda3/envs/python-exercises/lib/python3.8/posixpath.py
# Windows : C:\Python3.8\lib\ntpath.py

os.path
if os.name == 'nt': # for windows
    import ntpath as path

else: # for Linux :)))))
    import posixpath as path

