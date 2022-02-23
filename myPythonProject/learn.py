# -*-coding:utf-8-*-

class MethodClass:
    # class method
    @classmethod
    def demo_method(cls):
        print("this is class method")

    @staticmethod
    def static_demo(param1):
        print("static method", param1)


class Game:
    def __init__(self, first_hero, second_hero):
        self.first_hero = first_hero
        self.second_hero = second_hero

    def fight(self):
        print(f"本轮比赛开始，由{self.first_hero} VS {self.second_hero}")

    @staticmethod
    def start():
        print("游戏开始")


# 无需实例化直接调用类方法
# MethodClass.demo_method()
# MethodClass.static_demo("hello")
Game.start()
game1 = Game("Bob", "mary")
game2 = Game("Mike", "Henry")
game1.fight()
game2.fight()
