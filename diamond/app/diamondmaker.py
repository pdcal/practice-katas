class DiamondMaker:

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def diamond(self, supplied_letter):
        if (supplied_letter == None):
            raise TypeError

        supplied_letter = supplied_letter.upper()
        if(supplied_letter not in self.alphabet):
            raise ValueError

        return self.__create_diamond(supplied_letter)

    def __create_diamond(self, supplied_letter):
        if(supplied_letter == "A"):
            output_diamond = "A"
            return output_diamond

        position = self.alphabet.index(supplied_letter)
        front_padding = position
        back_padding = 0
        top_of_diamond = []

        for i in range(position+1):
            line = front_padding * " " + self.alphabet[back_padding] + back_padding * " "
            reverse = line[::-1]
            line = line + reverse[1:]
            top_of_diamond.append(line)
            back_padding = back_padding + 1
            front_padding = front_padding - 1

        bottom_of_diamond = top_of_diamond[:-1]
        bottom_of_diamond = bottom_of_diamond[::-1]

        output_diamond = top_of_diamond + bottom_of_diamond

        return output_diamond
