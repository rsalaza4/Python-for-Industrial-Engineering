### ECONOMIC PRODUCTION QUANTITY ###

# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Define EPQ function
def EPQ(D, P, K, H):
    
    """
    Economic Production Quantity
    
    Arguments:
    D: annual quantity demanded
    K: cost of production run
    H: holding cost per unit
    P: production rate
    
    Returns:
    [Q, cycle length, number_of_production_runs, production run length, demand period length, annual production cost, annual holding cost, maximum inventory level, annual total cost]
    
    """
    
    if(D>0 and P>0 and K>0 and H>0):
    
        Q = (np.sqrt((2*D*K)/(H*(1-(D/P)))))
        T = round(Q/D*12,2)
        number_of_production_runs = D/Q
        Tp = round(Q/P*12,2)
        Td = round((Q/D-Q/P)*12,2)
        APC = number_of_production_runs*K
        AHC = Q/2*(1-(D/P))*H
        Imax = Q*(1-(D/P))
        ATC = APC+AHC

        return[Q , T, number_of_production_runs, Tp, Td, APC, AHC, Imax, ATC]
    
    else:
        print("Error. All function arguments must be non-negative.")
        
  # Run example
  EPQ(200,1000,100,5)
  
  # Create period list and append values
period = [0]
while period[-1] < 12:
    period.append(period[-1] + 1.2)
    period.append(period[-1] + 4.8)
    
# Create inventory list and append values
inventory = [0]
while len(inventory) < len(period):
    inventory.append(80)
    inventory.append(0)
    
# Plot inventory level graph
plt.figure(figsize=(15,5))
plt.plot(period,inventory)
plt.plot([0,1.2],[0,100], linestyle="dashed", label="Production Rate")
plt.xlabel("Month")
plt.ylabel("Inventory Level")
plt.title("Economic Production Quantity")
plt.legend()
