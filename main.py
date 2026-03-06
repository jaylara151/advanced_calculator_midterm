from app.repl import CalculatorREPL


def main():
    """Start the calculator application."""
    app = CalculatorREPL()
    app.run()


if __name__ == "__main__":
    main()