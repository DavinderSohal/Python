class WithoutInit:
    def initialize(self, name):
        self.name = name
        return self.name


a1 = WithoutInit()
a1.initialize("Augustus")
print(a1.name)
