from typing import TextIO

class Decoder:
    def __init__(self, file: TextIO):
        self.file = file
        self.__my_list = self.__open_file().split("\n")
    
    def __open_file(self):
        with open(self.file, "r") as f:
            contenu = f.read()
        return contenu
    
    def __extract_digit(self):
        coord = []
        for line in self.__my_list:
            coord_line = [e for e in line if e.isdigit()]
                
            coord.append("".join(coord_line))
        
        return coord
    
    def __get_first_and_last_digit(self):
        return [int((n[0] + n[-1])) for n in self.__extract_digit()]
    
    def sum_coord(self):
        return sum(self.__get_first_and_last_digit())