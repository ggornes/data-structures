class Node():
    """ binary node """
    def __init__(self, char):
        self.val = char
        self.dot = None
        self.dash = None

class Morse_Code_Tree():
    """ Class that initializes and populates a binary tree for translating morse code strings into letters.
    """
    def __init__(self):
        self.root = Node("*")

        # letters = "ETIANMSURWDKGOHVF*L*PJBXCYZQ**54*3***2**+****16=/*****7***8*90"
        letters = "ETIANMSURWDKGOHVF*L*PJBXCYZQ"

        current = self.root
        nexts = []

        for char in letters:
            if current.dot == None:
                current.dot = Node(char)
            else:
                if current.dash == None:
                    current.dash = Node(char)
                else:
                    nexts.append(current.dot)
                    nexts.append(current.dash)
                    current = nexts.pop(0)
                    current.dot = Node(char)

    def translate_signal_to_letter(self, signal):
        """method that takes a string input of morse code, traverses the morse code binary tree, and returns a letter
        """
        current = self.root
        for char in signal:
            if char == ".":
                current = current.dot
            else:
                current = current.dash
        return current.val

    def translate_message(self, message):
        decoded_message = ""
        signals = message.split(" ")
        for s in signals:
            letter = self.translate_signal_to_letter(s)
            decoded_message += letter
        return decoded_message


if __name__ == "__main__":
    tree = Morse_Code_Tree()
    msg = ".... . .-.. .-.. ---  - .... .. ...  .. ...  .-  ... . -.-. .-. . -  -- . ... ... .- --. ."
    # try:
    #     result = tree.translate_message(msg)
    #     print(result)
    # except:
    #     print("Error")

    result = tree.translate_message(msg)
    print(result)
