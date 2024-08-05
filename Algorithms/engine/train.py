

def right_point(label_tuple, predict_tuple, tolerte):
    n = np.array([0, 0, 0, 0, 0])
    for i, (x, x_p) in enumerate(zip(label_tuple, predict_tuple)):
        if point_equal(x, x_p, tolerte):
            n[i] = 1
