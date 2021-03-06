import sys
import os
import argparse

def gen_list(net,label_path):

    hasPts = True
    if net == 12:
        hasPts = False

    stdsize = str(net)

    save_dir = label_path
    
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    f1 = open(os.path.join(save_dir, 'pos_'+ stdsize +'.txt'), 'r')
    f2 = open(os.path.join(save_dir, 'neg_'+ stdsize +'.txt'), 'r')
    f3 = open(os.path.join(save_dir, 'part_'+ stdsize +'.txt'), 'r')

    pos = f1.readlines()
    neg = f2.readlines()
    part = f3.readlines()
    f = open(os.path.join(save_dir, 'label-train.txt'), 'w')
    
    for i in range(int(len(pos))):
        p = pos[i].find(" ") + 1
        pos[i] = pos[i][:p-1] + ".jpg " + pos[i][p:-1] + "\n"
        f.write(pos[i])

    for i in range(int(len(neg))):
        p = neg[i].find(" ") + 1
        neg[i] = neg[i][:p-1] + ".jpg " + neg[i][p:-1] + " -1 -1 -1 -1" + (" -1 -1 -1 -1 -1 -1 -1 -1 -1 -1" if hasPts else "")+"\n"
        f.write(neg[i])

    for i in range(int(len(part))):
        p = part[i].find(" ") + 1
        part[i] = part[i][:p-1] + ".jpg " + part[i][p:-1] + "\n"
        f.write(part[i])

    f1.close()
    f2.close()
    f3.close()

def parse_args():
    parser = argparse.ArgumentParser(description='Gen positive negative part pictures.')
    parser.add_argument('--net', dest='net', help='P R O net',type=int)
    parser.add_argument('--label_path', dest='label_path', help='label path', type=str)

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    gen_list(args.net, args.label_path)