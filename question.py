def final_postion(r, v, t, w, h):
    """ Finds the final position of a ball starting at postion r moving on a w by h billards table with no friction and perfect reflection with velocity v after a time period of t """
    s = [0.,0.]
    # x portion
    if v[0] >= 0:
        x_travled = r[0] + t*v[0]
        x_bounces = int(x_travled//w)
        x_distance = x_travled%w
        print(x_travled,x_distance,x_bounces)
        if (x_bounces%2)==0:
            s[0] = x_distance
        else:
            s[0] = w-x_distance
    if v[0] < 0:
        x_travled = (w-r[0]) + t*v[0]
        x_bounces = int(x_travled//w)
        x_distance = x_travled%w
        if (x_bounces%2)==1:
            s[0] = x_distance
        else:
            s[0] = w-x_distance     
    # y portion
    if v[1] >= 0:
        y_travled = r[1] + t*v[1]
        y_bounces = int(y_travled//h)
        y_distance = y_travled%h
        if (y_bounces%2)==0:
            s[1] = y_distance
        else:
            s[1] = h-y_distance
    if v[1] < 0:
        y_travled = (h-r[1]) + t*v[1]
        y_bounces = int(y_travled//h)
        y_distance = y_travled%h
        if (y_bounces%2)==1:
            s[1] = y_distance
        else:
            s[1] = h-y_distance
    return s

if __name__ == "__main__":
    print(final_postion([0.,0.],[1.,2.],6.,5,5))


