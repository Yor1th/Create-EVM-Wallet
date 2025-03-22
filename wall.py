from eth_account import Account
from mnemonic import Mnemonic
import pandas as pd
import pyfiglet
from colorama import Fore, Style, init

# Инициализация colorama для поддержки цветов в консоли
init(autoreset=True)

def print_banner():
    """Выводим ASCII-арт заголовок с желтым цветом."""
    ascii_art = pyfiglet.figlet_format("Wallet Creator by NotHennadii")
    by_text = "By https://t.me/sukhanovhennadii"
    print(f"\n{Fore.YELLOW}{ascii_art}{by_text.center(80)}\n")

# Включаем поддержку Mnemonic
Account.enable_unaudited_hdwallet_features()

def get_wallet_count():
    """Запрашивает у пользователя количество кошельков для создания."""
    while True:
        try:
            num_wallets = int(input("Сколько кошельков создать? Введите число: "))
            if num_wallets > 0:
                return num_wallets
            else:
                print("Введите положительное число!")
        except ValueError:
            print("Ошибка ввода! Введите корректное число.")

def main():
    print_banner()
    
    # Запрашиваем количество кошельков
    n = get_wallet_count()
    
    # Инициализация генератора сид-фраз
    mnemo = Mnemonic("english")
    wallets = []
    
    for _ in range(n):
        try:
            # Генерация сид-фразы
            seed_phrase = mnemo.generate(strength=128)  # 12 слов
            
            # Создание кошелька из сид-фразы
            account = Account.from_mnemonic(seed_phrase)
            
            wallets.append({
                "Seed Phrase": seed_phrase,
                "Private Key": account.key.hex(),
                "Wallet Address": account.address
            })
        except Exception as e:
            print(f"Ошибка при создании кошелька: {e}")
    
    # Сохранение в wallets.txt (все данные)
    try:
        with open("wallets.txt", "w") as f:
            for wallet in wallets:
                f.write(f"{wallet['Seed Phrase']} | {wallet['Private Key']} | {wallet['Wallet Address']}\n")
    except Exception as e:
        print(f"Ошибка при сохранении wallets.txt: {e}")
    
    # Сохранение только приватных ключей в private_keys.txt
    try:
        with open("private_keys.txt", "w") as f:
            for wallet in wallets:
                f.write(f"{wallet['Private Key']}\n")
    except Exception as e:
        print(f"Ошибка при сохранении private_keys.txt: {e}")
    
    # Создание DataFrame и сохранение в Excel
    
    print(f"Генерация завершена. Кошельки сохранены: {len(wallets)}")

if __name__ == "__main__":
    main()