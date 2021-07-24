class Math:
    def add(self, *args):
        result = 0
        for arg in args:
            result += arg
        return result

    def mul(self, *args):
        result = 1
        for arg in args:
            result *= arg
        return result
