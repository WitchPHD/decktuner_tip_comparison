#find the fee for Ko-Fi and BuyMeACoffee

tips = []

class TIP:
    def __init__(self, dollars):
        self.amount = dollars
        #get the BuyMeACoffee Tip
        self.BMAC_FEE = dollars * 0.05
        self.BMAC_TIP = dollars - self.BMAC_FEE
        #Get the Ko-Fi stripe TIP
        self.KF_STRIPE_FEE = (dollars * 0.029) + 0.30
        self.KF_STRIPE_TIP = dollars - self.KF_STRIPE_FEE
        #Get the Ko-Fi stripe INTERNATIONAL TIP
        self.KF_STRIPEIN_FEE = (dollars * 0.029) + (dollars * 0.015) + 0.30
        self.KF_STRIPEIN_TIP = dollars - self.KF_STRIPEIN_FEE
        #Get the Ko-Fi PayPal TIP
        self.KF_PAYPAL_FEE = (dollars * 0.0289) + 0.49
        self.KF_PAYPAL_TIP = dollars - self.KF_PAYPAL_FEE
        #Get the Ko-Fi PayPal INTERNATIONAL TIP
        self.KF_PAYPALIN_FEE = (dollars * 0.0289) + (dollars * 0.015) + 0.49
        self.KF_PAYPALIN_TIP = dollars - self.KF_PAYPALIN_FEE

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
KF_STRIPEIN_FEE_TOT = 0
KF_STRIPEIN_TIP_TOT = 0
KF_PAYPALIN_FEE_TOT = 0
KF_PAYPALIN_TIP_TOT = 0
KF_STRIPE_FEE_TOT = 0
KF_STRIPE_TIP_TOT = 0
KF_PAYPAL_FEE_TOT = 0
KF_PAYPAL_TIP_TOT = 0
BMAC_FEE_TOT = 0
BMAC_TIP_TOT = 0
TIP_TOT = 0

print ('\n')
for t in tips:
    #print each tip and add them to counters
    print('{:.2f}$ tip costs: {:.2f}$ BMAC, {:.2f}$ Ko-Fi (Stripe), and {:.2f}$ Ko-Fi (Paypal) '.format(t.amount, t.BMAC_FEE, t.KF_STRIPE_FEE, t.KF_PAYPAL_FEE))
    KF_STRIPEIN_FEE_TOT = KF_STRIPEIN_FEE_TOT + t.KF_STRIPEIN_FEE
    KF_STRIPEIN_TIP_TOT = KF_STRIPEIN_TIP_TOT + t.KF_STRIPEIN_TIP
    KF_PAYPALIN_FEE_TOT = KF_PAYPALIN_FEE_TOT + t.KF_PAYPALIN_FEE
    KF_PAYPALIN_TIP_TOT = KF_PAYPALIN_TIP_TOT + t.KF_PAYPALIN_TIP
    KF_STRIPE_FEE_TOT = KF_STRIPE_FEE_TOT + t.KF_STRIPE_FEE
    KF_STRIPE_TIP_TOT = KF_STRIPE_TIP_TOT + t.KF_STRIPE_TIP
    KF_PAYPAL_FEE_TOT = KF_PAYPAL_FEE_TOT + t.KF_PAYPAL_FEE
    KF_PAYPAL_TIP_TOT = KF_PAYPAL_TIP_TOT + t.KF_PAYPAL_TIP
    BMAC_FEE_TOT = BMAC_FEE_TOT + t.BMAC_FEE
    BMAC_TIP_TOT = BMAC_TIP_TOT + t.BMAC_TIP
    TIP_TOT = TIP_TOT + t.amount

#print and format the results
print ('\nRESULTS FOR {:} TIPS TOTALING {:.2f}$:'.format(n-1, TIP_TOT))
print ('\n    BuyMeACoffee:')
print ('        BuyMeACoffee: you pay {:.2f}$ in fees and pocket {:.2f}$.'.format(BMAC_FEE_TOT, BMAC_TIP_TOT))
print ('        (w/ "cover credit card fees" unchecked)') 
print ('\n    Ko-Fi:')
print ('        Ko-Fi (Stripe): you pay {:.2f}$ in fees and pocket {:.2f}$.'.format(KF_STRIPE_FEE_TOT, KF_STRIPE_TIP_TOT))
print ('        Ko-Fi (Paypal): you pay {:.2f}$ in fees and pocket {:.2f}$.'.format(KF_PAYPAL_FEE_TOT, KF_PAYPAL_TIP_TOT))
print ('        Ko-Fi (Stripe - International): you pay {:.2f}$ in fees and pocket {:.2f}$.'.format(KF_STRIPEIN_FEE_TOT, KF_STRIPEIN_TIP_TOT))
print ('        Ko-Fi (Paypal - International): you pay {:.2f}$ in fees and pocket {:.2f}$.'.format(KF_PAYPALIN_FEE_TOT, KF_PAYPALIN_TIP_TOT))
print ('        Ko-Fi (Average): you pay {:.2f}$ in fees and pocket {:.2f}$.'.format((KF_PAYPAL_FEE_TOT+KF_STRIPE_FEE_TOT+KF_PAYPALIN_FEE_TOT+KF_STRIPEIN_FEE_TOT)/4, (KF_PAYPAL_TIP_TOT+KF_STRIPE_TIP_TOT+KF_PAYPALIN_TIP_TOT+KF_STRIPEIN_TIP_TOT)/4))
input('\nHIT ENTER TO TERMINATE THE PROGRAM.')

