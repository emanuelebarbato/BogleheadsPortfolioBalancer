def calculate_current_percentages(current_investments, total_invested):
    percentages = {fund: (amount / total_invested) * 100 for fund, amount in current_investments.items()}
    return percentages

def adjust_portfolio(current_investments, target_allocations):
    total_invested = sum(current_investments.values())
    adjusted_investments = {}

    for fund, target_alloc in target_allocations.items():
        target_amount = total_invested * target_alloc
        if current_investments[fund] < target_amount:
            adjusted_investments[fund] = target_amount - current_investments[fund]
        else:
            adjusted_investments[fund] = 0

    additional_total = sum(adjusted_investments.values())
    if additional_total > 0:
        for fund in adjusted_investments:
            adjusted_investments[fund] *= total_invested / (total_invested - additional_total)

    return adjusted_investments

def allocate_new_investment(new_investment, current_investments, target_allocations):
    total_invested = sum(current_investments.values()) + new_investment
    allocation = {}

    for fund, target_alloc in target_allocations.items():
        target_amount = total_invested * target_alloc
        allocation[fund] = max(target_amount - current_investments[fund], 0)

    total_allocated = sum(allocation.values())
    if total_allocated > new_investment:
        for fund in allocation:
            allocation[fund] *= new_investment / total_allocated

    return allocation

def main():
    target_allocations = {
        'global_stock_fund': 0.72,
        'small_cap_stocks_fund': 0.09,
        'emerging_markets_fund': 0.09,
        'government_bonds_fund': 0.10
    }

    current_investments = {}
    for fund in target_allocations.keys():
        current_investments[fund] = float(input(f"Enter the amount currently invested in {fund}: "))

    # Calculate the total amount invested
    total_invested = sum(current_investments.values())
    print(f"\nTotal amount currently invested: ${total_invested:.2f}")

    current_percentages = calculate_current_percentages(current_investments, total_invested)
    print("\nCurrent investment percentages:")
    for fund, percentage in current_percentages.items():
        print(f"{fund}: {percentage:.2f}%")

    adjustments_needed = adjust_portfolio(current_investments, target_allocations)
    print("\nAdjustments needed to achieve target allocation:")
    for fund, amount in adjustments_needed.items():
        print(f"{fund}: Increase by ${amount:.2f}")

    # Ask user if they want to calculate the allocation for a new investment
    proceed_with_new_investment = input("\nDo you want to calculate the allocation for a new addition of money? (yes/no): ").strip().lower()
    
    if proceed_with_new_investment == 'yes':
        new_investment = float(input("Enter the next investment amount: "))
        new_allocation = allocate_new_investment(new_investment, current_investments, target_allocations)
        print("\nAllocation of new investment:")
        for fund, amount in new_allocation.items():
            print(f"{fund}: ${amount:.2f}")

        # Calculate and display the total amount invested after the new allocation
        total_invested_after_new_allocation = total_invested + new_investment
        print("\nTotal amount invested after new allocation: ${:.2f}".format(total_invested_after_new_allocation))

        # Show the amount to add to each fund including the current investments
        for fund in target_allocations.keys():
            total_addition = current_investments[fund] + new_allocation[fund]
            print(f"{fund}: Total ${total_addition:.2f}")

    elif proceed_with_new_investment == 'no':
        print("No additional allocation will be calculated. Exiting the program.")
        return
    else:
        print("Invalid input. Please enter 'yes' or 'no'. Exiting the program.")
        return

if __name__ == "__main__":
    main()
