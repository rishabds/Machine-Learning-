import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
   # number of observations/points
   n = np.size(x)
   # mean of x and y vector
   m_x, m_y = np.mean(x), np.mean(y)
   # calculating cross deviation and deviation about x
   SS_xy = np.sum(y*x) - n*m_y*m_x
   SS_xx = np.sum(x*x) - n*m_x*m_x
   # calculating regression coefficients
   b_1 = SS_xy / SS_xx
   b_0 = m_y - b_1*m_x

   return(b_0,b_1)

def scatter_plot(x,y,b):
    plt.scatter(x, y, color="blue",marker="*", s=30)

    y_pred = b[0] + b[1]*x

    plt.plot(x, y_pred, color="cyan")

    plt.xlabel("Age")
    plt.ylabel("Population Using Mobile Phone")

    plt.show()

def main():
    x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    y = np.array([40, 80, 90, 82, 65, 50, 35, 30, 15, 5])

    b = estimate_coef(x, y)
    print("Estimated coefficients:\ngradient= {}\ny-intercept = {}".format(b[0], b[1]))

    # plotting regression line
    scatter_plot(x, y, b)


if __name__ == "__main__":
    main()