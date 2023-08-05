class Argument:
    def __init__(self):
        self.option = []
        self.optionValues = {}

    def parse_args(self, args):
        for arg in args:
            if arg.startswith('--'):
                self.option.append(arg)
                if args.index(arg) + 1 < len(args):
                    self.optionValues[arg] = args[args.index(arg) + 1]
            
