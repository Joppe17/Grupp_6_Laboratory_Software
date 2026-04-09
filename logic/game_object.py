class GameObject:

# Här är min tanke att jag skapar en mall för hur våran GameObject class ska se ut. 
# Detta är ett viktigt val då alla andra objekt använder denna klassens metoder för att köras i våran game loop.

# Än så länge ser jag detta bara som en mall för hur denna klass kan se ut.

    def update(self, dt): pass
    def draw(self, screen): pass
    def handle_event(self, event): pass


