# **Blind Auction Project**

## **Disclaimer**
This program uses the `clear()` function from the `replit` library to clear the console for each bidder. This feature ensures that each bidder's information remains confidential. The code is best executed on the Replit IDE. If you need to run it on any other IDE, you can remove line 3 and line 17, but it will affect the confidentiality of the bidding process.

## **Overview**
Welcome to the Blind Auction Project! This Python program facilitates a secret auction where multiple bidders can place their bids without seeing each other's offers. The highest bidder wins the auction.

## **Features**
- **Secret Bidding:** Each bidder's name and bid amount are kept secret until the end of the auction.
- **Multiple Bidders:** The program allows multiple bidders to place their bids.
- **Winner Announcement:** The highest bidder is announced at the end of the auction.

## **How to Run the Program**

### **Required Libraries**
- `art`: To display the logo.
- `replit`: To clear the console for each bidder.

### **Execution Steps**
1. **Welcome Message:** The program starts with a welcome message and displays the auction logo.
2. **Bidding Process:**
   - The first bidder enters their name and bid amount.
   - The program asks if there are any other bidders.
   - If "yes", the console is cleared using the `clear()` function from the `replit` library, and the next bidder can enter their details.
   - If "no", the bidding process ends.
3. **Determine the Winner:** The program iterates through all bids to find and announce the highest bidder.

## **Example Usage**

Here's how the bidding process works:
1. The program will display the auction logo and a welcome message.
2. Each bidder will be prompted to enter their name and bid amount.
3. After each bid, the program will ask if there are any other bidders.
4. The console will be cleared (in Replit) for the next bidder to enter their details.
5. Once all bids are in, the program will announce the highest bidder and their bid amount.

Enjoy managing your blind auction with this simple yet effective program!
