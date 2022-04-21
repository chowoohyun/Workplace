##code up 입력한 수보다 커지는 경우 그만하기
##code up 6086

# a = int(input())
# c = 0
# s = 0

# while True:
#     c += s
#     s += 1 
#     if c >= a :
#         break

# print(c)


##codeup 6083
##rgb 조합하기


# r, g, b = map(int, input().split())
# count = 0

# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print('%d, %d, %d' % (i, j, k))
#             count += 1

# print(count)


##codeup 에서 받은 정답

# r, g, b = input().split() 
# r = int(r) 
# g = int(g) 
# b = int(b) 

# for i in range(0, r) : 
#     for j in range(0, g) : 
#         for k in range(0, b) : 
#             print(i, j, k) 
# print(r*g*b)

#위 코드와 뭐가 다른지 모르겠다.....



'''
code up 소리파일 저장용량 계산하기 (6084)
소리가 컴퓨터에 저장될 때에는 디지털 데이터화 되어 저장된다.

마이크를 통해 1초에 적게는 수십 번, 많게는 수만 번 소리의 강약을 체크하고,
한 번씩 체크할 때 마다 그 값을 정수값으로 바꾸어 저장하는 방식으로 소리를 파일로 저장할 수 있다.

값을 저장할 때에는 비트를 사용하는 정도에 따라 세세한 녹음 정도를 결정할 수 있고,
좌우(스테레오) 채널로 저장하면 2배… 5.1채널이면 6배의 저장공간이 필요하고,
녹음 시간이 길면 그 만큼 더 많은 저장공간이 필요하다.

1초 동안 마이크로 소리강약을 체크하는 횟수를 h
(헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다.)

한 번 체크한 값을 저장할 때 사용하는 비트수를 b
(2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)

좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c
(모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.)

녹음할 시간(초) s가 주어질 때,

필요한 저장 용량을 계산하는 프로그램을 작성해보자.

실제로, 일반적인 CD 음질(44.1KHz, 16bit, 스테레오)로 1초 동안 저장하려면
44100 * 16 * 2 * 1 bit의 저장공간이 필요한데,
44100*16*2*1/8/1024/1024 로 계산하면 약 0.168 MB 정도가 필요하다.

이렇게 녹음하는 방식을 PCM(Pulse Code Modulation) 방법이라고 하는데,
압축하지 않은 순수한(raw) 소리 데이터 파일은 대표적으로 *.wav 가 있다.

**
      8 bit(비트)           = 1byte(바이트)       # 8bit=1Byte
1024 Byte(210 byte) = 1KB(킬로 바이트)  # 1024Byte=1KB
1024 KB(210 KB)      = 1MB(메가 바이트)
1024 MB(210 MB)     = 1GB(기가 바이트)
1024 GB(210 GB)      = 1TB(테라 바이트)

'''

# h, b, c, s = input().split()
# h = int(h)
# b = int(b)
# c = int(c)
# s = int(s)

# if h <=48000 and b%8 == 0 and c<=5 and s<6000:

#     save = h*b*c*s /1024/1024/8

# print('%0.1f MB' %save)



####code up 6092

# n = int(input())
# a = input().split()

# for i in range(n):
#     a[i] = int(a[i])

# d = [] ##리스트초기화
# for i in range(24):
#     d.append(0)

# for i in range(n):
#     d[a[i]] += 1

# for i in range(1, 24):
#     print(d[i], end=' ')

####code up 6097
##설탕과자 뽑기

