import random

# === Класс Hero ===
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")
        other.health -= damage
        if other.health < 0:
            other.health = 0
        print(f"У {other.name} осталось {other.health} здоровья.\n")

    def is_alive(self):
        return self.health > 0


# === Класс Game ===
class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: Семен ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("\n⚔️ Добро пожаловать в текстовую боевую игру! ⚔️\n")
        turn = 0  # 0 - ход игрока, 1 - ход компьютера

        while self.player.is_alive() and self.computer.is_alive():
            if turn == 0:
                self.player_turn()
            else:
                self.computer_turn()
            turn = 1 - turn  # Переключение хода

        self.declare_winner()

    def player_turn(self):
        input(f"{self.player.name}, нажмите Enter, чтобы атаковать...")
        self.player.attack(self.computer)

    def computer_turn(self):
        print("Ход компьютера:")
        self.computer.attack(self.player)

    def declare_winner(self):
        if self.player.is_alive():
            print(f"🏆 Поздравляем, {self.player.name}! Вы победили!")
        else:
            print("💀 К сожалению, вы проиграли. Компьютер победил.")


# === Запуск игры ===
if __name__ == "__main__":
    game = Game()
    game.start()