# cash_flows class

class CashFlows:
    def __init__(self):
        self.maturities = []
        self.amounts = []
    
    # add a cash flow to the cash flow list you good thing
    def add_cash_flow(self, maturity, amount):
        self.maturities.append(maturity)
        self.amounts.append(amount)

    def get_cash_flow(self, maturity):
        if maturity in self.maturities:
            return self.amounts[self.maturities.index(maturity)]
        else:
            return None
        
    def get_maturities(self):
        return list(self.maturities)
    
    def get_amounts(self):
        return list(self.amounts)
    
    def get_cash_flows(self):
        return list(zip(self.maturities, self.amounts))
        
# create a class for a bond that inherits from CashFlows
class Bank_bill(CashFlows):

    def __init__(self, face_value=100, maturity=.25, ytm=0.00, price=100):
        super().__init__()
        self.face_value = face_value
        self.maturity = maturity
        self.ytm = ytm
        self.price = price

    def set_face_value(self, face_value):
        self.face_value = face_value

    def set_maturity(self, maturity):
        self.maturity = maturity

    def set_ytm(self, ytm):
        self.ytm = ytm
        self.price = self.face_value/(1 + ytm*self.maturity)

    def set_price(self, price):
        self.price = price
        self.ytm = (self.face_value/price - 1)/self.maturity

    def get_price(self):
        return self.price
    
    def get_face_value(self):
        return self.face_value
    
    def get_maturity(self):
        return self.maturity
    
    def get_ytm(self):
        return self.ytm
    
    def set_cash_flows(self):
        self.add_cash_flow(0, -self.price)
        self.add_cash_flow(self.maturity, self.face_value)

# create a class for a bond that inherits from CashFlows
class Bond(CashFlows):
    
    def __init__(self, face_value=100, maturity=3, coupon=0, frequency=4, ytm=0, price=100):
        super().__init__()
        self.face_value = face_value    
        self.maturity = maturity
        self.coupon = coupon
        self.frequency = frequency
        self.ytm = ytm
        self.price = price
    
    def set_face_value(self, face_value):
        self.face_value = face_value

    def set_maturity(self, maturity):
        self.maturity = maturity

    def set_coupon(self, coupon):
        self.coupon = coupon

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_ytm(self, ytm):
        self.ytm = ytm
        # set the price of the bond using the bond formula
        self.price = (self.face_value*self.coupon/self.frequency)*(1-(1+ytm/self.frequency)**(-self.maturity*self.frequency))/(ytm/self.frequency) \
          + self.face_value/((1 + ytm/self.frequency)**(self.maturity*self.frequency))

    def get_price(self):
        return self.price
    
    def get_face_value(self):
        return self.face_value
    
    def get_maturity(self):
        return self.maturity
    
    def get_coupon_rate(self):
        return self.coupon
    
    def get_ytm(self):
        return self.ytm
    
    def set_cash_flows(self):
        self.add_cash_flow(0, -self.price)
        for i in range(1, self.maturity*self.frequency):
            self.add_cash_flow(i/self.frequency, self.face_value*self.coupon/self.frequency)
        self.add_cash_flow(self.maturity, self.face_value + self.face_value*self.coupon/self.frequency)

# create a class for portfolio that inherits from CashFlows and contains Bonds and Bank_bills
class Portfolio(CashFlows):
    
    def __init__(self):
        super().__init__()
        self.bonds = []
        self.bank_bills = []
    
    def add_bond(self, bond):
        self.bonds.append(bond)
    
    def add_bank_bill(self, bank_bill):
        self.bank_bills.append(bank_bill)
    
    def get_bonds(self):
        return self.bonds
    
    def get_bank_bills(self):
        return self.bank_bills
    
    def set_cash_flows(self):
        for bond in self.bonds:
            for cash_flow in bond.get_cash_flows():
                self.add_cash_flow(cash_flow[0], + cash_flow[1])
        for bank_bill in self.bank_bills:
            for cash_flow in bank_bill.get_cash_flows():
                self.add_cash_flow(cash_flow[0], + cash_flow[1])
