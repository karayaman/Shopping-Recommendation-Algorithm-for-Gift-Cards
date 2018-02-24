

**Shopping Recommendation Algorithm for Gift Cards**

**        For which problem this algorithm is useful for?**

**       ** Let&#39;s say you have a gift card and you want to spend your gift card completely. In addition you would like to buy certain type of products, that is there is a subset of products in shop which are suitable for you. Moreover you want to make the purchase such that you will pay minimum amount of money other than gift card.

  **How to use the program?**

**       ** Program first asks for the list of products in shop. For each product you should enter name, price and currency on each line. Example input:

 A 10 TL

 B 20 TL

 C 5 TL

 Then you should enter currency of prices (TL in this example), then amount of money on your gift card, limit for how many times a product can be purchased, keywords for products(Leave blank for including all products), and number of recommendations you want. Then program finds the cheapest purchase price possible and displays how these purchases can be made.

  **How it Works?**

**       ** Program first parses product list input and discards products that are not suitable. Then according to input parameters it computes cheapest possible purchase price using dynamic programming. After that in order to display how these purchases can be made program backtracks for each possible purchase and finds purchase information.

  **How to contribute?**

**       ** All contributions are welcome and feel free to send me email if you have questions.

  **Which features can be added further?**

**       ** Program finds purchases only greater than or equal to some amount, it can be modified so that an option for finding purchases that are less than or equal to some amount.

 There is an upper limit for how many times a product can be purchased but there is no lower limit. Lower limit for purchasing a product can be added.

 Products can be grouped according to their mapping keywords and so purchasing limits can be applied to groups or cheapest product in a group can be selected for making purchase.

**       **


