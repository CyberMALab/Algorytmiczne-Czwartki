import sys

def main(stream_in):
    sys.stdin = open(stream_in)
    
    z = int(input())
    for i in range(z):
        line = input().split()
        n, C = int(line[0]), int(line[1])
        
        al = [] # actual
        pl = [] # planned
        
        dl = [] # difference
        
        for j in range(n):
            line = input().split()
            al.append([int(line[0]), j])
            pl.append([int(line[1]), j])
            dl.append([(al[j][0] - pl[j][0]), j])
            
        dl.sort()
        
        # print(f'{z}')
        # print(f'n = {n} | C = {C}')
        # print(f'AL: {al}')
        # print(f'PL: {pl}')
        # print(f'DL: {dl}\n')
        
        t = 0       # time
        ops = []     # operations
        i = 0       
        ind = 1     
        
        while True:
            x = dl[i][0]
            if x == 0:
                # print(f'X   : {x} : {i}')
                break
            else:
                ops.append((dl[i][1]+1, dl[n-ind][1]+1))
                if x + dl[n-ind][0] == 0:
                    # print(f'I   : {x}')
                    dl[n-ind][0] = 0
                    ind += 1
                    dl[i][0] = 0
                    i += 1
                    # print(x)
                    t += C - x
                    
                elif x + dl[n-ind][0] > 0:
                    # print(f'II  : {x}')
                    dl[n-ind][0] += x
                    dl[i][0] = 0
                    i += 1
                    # print(dl[n-ind][0] + x)
                    
                    t += C + (dl[n-ind][0] + x)
                    
                elif x + dl[n-ind][0] < 0:
                    # print(f'III : {x}')
                    dl[i][0] += dl[n-ind][0]
                    dl[n-ind][0] = 0
                    ind += 1
                    # print(dl[n-ind][0])
            
                    t += C + dl[n-ind][0]
                    
        # print()
        # print(dl)
        print()
        print(f'{t} {len(ops)}')
        # for op in ops:
        #     print(f'{op[0]} {op[1]}')
        

if __name__ == '__main__':
    stream_in = './data/sample.in'
    main(stream_in)