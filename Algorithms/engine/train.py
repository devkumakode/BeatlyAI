            Ppos = i
        if val == 2 and y[i-1] == 0:
            Qpos = i
        if val == 2 and y[i+1] == 3:
            Rpos = i
        if val == 3 and y[i+1] == 0:
            Spos = i
        if val == 4 and y[i-1] == 0:
            Tpos = i

    return Ppos, Qpos, Rpos, Spos, Tpos


def point_equal(label, predict, tolerte):
    if label + tolerte * 250 >= predict >= label - tolerte * 250:
        return True
    else:
        return False
