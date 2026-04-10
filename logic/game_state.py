class GameState:

# Här är min tanke att vi kan spara "globala" värden som vi kan skicka in när vi skapar nya objekt.
# Detta vill jag göra så att tex vårt objekt som vi klickar på ska kunna updatera en räknare. 

    def __init__(self):
        self.score = 0
        self.kps = 0 #klick per sekund
        self.click_multiplier = 1



