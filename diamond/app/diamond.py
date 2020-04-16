# Python diamond kata ala https://github.com/davidwhitney/CodeDojos/tree/master/Diamond%20Kata
# Phil C

from diamondmaker import DiamondMaker

supplied_letter = input("Supply a letter: ")

diamondmaker = DiamondMaker()

print("\n".join(diamondmaker.diamond(supplied_letter)))
