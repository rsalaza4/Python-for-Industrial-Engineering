### ECONOMIC ORDER QUANTITY ###

# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Define EOQ function
def EOQ(S, D, H):
    
    """
    Economic Order Quantity
    
    Arguments:
    S: ordering cost
    D: annual quantity demanded
    H: holding cost per unit
    
    Returns:
    [Q, number_of_orders, time_between_cycles, annual ordering cost, annual holding cost, annual total cost]
    
    """
    
    # Validate that all function arguments are non-negative
    if(S>0 and D>0 and H>0):
        
        Q = (np.sqrt(2*S*D/H))
        number_of_orders = D/Q
        time_between_cycles = 12/number_of_orders
        AOC = D/Q*S
        AHC = Q/2*H
        ATC = AOC+AHC

        return [Q, number_of_orders, time_between_cycles, AOC, AHC, ATC]
    
    else:    
        print("Error. All function arguments must be non-negative.")
    
# Run example    
EOQ(10,2400,0.3)

# Create period list and append values
period = [0, 2]
while period[-1] < 12:
    period.append(period[-1])
    period.append(period[-1]+2)
    
# Create inventory list and append values
inventory = [400, 0]
while len(inventory) < len(period):
    inventory.append(400)
    inventory.append(0)

# Plot inventory level graph
plt.figure(figsize=(15,5))
plt.plot(period,inventory)
plt.xlabel("Month")
plt.ylabel("Inventory Level")
plt.title("Economic Order Quantity")
