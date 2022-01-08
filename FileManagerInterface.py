from FileManagerClass import FileManager
#  import os.path

print('для получения справки о командах введите help')
prog = FileManager()
work_dir = 'dira'  # start directory
prog.cd(work_dir)

while True:
    command = str(input('введите команду: '))
    if command == 'pwd':
        prog.pwd()
    elif command.split()[0] == 'mkdir':
        if len(command.split()) == 2:
            prog.mkdir(command.split()[1])
        elif len(command.split()) == 1:
            prog.mkdir()
    elif command.split()[0] == 'rmdir':
        prog.rmdir(command.split()[1])
    elif command.split()[0] == 'cd':
        prog.cd(command.split()[1])
    elif command.split()[0] == 'touch':
        prog.touch(command.split()[1])
    elif command.split()[0] == 'wrt':
        prog.wrt(command.split()[1], command.split()[2])
    elif command.split()[0] == 'cat':
        prog.cat(command.split()[1])
    elif command.split()[0] == 'delFile':
        prog.delFile(command.split()[1])
    elif command.split()[0] == 'copyFile':
        prog.copyFile(command.split()[1], command.split()[2])
    elif command.split()[0] == 'movingFile':
        prog.movingFiles(command.split()[1], command.split()[2])
    elif command.split()[0] == 'renameFile':
        prog.renameFile(command.split()[1], command.split()[2])
    elif command.split()[0] == 'ls':
        prog.ls()
    elif command == 'help':
        prog.help()
    elif command == 'exit':
        break
    else:
        print('Вы ввели недопустимое значение.\n \
        Если вам нужна справка, введите команду help')
