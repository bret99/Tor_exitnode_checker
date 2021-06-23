import os 

os.system('wget https://check.torproject.org/torbulkexitlist?ip=1.1.1.1 -q -O tor_exit_nodes.txt')
IP_to_check = input("Enter the exit node to check: ")

with open('{}/tor_exit_nodes.txt'.format(os.getcwd())) as ten:
    for line in ten.readlines():
        if IP_to_check == '':
            pass
        elif IP_to_check in line:
            print('{}\033[1;91mfound!!!\033[1;00m'.format(line))

