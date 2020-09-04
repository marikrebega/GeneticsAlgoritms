class ExtremumValues:
    def value(self, gen, ext):
        ext_value = self.my_func(gen[0])
        for i in range(len(gen)):
            value = self.my_func(gen[i])
            if ext:
                if ext_value < value:
                    ext_value = value
            else:
                if ext_value > value:
                    ext_value = value
        return ext_value

    @staticmethod
    def my_func(person):
        a = 12
        b = -8
        c = -40
        d = 3
        value = a + (b * person) + (c * person ^ 2) + (d * person ^ 3)
        return value
