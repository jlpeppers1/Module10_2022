
class Invoice:

    #Step 1, get your init working
        #hint: look at previous assignments to see how to make an empty dictionary
    #Step 2, figure out how to get your add_item function to take a dictionary in and update the object's dictionary
    #Step 3, start working through create_invoice() assignment
        #work through pseudocode


# Driver code (you shouldn't have to modify this)
if __name__ == "__main__":
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()

#output should look like this; TAX is 6% or 0.06
'''
iPad.....$799.99
Surface.....$999.99
Tax......... $108.00
Total.......$1907.98
'''
