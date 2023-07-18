#find the fee for Ko-Fi and BuyMeACoffee

tips = []

class TIP:
    def __init__(self, dollars):
        self.cents = float(dollars * 100)
        #get the BuyMeACoffee Tip
        self.BMAC_FEE = self.cents * 0.05
        self.BMAC_TIP = self.cents - self.BMAC_FEE
        #Get the Ko-Fi stripe TIP
        self.KF_STRIPE_FEE = (self.cents * 0.029) + 30
        self.KF_STRIPE_TIP = self.cents - self.KF_STRIPE_FEE
        #Get the Paypal stripe TIP
        self.KF_PAYPAL_FEE = (self.cents * 0.030) + 45
        self.KF_PAYPAL_TIP = self.cents - self.KF_PAYPAL_FEE

print ('Please enter all tips in $USD$ dollar amounts without special characters.\n')
print ('When you are finished entering tips, type \'done\' and hit enter.\n')

#ask for all the
n = 1
while True:
    try:
        x = float(input('Enter tip {:}: '.format(n)))
        tips.append(TIP(x))
        n = n + 1
    except:
        break

#generate some counters
KF_STRIPE_FEE_TOT = 0
KF_STRIPE_TIP_TOT = 0
KF_PAYPAL_FEE_TOT = 0
KF_PAYPAL_TIP_TOT = 0
BMAC_FEE_TOT = 0
BMAC_TIP_TOT = 0


print ('\n')
for t in tips:
    #print each tip and add them to counters
    print("{:.2f}$ tip costs: {:.0f}¢ BMAC, {:.0f}¢ Ko-Fi (Stripe), and {:.0f}¢ Ko-Fi (Paypal) ".format(t.cents/100, t.BMAC_FEE, t.KF_STRIPE_FEE, t.KF_PAYPAL_FEE))
    KF_STRIPE_FEE_TOT = KF_STRIPE_FEE_TOT + t.KF_STRIPE_FEE
    KF_STRIPE_TIP_TOT = KF_STRIPE_TIP_TOT + t.KF_STRIPE_TIP
    KF_PAYPAL_FEE_TOT = KF_PAYPAL_FEE_TOT + t.KF_PAYPAL_FEE
    KF_PAYPAL_TIP_TOT = KF_PAYPAL_TIP_TOT + t.KF_PAYPAL_TIP
    BMAC_FEE_TOT = BMAC_FEE_TOT + t.BMAC_FEE
    BMAC_TIP_TOT = BMAC_TIP_TOT + t.BMAC_TIP

print ('\nRESULTS:')
print ('\nWith BuyMeACoffee: you pay {:.2f}$ in fees and pocket {:.2f}$.'.format(BMAC_FEE_TOT/100, BMAC_TIP_TOT/100))
print ('\nWith Ko-Fi (Stripe): you pay {:.2f}$ in fees and pocket {:.2f}$.'.format(KF_STRIPE_FEE_TOT/100, KF_STRIPE_TIP_TOT/100))
print ('\nWith Ko-Fi (Paypal): you pay {:.2f}$ in fees and pocket {:.2f}$.'.format(KF_PAYPAL_FEE_TOT/100, KF_PAYPAL_TIP_TOT/100))
print ('\nWith Ko-Fi (Average): you pay {:.2f}$ in fees and pocket {:.2f}$.'.format((KF_PAYPAL_FEE_TOT+KF_STRIPE_FEE_TOT)/2/100, (KF_PAYPAL_TIP_TOT+KF_STRIPE_TIP_TOT)/2/100))
