def weight_on_planets():
    # write your code here
    weight = int(input("What would you weigh on earth? "))
    mars_weight = weight * 0.38
    jupiter_weight = weight * 2.34
    print ("\nOn Mars you would weight {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(mars_weight, jupiter_weight))
   

if __name__ == '__main__':
   weight_on_planets()
