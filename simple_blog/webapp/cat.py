from random import randint


class Cat:
    cat_name = ''
    happy_img = 'https://www.meme-arsenal.com/memes/ea8a7c37f66285b5639ae77f046c90e8.jpg'
    sad_img = 'https://www.meme-arsenal.com/memes/5cadb8a84d938114660618511399c024.jpg'
    sleep_img = 'https://www.meme-arsenal.com/memes/ba79e03461a0f8f5db277afa1af0916c.jpg'
    age = randint(1, 10)
    satiety = 10
    happiness = 10
    activity = 'Активный'

    @staticmethod
    def set_activity(info_activity):
        if info_activity == 'sleep':
            Cat.activity = 'Спит'
            return Cat.activity
        elif info_activity == 'play':
            Cat.activity = 'Активный'
            return Cat.activity
        return Cat.activity

    @staticmethod
    def change_satiety(doing):
        if Cat.activity == 'Спит' and doing == "feed":
            return Cat.satiety
        elif doing == "feed":
            Cat.satiety += 15
            return Cat.satiety
        elif doing == "play":
            Cat.satiety -= 10
            return Cat.satiety
        return Cat.satiety

    @staticmethod
    def change_happiness(doing):
        if Cat.activity == 'Спит' and doing == "feed":
            return Cat.happiness
        elif doing == "feed":
            Cat.happiness += 5
            return Cat.happiness
        elif Cat.activity == 'Спит' and doing == "play":
            Cat.happiness -= 5
            return Cat.happiness
        elif doing == "play":
            Cat.happiness += 10
            return Cat.happiness
        elif doing == "play" and doing == 'sleep':
            Cat.happiness -= 5
            return Cat.happiness
        elif Cat.satiety > 50:
            Cat.happiness -= 30
            return Cat.happiness
        elif Cat.satiety == 50:
            Cat.happiness = 0
            return Cat.happiness
        return Cat.happiness

    @staticmethod
    def change_image():
        if Cat.activity == 'Спит':
            return Cat.sleep_img
        elif Cat.happiness < 25:
            return Cat.sad_img
        elif Cat.happiness > 25:
            return Cat.happy_img


cat = Cat()
