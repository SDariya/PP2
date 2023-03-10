#1
import os
path = "C:\\Users\\asus\\Desktop\\pp2\\week6"
print("Only directories:")
print([name for name in os.listdir(path)
      if os.path.isdir(os.path.join(path, name))])
print("\nOnly files:")
print([name for name in os.listdir(path)
      if not os.path.isdir(os.path.join(path, name))])
print("\nAll directories and files :")
print([name for name in os.listdir(path)])

#2
import os
print('Exist:', os.access(
    'C:\\Users\\asus\\Desktop\\pp2\\week6\\file.txt', os.F_OK))
print('Readable:', os.access(
    'C:\\Users\\asus\\Desktop\\pp2\\week6\\file.txt', os.R_OK))
print('Writable:', os.access(
    'C:\\Users\\asus\\Desktop\\pp2\\week6\\file.txt', os.W_OK))
print('Executable:', os.access(
    'C:\\Users\\asus\\Desktop\\pp2\\week6\\file.txt', os.X_OK))

#3
import os
print("Test a path exists or not:")
path = r'C:\\Users\\asus\\Desktop\\pp2\\week6\\file.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))

#4
def file_length(fname):
    with open(fname, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1
print("Number of lines in the file: ", file_length('C:\\Users\\asus\\Desktop\\pp2\\week6\\lines.txt'))


