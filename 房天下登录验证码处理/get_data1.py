import random
import time
"""方式二得到滑块data数据"""
def get_silde_track(distance):  #传入缺口距离
    track = []
    start = {
        "x": 0,
        "y": 467,
        "t": int(time.time() * 1000),
        "e": "mousedown"
    }
    track.append(start)

    x, y, t = start['x'], start['y'], start['t']
    while distance >= x:
        x += random.choices([0,1,2],weights=[0.4,0.4,0.2],k=1)[0]
        y -= random.choices([0, 1, 2], weights=[0.4, 0.4, 0.2], k=1)[0]
        t += random.randint(0,20)
        track.append({
            "x": x,
            "y": y,
            "t": t,
            "e": "mousemove"
        })
    end = {
        "x": x,
        "y": y,
        "t": t + 30,
        "e": "mouseup"
    }
    track.append(end)
    return track




