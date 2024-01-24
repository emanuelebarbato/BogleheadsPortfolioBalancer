# LazyPortfolioBalancer
A Python tool for Bogleheads and lazy investors to manage and balance their investment portfolios, ensuring alignment with their preferred low-cost, diversified index fund strategies. Ideal for maintaining targeted asset allocations in line with long-term investment principles.

## Overview
This Python script is designed to assist investors in managing their stock portfolio allocation. It helps maintain a desired distribution of investments across various funds, based on a predefined allocation strategy. The script is particularly useful for those following a mixed investment approach with a combination of variable and fixed investments.

## Features
- **Current Portfolio Analysis**: Calculates the current percentage allocation of investments in different funds based on the total invested amount.
- **Adjustment Calculation**: Determines the additional amount required to invest in each fund to achieve the target allocation, without reducing any existing over-allocated funds.
- **New Investment Allocation**: For a new sum to be invested, it provides a detailed allocation to each fund to maintain or reach the desired investment distribution.

## How to Use
1. **Input Current Investments**: The script prompts for the amount currently invested in each fund.
2. **View Current Allocation**: Displays the percentage of the total investment in each fund.
3. **Adjust Portfolio**: Calculates and suggests adjustments needed to align with the target allocation.
4. **Allocate New Investment**: Optionally, enter a new investment amount to find out how it should be distributed across the funds to meet the allocation goals.

## Customization
The script is flexible and can be adapted to different investment strategies by modifying the `target_allocations` dictionary. This allows users to set their desired allocation percentages for each fund.

### Example
If you follow a 4 fund 60/10/10/20 allocation strategy, you can modify the `target_allocations` as follows:
```python
target_allocations = {
    'global_stock_fund': 0.60,
    'small_cap_stocks_fund': 0.10,
    'emerging_markets_fund': 0.10,
    'bonds_fund': 0.20
}
```
Adjust the keys and values in this dictionary according to your investment strategy and portfolio composition.

## Requirements

Python 3.x

## Running the Script

Simply run the script in a Python environment and follow the on-screen prompts to input your investment details.

```bash
python portfolio_allocation.py
```
## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## License

[MIT](https://github.com/emanuelebarbato/LazyPortfolioBalancer/blob/main/LICENSE)

