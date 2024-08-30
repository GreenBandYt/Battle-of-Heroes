import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other, attack_type="standard"):
        """Атакует другого героя, отнимая у него здоровье в зависимости от типа атаки."""
        if self.is_alive():
            damage = self.calculate_damage(attack_type)
            print(f"{self.name} атакует {other.name} и наносит {damage} урона!")
            other.health -= damage
        else:
            print(f"{self.name} не может атаковать, так как уже побежден!")

    def calculate_damage(self, attack_type):
        """Рассчитывает урон в зависимости от типа атаки."""
        if attack_type == "standard":
            return self.attack_power
        elif attack_type == "strong":
            return random.randint(self.attack_power, self.attack_power * 2)
        elif attack_type == "weak":
            return random.randint(1, self.attack_power // 2)
        else:
            return self.attack_power

    def is_alive(self):
        """Проверяет, жив ли герой (здоровье больше 0)."""
        return self.health > 0


class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        """Начинает игру, чередуя ходы игрока и компьютера, пока один из героев не умрет."""
        print("Игра началась!")
        print(f"Игрок: {self.player.name} vs Компьютер: {self.computer.name}")
        print("=" * 30)

        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player_turn()
            if not self.computer.is_alive():
                break

            # Ход компьютера
            self.computer_turn()
            print("=" * 30)

        self.show_winner()

    def player_turn(self):
        """Выполняет ход игрока."""
        attack_type = self.get_attack_choice()
        self.player.attack(self.computer, attack_type)
        self.show_health()

    def computer_turn(self):
        """Выполняет ход компьютера."""
        print(f"Ход компьютера!")
        attack_type = random.choice(["standard", "strong", "weak"])
        self.computer.attack(self.player, attack_type)
        self.show_health()

    def get_attack_choice(self):
        """Запрашивает у игрока выбор типа атаки."""
        while True:
            print("Выберите тип атаки:")
            print("1. Стандартная атака")
            print("2. Сильная атака (может нанести больше урона)")
            print("3. Слабая атака (может нанести меньше урона)")
            choice = input("Ваш выбор (1/2/3): ")
            if choice == '1':
                return "standard"
            elif choice == '2':
                return "strong"
            elif choice == '3':
                return "weak"
            else:
                print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")

    def show_health(self):
        """Показывает текущее здоровье обоих героев."""
        print(f"{self.player.name}: {self.player.health} здоровья")
        print(f"{self.computer.name}: {self.computer.health} здоровья")

    def show_winner(self):
        """Объявляет победителя игры."""
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


# Запуск игры
game = Game()
game.start()
