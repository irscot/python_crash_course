# Use list comprehension instead of a while loop.

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in list.
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Analyze results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6s 1000 times.',
                   xaxis=x_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

print(frequencies)
