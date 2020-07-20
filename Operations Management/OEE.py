### OVERALL EQUIPMENT EFFECTIVENESS ###

# Import required libraries
import matplotlib.pyplot as plt
%matplotlib inline

# Define ggplot style sheet
plt.style.use('ggplot')

# Define OEE function
def oee(A, B, C, D, E, F):
    
    '''
    Overall Equipment Effectiveness components:
    
    A : Total available time
    B : Run time
    C : Production capacity
    D : Actual production
    E : Product output
    F : Actual good products
    
    '''
    
    # Components validation
    if B <= A and D <= C and E == D and F <= E: 
    
        # Define a list for profit percentages
        
        # % Total available time
        Profits=[100]
        # % Run time
        Profits.append(B/A*100)
        # % Production capacity
        Profits.append(B/A*100)
        # % Actual production
        Profits.append(D/C*Profits[2])
        # % Product output
        Profits.append(D/C*Profits[2])
        # % Actual good products
        Profits.append(F/E*Profits[4])

        # Define a list for losses percentages
        Loss=[0]
        # % Time losses
        Loss.append(Profits[0]-Profits[1])
        Loss.append(Profits[1]-Profits[2])
        # % Speed losses
        Loss.append(Profits[2]-Profits[3])
        Loss.append(Profits[3]-Profits[4])
        # % Defective units
        Loss.append(Profits[4]-Profits[5])

        # Define list of indexes
        ind=[0, 1, 2, 3, 4, 5]
        
        # Define bars width
        width=0.85
        
        # Define figure size
        plt.figure(figsize=(20, 10))
        
        # Plot profits bars
        plt.barh(ind, Profits, width, color='#03C03C')
        
        # Plot losses bars
        plt.barh(ind, Loss, width, left=Profits, color='red')
        
        # Plot OEE universal benchmarks
        plt.axvline(85, linestyle='dashed', color='black', label='World Class OEE')
        plt.axvline(60, linestyle='dashdot', color='black', label='Typical OEE')
        plt.axvline(40, linestyle='dotted', color='black', label='Low OEE')
        
        # Invert y-axis
        plt.gca().invert_yaxis()
        
        # Hide y-axis labels
        plt.yticks([])

        # Add OEE components
        plt.text(0, 0, 'Total Available Time', horizontalalignment='left')
        plt.text(0, 1, 'Run Time', horizontalalignment='left')
        plt.text(Profits[1], 1, 'Time Losses', horizontalalignment='left')
        plt.text(0, 2, 'Production Capacity', horizontalalignment='left')
        plt.text(0, 3, 'Actual Production', horizontalalignment='left')
        plt.text(Profits[3], 3, 'Speed Losses', horizontalalignment='left')
        plt.text(0, 4, 'Product Output', horizontalalignment='left')
        plt.text(0, 5, 'Actual Good Products', horizontalalignment='left')
        plt.text(Profits[5], 5, 'Defective Units', horizontalalignment='left')

        # Add x-axis label
        plt.xlabel('Percentage')
        
        # Add plot title
        plt.title('Overall Equipment Efficiency')
        
        # Show plot legends
        plt.legend()

        # Print OEE components
        return(print('Overall Equipment Effectiveness: {}%'.format(round(Profits[-1],2))))
    
    # Errors validation
    if B > A:
        print('Error. The run time cannot be greater than the total available time.')        
    if D > C:
        print('Error. The actual production cannot be greater than the production capacity.')       
    if E != D:
        print('Error. The product output must be equal to actual production.')     
    if F > E:
        print('Error. The actual good products cannot be greater than the product output.')
