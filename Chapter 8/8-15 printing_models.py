# Import functions from another .py file.
# Use as 'type abbreviated function name here' to abbreviate the function when calling it.
import printing_functions as pf

unprinted_designs = ['keyblade', 'dragon ball', 'headband']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
