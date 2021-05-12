#include <iostream>
#include <array>
#include <cmath>

double compute_postion_1d(double r, double v, double t, double d) {
    double traveled = 0.;
    double distance = 0.;
    int bounces =  0;

    if(v>=0){
        traveled = r + t*v;
    }
    else{
        traveled = (d-r) + t*v;
    }
    distance = std::fmod(traveled,d);
    bounces = (int) traveled/d;
    if (((bounces%2)==0 && v>=0) || ((bounces%2)==1 && v<0)){
        return distance;
    }
    else {
        return d-distance;
    }
}

int main() {
    // Define test inputs
    std::array<double,2> r = {0.,0.}; // initial position
    std::array<double,2> v = {1.,1.}; // velocity
    double t = 7; // duration
    double w = 5; // width of table
    double h = 5; // height of table
    
    std::cout << "[" << compute_postion_1d(r[0],v[0],t,w) << ","<< compute_postion_1d(r[1],v[1],t,h) << "]" << "\n";
}

