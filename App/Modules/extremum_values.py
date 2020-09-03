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

    def my_func(self, person):
        a = 14
        b = 2
        c = -26
        d = 1
        value = a + (b * person) + (c * person ^ 2) + (d * person ^ 3)
        return value
