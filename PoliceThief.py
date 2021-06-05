import time
import turtle as t
import DrawPoliceThief

def policeThief(array, n, k):

    DrawPoliceThief.rundraw(array)

    count = 0
    i = 0
    l = 0
    r = 0
    res = 0
    thi = []
    pol = []

    while i < n:
        if array[i] == 'P':
            pol.append(i)
        elif array[i] == 'T':
            thi.append(i)
        i += 1
        
    DrawPoliceThief.t.speed(1)
    DrawPoliceThief.t.clearscreen()

    po = DrawPoliceThief.drawPolice2(pol)
    th = DrawPoliceThief.drawThief2(thi)
    
    drawRes = DrawPoliceThief.drawRectangle(0, -300, 200, 300, 'grey')
    DrawPoliceThief.drawNumRes(200, -100,'brown', 'Jail')
    DrawPoliceThief.drawNumRes(100, -100,'orange', ('K:' + str(k)))

    posPo = DrawPoliceThief.getPosition(po)
    posTh = DrawPoliceThief.getPosition(th)

    while l <  len(thi) and r < len(pol):
        
        check = abs(thi[l] - pol[r])
        if (check <= k):
            DrawPoliceThief.drawRunRes2(po, th, l , r, res, drawRes, count)
            po[r].goto(posPo[r][0], posPo[r][1])
            res += 1
            l += 1
            r += 1
            count += 70
        else:
            DrawPoliceThief.drawRunGo2(po, th, l, r)

            po[r].goto(posPo[r][0], posPo[r][1])
            th[l].goto(posTh[l][0], posPo[l][1])
            
            if thi[l] < pol[r]:
                l += 1
            else:
                r += 1

    DrawPoliceThief.drawNumRes(-300, -300,'green', ('Result: ' + str(res)))

    return res

if __name__ == '__main__':
    arr3 = ['P', 'T', 'P', 'P','T']
    # arr3 = ['P', 'P', 'P', 'T', 'T', 'T']

    # arr3 = ['P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P', 'T','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P', 'P', 'T', 'T', 'P','P','P', 'T', 'P', 'T', 'T', 'P','P', 'T', 'P', 'T', 'T', 'P']
    k = 1
    n = len(arr3)
    ts = time.time()
    res = policeThief(arr3, n, k)
    te = time.time()
    print(("Maximum thieves caught: {}".format(res)))
    print(te-ts, n)

    DrawPoliceThief.wn.exitonclick()
