from roughtest.LogicLayer.LogicHandler import LogicAPI


class menuUI:
    def __init__(self, logic_layer: LogicAPI):
        self.__LogicHandler = logic_layer

    def __prompt_options(self, valid_options: list[str]):
        valid_lower = [i.lower() for i in valid_options]

        while True:
            choice = input("> ").strip().lower()

            if choice in valid_lower:
                return choice

            print(f"Invalid input. Valid options are: {". ".join(valid_lower)}")
