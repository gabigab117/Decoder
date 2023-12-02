from typing import TextIO

class Decoder:
    def __init__(self, file: TextIO):
        self.file = file
    
    def open_file(self):
        with open(self.file, "r") as f:
            contenu = f.read()
        return contenu
    
    def split_content(self):
        return self.open_file().split("\n")
    
    def extract_digit(self):
        coord = []
        for line in self.split_content():
            coord_line = [e for e in line if e.isdigit()]
            coord_line.append(coord_line[0]) if len(coord_line) == 1 else None
                
            coord.append("".join(coord_line))
        
        return coord
    
    def get_first_and_last_digit(self):
        return [int("".join((n[0], n[-1]))) for n in self.extract_digit()]
    
    def sum_coord(self):
        return sum(self.get_first_and_last_digit())