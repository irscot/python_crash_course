# What would happen if we multiply
# instead of add for the rolls and num_sides?

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in list.
results = []
for roll_num in range(1_000_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8s 1,000,000 times '
                         'and multiplying the results.',
                   xaxis=x_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

print(frequencies)
