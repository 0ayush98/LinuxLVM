# LinuxLVM
RHEL_linux_8 is used.

vg name  = ayush

lvm name  = mylvm

command to create the lvm from the existing vg


lvcreate --size {}G --name mylvm ayush

and to see info about lv use

lvdisplay /dev/ayush/lvm
