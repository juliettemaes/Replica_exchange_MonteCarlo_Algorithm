# Libraries
from variables import AA_DICT

# Classes
class Sequence():
    def __init__(self, sequence : str):
        if len(sequence) > 50:
            raise ValueError("Sequence is too long, should be less than 50 amino acids")
        for aa in sequence:
            if aa not in AA_DICT:
                raise ValueError(f"Invalid amino acid: {aa}")
            else:
                self.sequence = sequence
                self.length = len(sequence)
                self.hp_sequence = self.HP_convert()
                self.aa_coord = self.aa_coord_generator()

    def __str__(self):
        return self.sequence

    def HP_convert(self):
        return "".join(AA_DICT[aa] for aa in self.sequence)

    def aa_coord_generator(self):
        # Generate the coordinates of the amino acids of the sequence
        aa_coord = []
        for i, aa in enumerate(self.hp_sequence):
            dict_aa = {}
            dict_aa["type"] = aa
            dict_aa["index"] = i
            dict_aa["chain_index"] = i + 1
            dict_aa["x"] = None
            dict_aa["y"] = None
            aa_coord.append(dict_aa)
        return aa_coord

    def aa_coord_update(self, index, x, y):
        # Update the coordinates of the amino acid at index
        self.aa_coord[index]["x"] = x
        self.aa_coord[index]["y"] = y