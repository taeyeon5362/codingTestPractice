def solution(hp):
    jang = hp // 5
    byeong = (hp-(jang*5)) // 3
    il = (hp-(jang*5)-(byeong*3))//1
    
    return jang + byeong + il
        