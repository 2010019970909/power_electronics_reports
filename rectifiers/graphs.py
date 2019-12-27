# -*- coding: utf-8 -*-
from graph_generator import *

## Change these functions according to your calculus
# Triphased half bridge rectifier
def V_d(alpha = 0, I_d = 0):
    return (3*np.sqrt(2))/(2*np.pi) * 81 * np.sqrt(3) * cos(alpha) - 0.338 * I_d - 0.8

# Graetz full bridge rectifier
def V_d_2(alpha = 0, I_d = 0):
    m = 3/np.pi * 0.1747 + 2 * 0.04 + 0.219  # 0.4258 + 0.04 # -0.08
    print("m:", m)
    return ((3*np.sqrt(2))/(np.pi) * 46.2 * np.sqrt(3) * cos(alpha) - m * I_d - 1.6)

# Prediction of the estimation delay
def mu_cal(alpha = 0, I_d = 0, cst=((2*0.2666)/(np.sqrt(2)*81*np.sqrt(3)))):
    return rad2deg(np.arccos(cos(alpha) - cst*I_d) - deg2rad(alpha))

# Some maths
def cos(deg):
    return np.cos(deg/180*np.pi)

def deg2rad(deg):
    return deg/180*np.pi

def rad2deg(rad):
    return rad/np.pi*180

"""
    Fill the data.xlsx file without changing the place of the columns.
    You do not have to fill the values of \mu in the column the values
    used are computed from the time values in microsecond.
"""

def main():
    SHOW = False
    graph_1()
    graph_2()
    graph_3()
    graph_4()
    graph_5()
    graph_6()
    graph_7()
    graph_8()
    graph_9()
    graph_10()
    graph_11()
    graph_12()
    graph_13()
    graph_14()
    graph_15()
    circle()

    print("Done\nPress enter to exit.")
    if SHOW:
        plt.show(block=False)
        input()
    plt.close('all')    

"""
    GRAPHS for the report
"""

