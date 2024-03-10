from sys import stdin, stdout

n = stdin.readline()
n_list = set(stdin.readline().split())
m = stdin.readline()
m_list = stdin.readline().split()

for i in m_list :
    stdout.write('1\n') if i in n_list else stdout.write('0\n')