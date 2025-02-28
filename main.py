import sys
from typing import List

def main():
    args = sys.argv
    
    match(args[0]):
        case "char":
            match(args[1]):
                case "add":
                    add_character(args[2:])
                case "remove":
                    remove_character(args[2:])
                case "set":
                    set_character(args[2])
                case "current":
                    current_character()
                case _:
                    unknown_option(args[1])
        case "roll":
            roll(args[1:])
        case "abilities":
            print("Not Implemented Yet")
        case _:
            unknown_option(args[0])

def unknown_option(opt: str):
    print(f"Unknown Option: {opt}")
    sys.exit(0)
    
def roll(args: list[str]) -> None:
    character = get_current_character()
    match(args[0]):
        case "mig":
            stat1 = character.might
        case "dex":
            stat1 = character.dexterity
        case "ins":
            stat1 = character.insight
        case "wlp":
            stat1 = character.willpower
        case _:
            unknown_option(args[0])
    match(args[0]):
        case "mig":
            stat2 = character.might
        case "dex":
            stat2 = character.dexterity
        case "ins":
            stat2 = character.insight
        case "wlp":
            stat2 = character.willpower
        case _:
            unknown_option(args[0])

def get_current_character() -> Character:
    pass #TODO

class Character:
    def __init__(self, name: str, might: int, dexterity: int, insight: int, willpower: int, level: int) -> None:
        self.name: str = name

        self.might: int = might
        self.dexterity: int = dexterity
        self.insight: int = insight 
        self.willpower: int = willpower
        
        self.hp: int = level + 5 * might
        self.mp: int = level + 5 * willpower

        self.defense: int = dexterity
        self.magic_defense: int = insight

        self.level: int = level
    
if __name__ == "__main__":
    main()
