import os
import glob
import shutil



def make_dir_for_arrange_():

    # c:\python\work-for-python/scans 생성
    # c:\python\work-for-python/scans/01 ~ 20 생성
    try:
        for i in range(20):
            if i < 9:
                os.mkdir('c:\\python\work-for-python\scans\\0' + str(i + 1) )
            else:
                os.mkdir('c:\\python\work-for-python\scans\\' + str(i + 1))
    except:
        print('디렉토리가 있으므로 만들지 않습니다.')


def check_for_work_and_get_files():
    os.chdir('c:\\python\work-for-python')
    return glob.glob('*.pdf')


def copy_and_delete_scanfiles(files):
    if len(files) > 0:
        for file in files:

            index_Number = int(file.split('-')[1])

            if index_Number <= 10:
                shutil.copy(file, 'c:\\python\work-for-python\scans\\01')
            elif index_Number <= 20:
                shutil.copy(file, 'c:\\python\work-for-python\scans\\02')
            elif index_Number <= 30:
                shutil.copy(file, 'c:\\python\work-for-python\scans\\03')
            elif index_Number <= 40:
                shutil.copy(file, 'c:\\python\work-for-python\scans\\04')
            elif index_Number <= 50:
                shutil.copy(file, 'c:\\python\work-for-python\scans\\05')
            elif index_Number <= 60:
                shutil.copy(file, 'c:\\python\work-for-python\scans\\06')
            elif index_Number <= 70:
                shutil.copy(file, 'c:\\python\work-for-python\scans\\07')
    else:
        pass


# 00010 ~ 00011 파일은 02 디렉토리로 이동(복사후 삭제)
# 위 작업을 20번 반복