a = deg2rad(90);
b = 0;
g = deg2rad(-90);
m1 = [1 0 0; 0 cos(a) -sin(a); 0 sin(a) cos(a)];
m2 = [cos(b) 0 sin(b); 0 1 0; -sin(b) 0 cos(b)];
m3 = [cos(g) -sin(g) 0; sin(g) cos(g) 0; 0 0 1];

M = m3 * m2 * m1

M1 = [cos(a), -sin(a), 0; sin(a), cos(a), 0; 0, 0, 1] * [cos(b), 0, sin(b); 0, 1, 0; -sin(b), 0, cos(b)] * [1, 0, 0; 0, cos(g), -sin(g); 0, sin(g), cos(g)]
M2 = [cos(a)*cos(b), cos(a)*sin(b)*sin(g)-sin(a)*cos(g), cos(a)*sin(b)*cos(g)+sin(a)*sin(g);
      sin(a)*cos(b), cos(a)*sin(b)*sin(g)+cos(a)*cos(g), sin(a)*sin(b)*cos(g)-cos(a)*sin(g);
      -sin(b), cos(b)*sin(g), cos(b)*cos(g)];
