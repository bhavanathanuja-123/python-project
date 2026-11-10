import mysql.connector
from decimal import Decimal, InvalidOperation


class BankAccount:

    def __init__(self, account_number, customer_name=""):
        self.account_number = account_number
        self.customer_name = customer_name

    def create_account(self, con, amount):
        cursor = con.cursor()

        try:
            if amount <= 0:
                print("Initial deposit must be greater than zero.")
                return

            cursor.execute(
                """INSERT INTO accounts
                (account_number, customer_name, balance)
                VALUES (%s, %s, %s)""",
                (self.account_number, self.customer_name, amount)
            )

            cursor.execute(
                """INSERT INTO transactions
                (account_number, transaction_type, amount, balance_after)
                VALUES (%s, %s, %s, %s)""",
                (self.account_number, "DEPOSIT", amount, amount)
            )

            con.commit()
            print("Account created successfully!")

        except mysql.connector.Error:
            con.rollback()
            raise

        finally:
            cursor.close()

    def check_balance(self, con):
        cursor = con.cursor()

        try:
            cursor.execute(
                "SELECT customer_name, balance FROM accounts "
                "WHERE account_number = %s",
                (self.account_number,)
            )

            result = cursor.fetchone()

            if result:
                print("Customer Name:", result[0])
                print("Account Number:", self.account_number)
                print("Current Balance: ₹", result[1])
            else:
                print("Account not found!")

        finally:
            cursor.close()

    def deposit(self, con, amount):
        cursor = con.cursor()

        try:
            if amount <= 0:
                print("Deposit amount must be greater than zero.")
                return

            cursor.execute(
                "SELECT balance FROM accounts WHERE account_number = %s",
                (self.account_number,)
            )

            result = cursor.fetchone()

            if result is None:
                print("Account not found!")
                return

            new_balance = Decimal(str(result[0])) + amount

            cursor.execute(
                "UPDATE accounts SET balance = %s "
                "WHERE account_number = %s",
                (new_balance, self.account_number)
            )

            cursor.execute(
                """INSERT INTO transactions
                (account_number, transaction_type, amount, balance_after)
                VALUES (%s, %s, %s, %s)""",
                (self.account_number, "DEPOSIT", amount, new_balance)
            )

            con.commit()
            print("Deposit successful!")
            print("Current Balance: ₹", new_balance)

        except mysql.connector.Error:
            con.rollback()
            raise

        finally:
            cursor.close()

    def withdraw(self, con, amount):
        cursor = con.cursor()

        try:
            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
                return

            cursor.execute(
                "SELECT balance FROM accounts WHERE account_number = %s",
                (self.account_number,)
            )

            result = cursor.fetchone()

            if result is None:
                print("Account not found!")
                return

            balance = Decimal(str(result[0]))

            if amount > balance:
                print("Insufficient balance!")
                return

            new_balance = balance - amount

            cursor.execute(
                "UPDATE accounts SET balance = %s "
                "WHERE account_number = %s",
                (new_balance, self.account_number)
            )

            cursor.execute(
                """INSERT INTO transactions
                (account_number, transaction_type, amount, balance_after)
                VALUES (%s, %s, %s, %s)""",
                (self.account_number, "WITHDRAW", amount, new_balance)
            )

            con.commit()
            print("Withdrawal successful!")
            print("Remaining Balance: ₹", new_balance)

        except mysql.connector.Error:
            con.rollback()
            raise

        finally:
            cursor.close()

    def transaction_history(self, con):
        cursor = con.cursor()

        try:
            cursor.execute(
                """SELECT transaction_type, amount,
                          transaction_date, balance_after
                   FROM transactions
                   WHERE account_number = %s
                   ORDER BY transaction_id DESC""",
                (self.account_number,)
            )

            rows = cursor.fetchall()

            if not rows:
                print("No transactions found.")
                return

            print("\n--- TRANSACTION HISTORY ---")

            for row in rows:
                print(
                    "Type:", row[0],
                    "| Amount: ₹", row[1],
                    "| Date:", row[2],
                    "| Balance: ₹", row[3]
                )

        finally:
            cursor.close()


def main():
    con = None

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bhavana22@",
            database="bank_db"
        )

        if not con.is_connected():
            print("Database connection failed.")
            return

        while True:
            print("\n===== BANK MANAGEMENT SYSTEM =====")
            print("1. Create Account")
            print("2. Check Balance")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                acc_no = input("Enter account number: ").strip()
                name = input("Enter customer name: ").strip()

                if not acc_no or not name:
                    print("Account number and name are required.")
                    continue

                amount = Decimal(
                    input("Enter initial deposit: ").strip()
                )

                account = BankAccount(acc_no, name)
                account.create_account(con, amount)

            elif choice in ("2", "3", "4", "5"):
                acc_no = input("Enter account number: ").strip()

                if not acc_no:
                    print("Account number is required.")
                    continue

                account = BankAccount(acc_no)

                if choice == "2":
                    account.check_balance(con)

                elif choice == "3":
                    amount = Decimal(
                        input("Enter deposit amount: ").strip()
                    )
                    account.deposit(con, amount)

                elif choice == "4":
                    amount = Decimal(
                        input("Enter withdrawal amount: ").strip()
                    )
                    account.withdraw(con, amount)

                elif choice == "5":
                    account.transaction_history(con)

            elif choice == "6":
                print("Thank you for using our banking system!")
                break

            else:
                print("Invalid choice! Please select 1 to 6.")

    except (mysql.connector.Error, InvalidOperation, ValueError) as e:
        print("Error:", e)

    finally:
        if con is not None and con.is_connected():
            con.close()


if __name__ == "__main__":
    main()






