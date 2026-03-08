from app.facade import CalculatorFacade
from app.exceptions import CalculatorError, InvalidInputError


class CalculatorREPL:
    """Command-line calculator application."""

    def __init__(self):
        """Create the REPL with a calculator facade."""
        self.facade = CalculatorFacade()
        self.running = True

    def show_help(self):
        """Display the available commands."""
        print("\nAvailable commands:")
        print("  add <a> <b>")
        print("  subtract <a> <b>")
        print("  multiply <a> <b>")
        print("  divide <a> <b>")
        print("  power <a> <b>")
        print("  root <a> <b>")
        print("  modulo <a> <b>")
        print("  int_divide <a> <b>")
        print("  percent_diff <a> <b>")
        print("  percent_change <a> <b>")
        print("  history")
        print("  clear")
        print("  save")
        print("  load")
        print("  help")
        print("  exit\n")

    def parse_number(self, value):
        """Convert user input into a number."""
        try:
            return float(value)
        except ValueError as error:
            raise InvalidInputError(f"Invalid number: {value}") from error

    def handle_command(self, user_input):
        """
        Handle one command entered by the user.

        Parameters:
            user_input (str): The raw input string from the user
        """
        parts = user_input.strip().split()

        if not parts:
            print("Please enter a command.")
            return

        command = parts[0].lower()

        if command == "help":
            self.show_help()
            return

        if command == "exit":
            print("Exiting calculator. Goodbye!")
            self.running = False
            return

        if command == "history":
            records = self.facade.get_history()
            if not records:
                print("No calculation history found.")
                return

            print("\nCalculation History:")
            for index, record in enumerate(records, start=1):
                print(
                    f"{index}. {record['operation']} {record['a']} {record['b']} = "
                    f"{record['result']} at {record['timestamp']}"
                )
            print()
            return

        if command == "clear":
            self.facade.clear_history()
            print("Calculation history cleared.")
            return

        if command == "save":
            self.facade.save_history("data/calculator_history.csv")
            print("History saved to data/calculator_history.csv")
            return

        if command == "load":
            self.facade.load_history("data/calculator_history.csv")
            print("History loaded from data/calculator_history.csv")
            return

        if len(parts) != 3:
            print("Invalid command format. Type 'help' for instructions.")
            return

        try:
            a = self.parse_number(parts[1])
            b = self.parse_number(parts[2])
            result = self.facade.calculate(command, a, b)
            print(f"Result: {result}")
        except CalculatorError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Unexpected error: {error}")

    def run(self):
        """Start the REPL loop."""
        print("Welcome to the Advanced Calculator!")
        print("Type 'help' to see available commands.\n")

        while self.running:
            user_input = input("calculator> ")
            self.handle_command(user_input)