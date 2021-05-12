def final_postion(r, v, t, w, h):
    """ Finds the final position of a ball starting at position r moving on a w by h billiards table with no friction and perfect reflection with velocity v after a time period of t """
    return [compute_position_1d(r[0],v[0],t,w),compute_position_1d(r[1],v[1],t,h)]

def compute_position_1d(r, v, t, d):
    """ Computes the position of a ball along one axis starting a r moving on interval of width d with no friction and perfect reflection with velocity v after time t"""
    if v >= 0:
        travled = r + t*v
    if v < 0:
        travled = (d-r) + t*v
    bounces = int(travled//d)
    distance = travled%d
    if ((bounces%2)==0 and v>=0) or ((bounces%2)==1 and v<0):
        return distance
    else:
        return d-distance

if __name__ == "__main__":
    print(final_postion([0.,0.],[1.,14.],.5,1,5))

    

