
// package OOP.Bank Account;
// Bank Account Simulation

// Problem:
// Design a BankAccount class with attributes like:

//     Account Number
//     Account Holder Name
//     Balance

// Add methods to:

//     Deposit money.
//     Withdraw money (ensure sufficient balance).
//     Display account details.
package oop.bankaccount;
import java.io.FileWriter;
import java.util.Scanner;

class Bank {
    String accountNumber = "";
    String accountHolderName = "";
    float balance = 0;

    public Bank(String accountNumber, String accountHolderName, float openingBalance) {
        this.accountNumber = accountNumber;
        this.accountHolderName = accountHolderName;
        this.balance = openingBalance;
    }

    void getBalance() {
        int pin = (int) (Math.random() * 9000) + 1000;
        String fileName = "messages.txt";
        try {
            FileWriter fileW = new FileWriter(fileName);
            fileW.write("Here is a 4 digit pin for accessing you balance: " + pin);
            System.out.println("PIN has been exported to " + fileName);
            fileW.close();
        } catch (Exception e) {
            System.out.println("error: " + e);
        }

        System.out.println("\n\nA 4 digit pin has been sent to you!!\n\nEnter the 4 digit PIN sent to You: ");
        Scanner sc = new Scanner(System.in);
        int pinGenerated = sc.nextInt();
        System.out.println("balance: " + ((pinGenerated == pin) ? this.balance : "Incorrect Pin"));
        sc.close();
        // return 0.0f;
    }

    // public static void main(String[] args) {
    // Bank akash = new Bank("35894044177", "Akash Kumar Roy", 500);

    // akash.getBalance();
    // }
}