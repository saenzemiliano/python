class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.pets = []
        self.points = 100
    
    def __str__(self):
        return self.name + ' ' + '[' + str(self.points) + ']'
    def __unicode__(self):
        return '%d' % (self.name)

    
