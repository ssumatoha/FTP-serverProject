import os
import re
import shutil


class FileManager(object):

    def pwd(self):
        return 'Текущая деректория: ', os.getcwd()

    def ls(self):
        return os.listdir()

    def mkdir(self, name='noName'):
        os.mkdir(name)

    def rmdir(self, name):
        os.rmdir(name)

    def cd(self, name):
        if name != '..':
            os.chdir(name)
            return 'Текущая деректория была изменена на: ', os.getcwd()
        else:
            r = re.split(r'[\\]', os.getcwd())
            r.pop(-1)
            r_new = [x + '\\' for x in r]
            r_new[-1] = r_new[-1][:-1]
            way = ''.join(r_new)
            os.chdir(way)
            return 'Текущая деректория была изменена на: ', os.getcwd()

    def touch(self, name='noneFile'):
        text_file = open(f'{name}.txt', 'w')
        text_file.close()

    def wrt(self, name, text=''):
        text_file = open(f'{name}.txt', 'w')
        text_file.write(text)
        text_file.close()

    def cat(self, name):
        with open(f'{name}') as f:
            return f.read()

    def delFile(self, name):
        os.remove(f'{name}')

    def copyFile(self, original, copy):
        shutil.copyfile(f'{original}', f'{copy}')

    def movingFiles(self, loc, newLoc):
        shutil.move(f'{loc}', f'{newLoc}')

    def renameFile(self, name, rename):
        os.rename(f'{name}', f'{rename}')

    def help(self):
        return 'Команда pwd указывает на текущую деректорию\
        \nКоманда mkdir создаёт деректорию (принимает аргумент: имя создаваемой деректории)\
        \nКоманда rmdir удаляет дерикторию (принимает аргумент: имя удаляемой дерекирии)\
        \nКоманда cd изменяет текущую деректорию (принимает аргумент: деректория, в которую хотите переместиться)\
        \ncd может принемать аргумент .., который меняет текущую деректорию вверх по ветви\
        \nКоманда touch создаёт файл в текущей деректории (принимает аргумент: имя создаваемого файла)\
        \nКоманда wrt записывает текст в файл (принимает аргументы: 1-имя файла 2-текст)\
        \nКоманда cat выводит содержимое файла (принимает аргумент: имя файла)\
        \nКоманда delFile удаляет файл (принимает аргумент: имя файла)\
        \nКоманда copyFail копирует файл (принимает аргумены: 1-имя копироваемого файла 2-имя файла-копии)\
        \nКоманда movingFile перемещает файл (принимает аргументы: локацию перемещаемого файла и новую локацию)\
        \nКоманда renameFile переименовывает файл (принимает аргументы: имя изменяемого файла и новое имя'
