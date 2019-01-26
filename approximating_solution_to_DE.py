delta_t=2
pi=3.1415926
t=[0]

phi_b=[]
phi_b_d=[] #derivative of phi
phi_b_dd=[] #2nd derivative of phi



phi_s=[]
phi_s_d=[]
phi_s_dd=[]

delta_phi=[phi_b[0]-phi_b[0]]

def euler_step(last_var: float, last_var_d : float):
    var = last_var + last_var_d * delta_t
    return var

def calculate_phi_b_dd(current_phi_b, current_phi_b_d ,current_phi_s ,current_phi_s_d ,
                       current_phi_b_dd):
    return new_phi_b_dd

def calculate_phi_s_dd(current_phi_b, current_phi_b_d ,current_phi_s ,current_phi_s_d ,
                       current_phi_b_dd):
    return new_phi_s_dd

def calculate_range(current_phi_s, current_phi_s_d):
    return new_range

def set_initial_conditions:
    phi_b.append(3 * pi / 4)
    phi_b_d.append(0.0)
    phi_s.append(pi / 2)
    phi_s_d .append(0.0)
    phi_b_dd.append(calculate_phi_b_dd(phi_b[0], phi_b_d[0], phi_s[0], phi_s_d[0]))
    phi_s_dd.append(calculate_phi_s_dd(phi_b[0], phi_b_d[0],phi_s[0],phi_s_d[0], phi_b_dd[0]))
    delta_phi.append([phi_b[0] - phi_b[0]])


def stepequation("takes in the last term of each eqn"):
    delta_phi.append(phi_b[i] - phi[i])
    phi_b.append(euler_step(phi_b[i], phi_b_d[i]))
    phi_b_d.append(euler_step(phi_b_d[i],phi_b_dd[i]))
    phi_s.append(euler_step(phi_s[i],phi_s_d[i]))
    phi_s_d.append(euler_step(phi_s_d[i],phi_s_dd[i]))
    phi_b_dd.append(calculate_phi_b_dd(phi_b[i], phi_b_d[i], phi_s[i], phi_s_d[i]))
    phi_s_dd.append(calculate_phi_s_dd(phi_b[i], phi_b_d[i],phi_s[i],phi_s_d[i], phi_b_dd[i]))

