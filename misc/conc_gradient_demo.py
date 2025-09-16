"""
I used this as a demo for journal club on learning how to
use Python to solve simple, daily tasks in a drug discovery
lab. I had the audience come up with what steps we need to
take to create a concentration gradient object, then translated
it into Python live, explaining the logic as we went.
"""

# GDA comes from Growth Delay Assay, a short-term viability experiment
def gda(num_concs: int, top_conc: float, dilution: int):
    conc_array = []
    counter = num_concs

    while counter > 0:
        conc_array.append(top_conc)
        top_conc /= dilution
        counter -= 1
    
    conc_array.append(0) # add 0 for vehicle control
    
    return conc_array

print(gda(9, 100, 3))