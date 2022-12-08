file1 = 'wrew.txt'
file2 = 'wrew.exe'
file3 = 'wrew.pdf'
file4 = 'wrew.txt.rip'

print(file1[:file1.find(".")])
print(file2[file2.find("."):])
print(file3[file3.find(".") + 1:])
print(file4[file4.find(".") + 1:])
print(file4[file4.rfind(".") + 1:])