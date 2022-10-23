import os

from numpy import append
class json_filelist_reader:
    folder = os.getcwd()
    #현재 디렉토리 불러오기
    filenamelist=[]
    filenamelist_without_extension=[]
    txtfilenamelist=[]
    #print(os.listdir(folder))
    for filename in os.listdir(folder):  #현재 디랙토리에 있는 파일명 불러오기
        ext=filename.split(".")[-1]
        # os.listdir(folder)으로 불러온 파일명을 split으로"." 으로나눈후
        #[-1]뒤에서 첫번째 . 자리의 이름을  ext 변수에 대입 
        if ext == 'json': # 대입한 ext 값이 json 이면 파일명 불러오기
            filenamelist.append(filename)
            filenamelist_without_extension.append(filename.split(".")[0])
        if ext == 'txt':
            txtfilenamelist.append(filename)

    for i in filenamelist_without_extension:
        if not filenamelist_without_extension in txtfilenamelist:
            f = open("{0}.txt".format(i),"w")
            f.write("enable")
            f.close()
    