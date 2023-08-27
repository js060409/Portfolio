import os
import shutil

defualt_extention_path = 'C:/Users/ADMIN/AppData/Local/Google/Chrome/User Data/Default/Extensions'

shutil.rmtree(defualt_extention_path)
os.mkdir('C:/Users/ADMIN/AppData/Local/Google/Chrome/User Data/Default/Extensions')

for i in range(60):
    guest_extention_path = 'C:/Users/ADMIN/AppData/Local/Google/Chrome/User Data/Profile '+str(i)

    if not os.path.isdir(guest_extention_path):
        continue

    else:
        os.path.isdir(guest_extention_path)
        shutil.rmtree(guest_extention_path)

print('END')

# PATCH 2023_08_01
#확장 프로그램 경로 오류 수정 완료

#PATCH 2023_08_03
#확장 프로그램 및 프로필 완전 초기화 성공
#.exe 형태로 만들어서 배포 예정