# Caractéristique externe Vd=f(Id) avec α=0°
def graph_1(filename='exp1_graph1', show=False):
    data = xl.parse(sheet[0])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    I = np.array(data[col[0]][:])
    U = np.array(data[col[1]][:])

    ax.plot(I, U, 'k-', marker='1', linewidth=0.5, label='$V_d$ en fonction de $I_d$')

    # Add title and labels
    ax.set_title(r'Tension en sortie du redresseur en fonction du courant passant dans la charge')
    ax.set_xlabel(r'Courant $I_d$ [A]')
    ax.set_ylabel(r"Tension $V_d$ [V]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    # Axis
    # plt.xscale('log')
    # plt.yscale('log')
    # plt.ylim(bottom=0, top=12)
    # plt.xlim(left=0, right=26)

    #fig.set_size_inches(16/2, 9/2, forward=True)

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Loi d’empiètement en fonction du courant de charge μ=f(Id) avec α=0°
def graph_2(filename='exp1_graph2', show=False):
    data = xl.parse(sheet[0])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    I = np.array(data[col[0]][1:])
    mu = np.array(data[col[2]][1:]) * 360 * 50 / 1e6

    ax.plot(I, mu, 'k-', marker='1', linewidth=0.5, label='$\mu$ en fonction de $I_d$')

    # Add title and labels
    ax.set_title(r"Angle d'empiètement en fonction du courant passant dans la charge")
    ax.set_xlabel(r'Courant $I_d$ [A]')
    ax.set_ylabel(r"Angle $\mu$ [°]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Caractéristique externe Vd=f(Id) avec α=30°
def graph_3(filename='exp1_graph3', show=False):
    data = xl.parse(sheet[1])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    I = np.array(data[col[0]][:])
    U = np.array(data[col[1]][:])

    ax.plot(I, U, 'k-', marker='1', linewidth=0.5, label='$V_d$ en fonction de $I_d$')

    # Add title and labels
    ax.set_title(r"Tension en sortie du redresseur en fonction du courant passant dans la charge")
    ax.set_xlabel(r'Courant $I_d$ [A]')
    ax.set_ylabel(r"Tension $V_d$ [V]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Loi d’empiètement en fonction du courant de charge μ=f(Id) avec α=30°
def graph_4(filename='exp1_graph4', show=False):
    data = xl.parse(sheet[1])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    I = np.array(data[col[0]][1:])
    mu = np.array(data[col[2]][1:]) * 360 * 50 / 1e6

    ax.plot(I, mu, 'k-', marker='1', linewidth=0.5, label='$\mu$ en fonction de $I_d$')

    # Add title and labels
    ax.set_title(r"Angle d'empiètement en fonction du courant passant dans la charge")
    ax.set_xlabel(r'Courant $I_d$ [A]')
    ax.set_ylabel(r"Angle $\mu$ [°]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Relevé de la puissance active en fonction de cos(α), avec Id=10 A
def graph_5(filename='exp1_graph5', show=False):
    data = xl.parse(sheet[2])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    alpha = np.array(data[col[0]][:])
    P = np.array(data[col[1]][:])

    ax.plot(np.cos(alpha/180*np.pi), P, 'k-', marker='1', linewidth=0.5, label=r'$P$ en fonction de $\cos{\left( \alpha \right)}$')

    # Add title and labels
    ax.set_title(r"Puissance active en fonction du cosinus de l'angle de déclenchement")
    ax.set_xlabel(r'$\cos{\left(\alpha\right)}$')
    ax.set_ylabel(r"Puissance $P$ [W]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Comparaison de la caractéristique externe Vd=f(Id) avec α=0°
def graph_6(filename='exp1_graph6', show=False):
    data = xl.parse(sheet[0])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    I = np.array(data[col[0]][:])
    U = np.array(data[col[1]][:])
    U_calc = V_d(I_d=I, alpha=0)

    ax.plot(I, U, 'k-', marker='1', linewidth=0.5, label='Mesuré')
    ax.plot(I, U_calc, 'b-', marker='', linewidth=0.5, label='Calculé')

    # Add title and labels
    ax.set_title(r'Tension en sortie du redresseur en fonction du courant passant dans la charge')
    ax.set_xlabel(r'Courant $I_d$ [A]')
    ax.set_ylabel(r"Tension $V_d$ [V]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Comparaison de la caractéristique externe Vd=f(Id) avec α=30°
def graph_7(filename='exp1_graph7', show=False):
    data = xl.parse(sheet[1])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    I = np.array(data[col[0]][:])
    U = np.array(data[col[1]][:])
    U_calc = V_d(I_d=I, alpha=30)

    ax.plot(I, U, 'k-', marker='1', linewidth=0.5, label='Mesuré')
    ax.plot(I, U_calc, 'b-', marker='', linewidth=0.5, label='Calculé')

    # Add title and labels
    ax.set_title(r'Tension en sortie du redresseur en fonction du courant passant dans la charge')
    ax.set_xlabel(r'Courant $I_d$ [A]')
    ax.set_ylabel(r"Tension $V_d$ [V]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Comparaison de la loi d’empiètement, fonction du courant de charge μ=f(Id) avec α=0°
def graph_8(filename='exp1_graph8', show=False):
    data = xl.parse(sheet[0])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    I = np.array(data[col[0]][1:])
    mu = np.array(data[col[2]][1:]) * 360 * 50 / 1e6
    mu_calc = mu_cal(I_d=I)

    ax.plot(I, mu, 'k-', marker='1', linewidth=0.5, label='Mesuré')
    ax.plot(I, mu_calc, 'b-', marker='1', linewidth=0.5, label='Calculé')

    # Add title and labels
    ax.set_title(r"Angle d'empiètement en fonction du courant passant dans la charge")
    ax.set_xlabel(r'Courant $I_d$ [A]')
    ax.set_ylabel(r"Angle $\mu$ [°]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Comparaison de la loi d’empiètement, fonction du courant de charge μ=f(Id) avec α=30°
def graph_9(filename='exp1_graph9', show=False):
    data = xl.parse(sheet[1])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    I = np.array(data[col[0]][1:])
    mu = np.array(data[col[2]][1:]) * 360 * 50 / 1e6
    mu_calc = mu_cal(alpha=30, I_d=I)

    ax.plot(I, mu, 'k-', marker='1', linewidth=0.5, label='Mesuré')
    ax.plot(I, mu_calc, 'b-', marker='1', linewidth=0.5, label='Calculé')

    # Add title and labels
    ax.set_title(r"Angle d'empiètement en fonction du courant passant dans la charge")
    ax.set_xlabel(r'Courant $I_d$ [A]')
    ax.set_ylabel(r"Angle $\mu$ [°]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

## Graetz
# Comparaison de la caractéristique externe Vd=f(Id) avec α=0°
def graph_10(filename='exp1_graph10', show=False):
    data = xl.parse(sheet[3])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    I = np.array(data[col[0]][:])
    U = np.array(data[col[1]][:])
    U_calc = V_d_2(I_d=I, alpha=0)

    ax.plot(I, U, 'k-', marker='1', linewidth=0.5, label='Mesuré')
    ax.plot(I, U_calc, 'b-', marker='', linewidth=0.5, label='Calculé')

    # Add title and labels
    ax.set_title(r"Tension en sortie du redresseur en fonction du courant passant dans la charge")
    ax.set_xlabel(r'Courant $I_d$ [A]')
    ax.set_ylabel(r"Tension $V_d$ [V]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Comparaison de la loi d’empiètement, fonction du courant de charge μ=f(Id) avec α=0°
def graph_11(filename='exp1_graph11', show=False):
    data = xl.parse(sheet[3])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    I = np.array(data[col[0]][1:])
    mu = np.array(data[col[3]][1:])
    mu_calc = mu_cal(alpha=0, I_d=I, cst=((2*0.1747)/(np.sqrt(2)*46.2*np.sqrt(3))))

    ax.plot(I, mu, 'k-', marker='1', linewidth=0.5, label='Mesuré')
    ax.plot(I, mu_calc, 'b-', marker='1', linewidth=0.5, label='Calculé')

    # Add title and labels
    ax.set_title(r"Angle d'empiètement en fonction du courant passant dans la charge")
    ax.set_xlabel(r'Courant $I_d$ [A]')
    ax.set_ylabel(r"Angle $\mu$ [°]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Comparaison de la caractéristique externe Vd=f(Id) avec α=30°
def graph_12(filename='exp1_graph12', show=False):
    data = xl.parse(sheet[4])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    I = np.array(data[col[0]][:])
    U = np.array(data[col[1]][:])
    U_calc = V_d_2(I_d=I, alpha=30)

    ax.plot(I, U, 'k-', marker='1', linewidth=0.5, label='Mesuré')
    ax.plot(I, U_calc, 'b-', marker='', linewidth=0.5, label='Calculé')

    # Add title and labels
    ax.set_title(r"Tension en sortie du redresseur en fonction du courant passant dans la charge")
    ax.set_xlabel(r'Courant $I_d$ [A]')
    ax.set_ylabel(r"Tension $V_d$ [V]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Comparaison de la loi d’empiètement, fonction du courant de charge μ=f(Id) avec α=30°
def graph_13(filename='exp1_graph13', show=False):
    data = xl.parse(sheet[4])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    I = np.array(data[col[0]][1:])
    mu = np.array(data[col[3]][1:])
    mu_calc = mu_cal(alpha=30, I_d=I, cst=((2*0.1747)/(np.sqrt(2)*46.2*np.sqrt(3))))

    ax.plot(I, mu, 'k-', marker='1', linewidth=0.5, label='Mesuré')
    ax.plot(I, mu_calc, 'b-', marker='1', linewidth=0.5, label='Calculé')

    # Add title and labels
    ax.set_title(r"Angle d'empiètement en fonction du courant passant dans la charge")
    ax.set_xlabel(r'Courant $I_d$ [A]')
    ax.set_ylabel(r"Angle $\mu$ [°]")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Diagramme P−Q du pont de Graetz
def graph_14(filename='exp1_graph14', show=False):
    data = xl.parse(sheet[5])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    # Graetz bridge
    P = np.array(data[col[1]][1:])
    Q = np.array(data[col[2]][1:])

    ax.plot(P, Q, 'k-', marker='1', linewidth=0.5, label='Puissance réactive en fonction\nde la puissance active (pont de Graetz)')

    # Add title and labels
    ax.set_title(r'Point de fonctionnement dans le plan $P-Q$')
    ax.set_xlabel(r'Puissance active en W')
    ax.set_ylabel(r"Puissance réactive en VA")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Diagramme P−Q du pont de mixte
def graph_15(filename='exp1_graph15', show=False):
    data = xl.parse(sheet[5])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    # Mixte bridge
    P = np.array(data[col[5]][1:])
    Q = np.array(data[col[6]][1:])

    ax.plot(P, Q, 'b-', marker='1', linewidth=0.5, label='Puissance réactive en fonction\nde la puissance active (pont mixte)')

    # Add title and labels
    ax.set_title(r'Point de fonctionnement dans le plan $P-Q$')
    ax.set_xlabel(r'Puissance active en W')
    ax.set_ylabel(r"Puissance réactive en VA")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

# Diagramme P−Q du pont de mixte et du pont de Graetz
def circle(filename='cercle_PQ_complet', show=False):
    data = xl.parse(sheet[5])
    col = data.columns
    # print(col)  # read a specific sheet to DataFrame

    _, ax = plt.subplots()

    # Graetz bridge
    P_0 = np.array(data[col[1]][1:])
    Q_0 = np.array(data[col[2]][1:])
    # Mixte bridge
    P_1 = np.array(data[col[5]][1:])
    Q_1 = np.array(data[col[6]][1:])

    ax.plot(P_0, Q_0, 'k-', marker='1', linewidth=0.5, label='Puissance réactive en fonction\nde la puissance active (pont de Graetz)')
    ax.plot(P_1, Q_1, 'b-', marker='1', linewidth=0.5, label='Puissance réactive en fonction\nde la puissance active (pont mixte)')

    # Add title and labels
    ax.set_title(r'Point de fonctionnement dans le plan $P-Q$')
    ax.set_xlabel(r'Puissance active en W')
    ax.set_ylabel(r"Puissance réactive en VA")
    plt.legend()

    # Grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5, which='both')

    plt.savefig(gen_path(filename), bbox_inches='tight', figsize=(12/2.54, 7.416/2.54), format="PDF", quality=95, dpi=1200)
    if show:
        plt.show(block=False)

if __name__ == "__main__":
    main()