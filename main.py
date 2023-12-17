import random

is_used = [False, False, False, False, False, False]

def game():
    selected_bullet = random.randint(1, 6)

    while True:
        users_choice = int(input("1 ile 6 arasında bir sayı seç:"))
        if users_choice >= 7 or users_choice <= 0:
            print("Lütfen 1 ile 6 arasında bir sayı seçiniz.")
            continue

        if selected_bullet == users_choice:
            print("öldün")
            break
        else:
            print("yaşıyorsun")


game()
