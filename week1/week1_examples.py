
'''
Machine Learning: Regression

Computing regression parameters (closed form example)

We want the line that best fits this data set as measured by residual sum of squares -
the simple linear regression cost. We have a closed form solution that involves the following terms:

    The number of data points (N)
    The sum (or mean) of the Ys
    The sum (or mean) of the Xs
    The sum (or mean) of the product of the Xs and the Ys
    The sum (or mean) of the Xs squared

Then once we have calculated all of these terms, we can use the formulas to compute the slope and intercept.
Recall that we first solve for the slope and then we use the value of the slope to solve for the intercept.
The formula for the slope is a fraction with:

numerator = (sum of X*Y) - (1/N)*((sum of X) * (sum of Y))
denominator = (sum of X**2) - (1/N)*((sum of X) * (sum of X))

Note that you can divide both the numerator and denominator by N (which does not change the answer!) to get:

numerator = (mean of X * Y) - (mean of X)*(mean of Y)
denominator = (mean of X**2) - (mean of X)*(mean of X)

Hence, we can use either the sum or the means.
'''

import math
from matplotlib import pyplot as plt

x_data = [0, 1, 2, 3, 4]
y_data = [1, 3, 7, 13, 21]

# Method 1 - using sums

n = 5 #=5
y_sum = sum(y_data) #=45
x_sum = sum(x_data) #=10
sum_x_and_y_product = sum([a * b for a, b in zip(x_data, y_data)]) #=140
x_squared = sum(val ** 2 for val in x_data) #=30

numerator = sum_x_and_y_product - 1/float(n) * (x_sum * y_sum) #=50
denominator = x_squared - 1/float(n) * (x_sum * x_sum) #=10
slope = numerator / denominator #=5

# Method 2 - using means

y_mean = sum(y_data) / float(len(y_data)) #=9
x_mean = sum(x_data) / float(len(x_data)) #=2
mean_x_and_y_product = sum([a * b for a, b in zip(x_data, y_data)]) / float(len(x_data)) #=28
x_squared_mean = sum(val ** 2 for val in x_data) / float(len(x_data)) #=6

numerator = mean_x_and_y_product - (x_mean * y_mean) #=10
denominator = x_squared_mean - (x_mean * x_mean) #=2
slope = numerator / float(denominator) #=5

'''
Then, we can use this computed slope to compute the intercept:
intercept = (mean of Y) - slope * (mean of X)
'''
intercept = y_mean - slope * x_mean #=-1

# best fit line data
best_fit_line = [slope * x + intercept for x in range(5)]

# plot graph

plt.plot(x_data, y_data, 'bo')
plt.plot(best_fit_line, 'r')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Closed form example of best fit line')
plt.show()

'''
Computing regression parameters (gradient descent example)

Now that we have computed the regression line using a closed form solution let us do it again but with gradient descent.

Recall that:

    The derivative of the cost for the intercept is the sum of the errors
    The derivative of the cost for the slope is the sum of the product of the errors and the input

We will need a starting value for the slope and intercept, a step_size and a tolerance

    initial_intercept = 0
    initial_slope = 0
    step_size = 0.05
    tolerance = 0.01

The algorithm

In each step of the gradient descent we will do the following:

1. Compute the predicted values given the current slope and intercept
2. Compute the prediction errors (prediction - Y)
3. Update the intercept:

    compute the derivative: sum(errors)
    compute the adjustment as step_size times the derivative
    decrease the intercept by the adjustment

4. Update the slope:

    compute the derivative: sum(errors*input)
    compute the adjustment as step_size times the derivative
    decrease the slope by the adjustment

5. Compute the magnitude of the gradient
6. Check for convergence

The algorithm in action
'''

step_counter = 1

x_data = [0, 1, 2, 3, 4]
y_data = [1, 3, 7, 13, 21]

step_size = 0.05
tolerance = 0.01
intercept = 0
slope = 0

def make_steps(step_size, tolerance, intercept, slope):
    '''
    Gradient descent step process
    '''
    global step_counter

    # 1. predictions
    predictions = [slope * x + intercept for x in x_data]

    # 2. errors
    errors = [x-y for x,y in zip(predictions, y_data)] # [-1, -3, -7, -13, -21]

    # 3. update intercept
    sum_errors = sum(errors) #-45
    adjustment = step_size * sum_errors  # 0.05 * -45 = -2.25
    intercept -= adjustment #2.25

    # 4. update slope
    sum_x_and_errors = sum([a * b for a, b in zip(x_data, errors)]) #-140
    adjustment = step_size * sum_x_and_errors  # 0.05 * -140 = -7
    slope -= adjustment # -7

    # 5. magnitude

    magnitude = math.sqrt((sum_errors**2) + (sum_x_and_errors**2)) #147.05

    # 6. magnitude vs tolerance

    print 'step:', step_counter, 'difference:', magnitude - tolerance

    if magnitude > tolerance:
        step_counter += 1
        make_steps(step_size, tolerance, intercept, slope)
    else:
        plt.plot(x_data, y_data, 'bo')
        plt.plot(predictions, 'r')
        plt.xlabel('x values')
        plt.ylabel('y values')
        graph_title = 'Gradient descent example of best fit line after %d steps' % (step_counter)
        plt.title(graph_title)
        plt.show()

make_steps(step_size, tolerance, intercept, slope)

'''
Homework question 5 and 6

Your friend in the U.S. gives you a simple regression fit for predicting house prices from square feet.
The estimated intercept is -44850 and the estimated slope is 280.76.
You believe that your housing market behaves very similarly, but houses are measured in square meters.
To make predictions for inputs in square meters, what intercept and slope must you use?
Hint: there are 0.092903 square meters in 1 square foot.
'''

intercept = -44850
slope = 280.76

new_intercept = -44850
new_slope = slope * (1/0.092903) # ~3022
