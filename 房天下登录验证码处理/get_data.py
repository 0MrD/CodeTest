import time
"""方式一得到滑块data数据"""
def linear_interpolation(start, end, duration, interval):
    """
    线性插值函数，根据起始值、目标值、持续时间和插值时间间隔来计算插值列表
    """
    steps = int(duration / interval)
    step_size = (end - start) / steps
    values = [start + i * step_size for i in range(steps)]
    return values


def generate_mouse_data(x, y, t, duration, interval):
    """
    生成鼠标数据，根据初始位置和时间，持续时间和插值时间间隔来生成鼠标移动数据
    """
    data = []
    timestamp = int(time.time() * 1000)
    data.append({"x": 0, "y": y, "t": timestamp, "e": "mousedown"})

    x_values = linear_interpolation(0, x, duration, interval)  # mousedown的x坐标从0递增到x
    t_values = linear_interpolation(t, t + duration, duration, interval)  # 时间从t增加到t + duration

    for x_val, t_val in zip(x_values, t_values):
        timestamp = int(time.time() * 1000)
        data.append({"x": int(x_val), "y": y, "t": int(t_val), "e": "mousemove"})

    timestamp = int(time.time() * 1000) + duration * 1000  # mouseup的时间应该比最后一个mousemove的时间大
    data.append({"x": x, "y": y, "t": timestamp, "e": "mouseup"})

    return data


def main(x, y):
    # 示例用法
    t = int(time.time() * 1000)
    duration = 2  # 持续时间为2秒
    interval = 0.1  # 插值时间间隔为0.1秒
    data = generate_mouse_data(x, y, t, duration, interval)
    return data

