import json
import os
from datetime import datetime
try:
    import pandas as pd
    import matplotlib.pyplot as plt
    ADVANCED = True
except ImportError:
    ADVANCED = False
    print("⚠️ Install required packages: pip install pandas matplotlib")

class StoneTycoon:
    def __init__(self):
        self.database = "stone_db.json"
        self.load_data()
        
    def load_data(self):
        if os.path.exists(self.database):
            with open(self.database, 'r') as f:
                self.records = json.load(f)
        else:
            self.records = []
    
    def save_data(self):
        with open(self.database, 'w') as f:
            json.dump(self.records, f, indent=4)
    
    def calculate_empire(self):
        try:
            stone = int(input("Enter stone quantity 📋: "))
            price = int(input("Enter price per stone 💴: "))
            buyer = input("Enter buyer name 👤: ")
            
            total = stone * price
            profit = total * 0.2  # 20% profit margin
            
            deal = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "buyer": buyer,
                "quantity": stone,
                "price": price,
                "total": total,
                "profit": profit
            }
            
            self.records.append(deal)
            self.save_data()
            
            print(f"\n💰 DEAL CLOSED: {total} PKR")
            print(f"📈 PROFIT: {profit} PKR")
            print(f"👑 EMPIRE LEVEL: {self.get_rank(total)}")
            
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
    
    def get_rank(self, total):
        ranks = [
            (1000000, "🌌 UNIVERSE TYCOON"),
            (500000, "💎 DIAMOND MOGUL"),
            (100000, "👑 GOLD EMPEROR"),
            (50000, "💰 SILVER KING"),
            (10000, "📦 BRONZE TRADER"),
            (0, "😂 INTERN")
        ]
        for amount, rank in ranks:
            if total >= amount: return rank
    
    def show_dashboard(self):
        if not self.records:
            print("❌ No deals recorded yet")
            return
            
        if ADVANCED:
            df = pd.DataFrame(self.records)
            print("\n📊 BUSINESS DASHBOARD:")
            print(df[['date', 'buyer', 'total', 'profit']])
            print(f"\n💸 TOTAL REVENUE: {df['total'].sum()} PKR")
            print(f"📈 TOTAL PROFIT: {df['profit'].sum()} PKR")
            
            # Generate graph
            df.plot(x='buyer', y='total', kind='bar', title='Sales by Buyer')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('sales_chart.png')
            print("✅ Graph saved: sales_chart.png")
        else:
            for r in self.records:
                print(f"{r['date']} | {r['buyer']} | {r['total']} PKR")

    def ceo_login(self):
        password = input("🔐 Enter CEO Password: ")
        if password == "sher123":
            return True
        else:
            print("❌ ACCESS DENIED. Intern level access only 😂")
            return False

def main():
    app = StoneTycoon()
    print("🚀 STONE SOFTWARE COMPANY v3.1 💣")
    print("INTERNATIONAL EDITION 🦾\n")
    
    if not app.ceo_login(): return
    
    while True:
        print("\n=== CEO PANEL ===")
        print("1. Add New Deal")
        print("2. View Business Dashboard") 
        print("3. Shutdown Empire")
        
        choice = input("Enter Command: ")
        
        if choice == "1": app.calculate_empire()
        elif choice == "2": app.show_dashboard()
        elif choice == "3": 
            print("SHUTTING DOWN STONE INDUSTRIES... 💎")
            break
        else: print("Invalid command 😂 Please enter 1, 2 or 3")

if __name__ == "__main__":
    main()#