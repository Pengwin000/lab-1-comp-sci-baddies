# Michael Gell, Emma Heiser, Erin Dunn, Sonya Sultchouk
# Course CS:151 Prof. Mehri
# September 23, 2021
# LAb #1
# Program Inputs: Volume in mL
# Program Outputs: Volume in teaspoon & tablespoon

# program input
volume_mL = input("enter volume in mL: ")
# turn value into a float
volume_mL = float(volume_mL)

#formula for converting mL to tea spoon
tea_spoon = volume_mL // 5
#formula for converting teaspoon to tblspoon
table_spoon = tea_spoon // 3
#
tea_spoon =tea_spoon - 3 * table_spoon

print("teaspoons =" , tea_spoon)
print("tablespoon = ",table_spoon)