import random
import time

def remove_sheep():
    sheep = ["Бэйли", "Ламберт", "Мэри", "Бэзил", "Клотильда"]
    sheep_str = ", ".join(sheep)
    print("🧾 Список овец:", sheep_str)

    while sheep:
        removed_sheep = random.choice(sheep)
        sheep.remove(removed_sheep)
        print(f"🤑 Продаем овцу: {removed_sheep}")
        if len(sheep) == 1:
            print(f"🧾 Осталась овца: {sheep[0]}")
        elif sheep:
            remaining_sheep = ", ".join(sheep)
            print(f"🧾 Осталось овец: {remaining_sheep}")
        time.sleep(2)
        print()

    if not sheep:
        print("🚫 Ахтунг, овец больше нет!")

if __name__ == "__main__":
    remove_sheep()
