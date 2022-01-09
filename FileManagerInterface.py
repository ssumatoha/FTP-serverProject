
def start(prog):
    print('для получения справки о командах введите help')
    work_dir = 'dira'  # server start directory
    prog.cd(work_dir)


def process(prog, command):
    if command == 'pwd':
        return prog.pwd()
    elif command.split()[0] == 'mkdir':
        if len(command.split()) == 2:
            prog.mkdir(command.split()[1])
        elif len(command.split()) == 1:
            prog.mkdir()
    elif command.split()[0] == 'rmdir':
        prog.rmdir(command.split()[1])
    elif command.split()[0] == 'cd':
        return prog.cd(command.split()[1])
    elif command.split()[0] == 'touch':
        prog.touch(command.split()[1])
    elif command.split()[0] == 'wrt':
        prog.wrt(command.split()[1], command.split()[2])
    elif command.split()[0] == 'cat':
        return prog.cat(command.split()[1])
    elif command.split()[0] == 'delFile':
        prog.delFile(command.split()[1])
    elif command.split()[0] == 'copyFile':
        prog.copyFile(command.split()[1], command.split()[2])
    elif command.split()[0] == 'movingFile':
        prog.movingFiles(command.split()[1], command.split()[2])
    elif command.split()[0] == 'renameFile':
        prog.renameFile(command.split()[1], command.split()[2])
    elif command.split()[0] == 'ls':
        return prog.ls()
    elif command == 'help':
        return prog.help()
    else:
        print('Вы ввели недопустимое значение.\n \
        Если вам нужна справка, введите команду help')
