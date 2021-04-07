import os
print("""
       select your option
       1: To extend the LVM volume
       2: To decrese the LVM volume


        """)
x=int(input("select option: "))

if x==1:
    y = int(input("size: "))
    os.system("""lvextend --size +{}G /dev/ayush/mylvm
                 resize2fs /dev/ayush/mylvm
                 size is increase succesfully""".format(y))

elif x==2:
    y = int(input("size: "))
    os.system("""umount /dev/ayush/mylvm
                 e2fsck -f /dev/ayush/mylvm
                 resize2fs /dev/ayush/mylvm {}G 
                 lvreduce --size {}G /dev/ayush/mylvm
                 mount /dev/ayush/mylvm /root/drive
                 size is decrease succesfully""".format(y,y))


                                     
