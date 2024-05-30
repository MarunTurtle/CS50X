// Function prototype for calculating half of the bill
float half(float bill, float tax, int tip);

int main(void)
{
    // Prompt user for the bill amount before tax and tip
    float bill_amount = get_float("Bill before tax and tip: ");
    
    // Prompt user for the sales tax percentage
    float tax_percent = get_float("Sale Tax Percent: ");
    
    // Prompt user for the tip percentage
    int tip_percent = get_int("Tip percent: ");

    // Calculate and display the amount each person owes
    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}

// Function to calculate half of the total bill including tax and tip
float half(float bill, float tax, int tip)
{
    // Calculate the total amount including tax
    float total_with_tax = bill + (bill * tax / 100);
    
    // Calculate the total amount including tip
    float total_with_tip = total_with_tax + (total_with_tax * tip / 100);
    
    // Return half of the total amount
    return total_with_tip / 2;
}