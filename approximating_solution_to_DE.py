import matplotlib.pyplot as plt

delta_t=2
pi=3.1415926
t=[0]

phi_b=[]
phi_b_d=[] #derivative of phi
phi_b_dd=[] #2nd derivative of phi



phi_s=[]
phi_s_d=[]
phi_s_dd=[]

delta_phi=[phi_b[0]-phi_s[0]]

range=[]

a_s = 5 #function in terms of l1 and l2
a_b = 5 #function in terms of l1 and l2
w_s_squared = 5 #function in terms of l1 and l2
w_b_squared = 5 #function in terms of l1 and l2

def euler_step(last_var: float, last_var_d : float):
    var = last_var + last_var_d * delta_t
    return var


def calculate_phi_b_dd(current_phi_b, current_phi_b_d, current_phi_s, current_phi_s_d,
                        current_delta_phi):
    new_phi_b_dd = (1 / (1 - a_s * (cos(current_delta_phi)) ** 2)) * (a_b * (current_phi_s_d ^ 2 *
                                                                         sin(current_delta_phi)
                                                                             + (a_s *
                                                                                current_phi_b_d ** 2 *
                                                                                sin(
                                                                                    -current_delta_phi) - w_s_squared * sin(
                        current_phi_s)) * cos(current_delta_phi) - w_b_squared * sin(current_phi_b)))
    return new_phi_b_dd


def calculate_phi_s_dd(current_phi_b_d, current_phi_s,
                       current_phi_b_dd, current_delta_phi):
    new_phi_s_dd = a_s * (current_phi_b_d ** 2 * sin(-current_delta_phi) + current_phi_b_dd * cos(
        -current_delta_phi)) - w_s_squared * sin(current_phi_s)
    return new_phi_s_dd

def calculate_range(current_phi_s, current_phi_s_d):
    #TODO write real function
    new_range= current_phi_s+current_phi_s_d

    return new_range


def stepequation():
    delta_phi.append(phi_b[i] - phi[i])
    phi_b.append(euler_step(phi_b[i], phi_b_d[i]))
    phi_b_d.append(euler_step(phi_b_d[i],phi_b_dd[i]))
    phi_s.append(euler_step(phi_s[i],phi_s_d[i]))
    phi_s_d.append(euler_step(phi_s_d[i],phi_s_dd[i]))
    phi_b_dd.append(calculate_phi_b_dd(phi_b[i], phi_b_d[i], phi_s[i], phi_s_d[i],delta_phi[i]))
    phi_s_dd.append(calculate_phi_s_dd(phi_b_d[i],phi_s[i], phi_b_dd[i], delta_phi[i]))
    range.append(calculate_range(phi_s[i], phi_s_d[i]))

def set_constants(l1,l2):
    global a_s, a_b, w_s_squared, w_b_squared
    l1 = 0.2
    l2 = 0.8
    ls = 1
    #l1 + l2 == 1
    m1 = 0.12  # kg
    m2 = 0.005  # kg
    mb = 0.1 * (m1 ** 0.5) * (l1 + l2)
    lb = 0.5 - l1
    dmax = (2 + 2 ** 0.5) / m2 * (m1 * l1 - mb * lb)
    g = 9.8
    Ib = (1 / 12) * mb  # check on this definition for moment of inertia

    phi_b.append(3 * pi / 4)
    phi_b_d.append(0.0)
    phi_s.append(pi / 2)
    phi_s_d .append(0.0)
    phi_b_dd.append(calculate_phi_b_dd(phi_b[0], phi_b_d[0], phi_s[0], phi_s_d[0]))
    phi_s_dd.append(calculate_phi_s_dd(phi_b[0], phi_b_d[0],phi_s[0],phi_s_d[0], phi_b_dd[0]))
    delta_phi.append([phi_b[0] - phi_b[0]])
    range.append(0)
    a_s = l2/ls  # function in terms of l1 and l2
    a_b = m2*l2*ls / (m1*l1**2 + m2*l2**2 + mb*lb**2 + Ib)  # function in terms of l1 and l2
    w_s_squared = g/ls  # function in terms of l1 and l2
    w_b_squared = g*(m1*l1 - m2*l2 - mb*lb)/(m1*(l1**2) + m2*(l2**2) + mb*(lb**2) +Ib)  # function
    # in terms of l1 and l2



def optimize_this(l1, l2):
    stepequation()
    while range[-1]<range[-2]:
        stepequation()
    plt.plot(t,range)
    return range[-1]