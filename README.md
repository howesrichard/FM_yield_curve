# FM Yield Curve: An OOP Teaching Repository

## Overview

This repository teaches object-oriented programming (OOP) principles to university-level finance students through the practical application of yield curve construction. By combining financial mathematics with software engineering concepts, students learn how to structure, organize, and implement code in a professional manner while working with real-world financial instruments.

## Learning Objectives

Students working through this repository will learn to:

1. **Understand OOP fundamentals**: Classes, objects, inheritance, encapsulation, and polymorphism
2. **Apply OOP to finance**: Model financial instruments (bonds, bank bills) as objects with attributes and behaviors
3. **Build complex systems**: Construct yield curves through bootstrapping techniques using portfolios of instruments
4. **Implement financial mathematics**: Work with zero rates, discount factors, and exponential interpolation
5. **Write maintainable code**: Organize code into reusable classes and modules following best practices

## Repository Structure

### Core Modules

- [instrument_classes.py](instrument_classes.py) - Defines classes for financial instruments:
  - `CashFlows`: Base class for managing cash flow streams
  - `Bank_bill`: Zero-coupon instruments with simple yield-to-maturity calculations
  - `Bond`: Coupon-bearing instruments with multiple cash flows
  - `Portfolio`: Container class for aggregating multiple instruments

- [curve_classes_and_functions.py](curve_classes_and_functions.py) - Implements yield curve functionality:
  - `ZeroCurve`: Stores and interpolates zero rates and discount factors
  - `YieldCurve`: Extends `ZeroCurve` to bootstrap curves from market instruments
  - `exp_interp()`: Exponential interpolation function for continuous compounding

### Educational Notebooks

#### Getting Started with OOP
- [object_oriented_programming/0_beginners_intro_to_OOP.ipynb](object_oriented_programming/0_beginners_intro_to_OOP.ipynb) - Introduction to OOP concepts using simple animal examples
- [object_oriented_programming/1_overview_of_FM_yield_curve_objects.ipynb](object_oriented_programming/1_overview_of_FM_yield_curve_objects.ipynb) - Overview of the financial classes in this repository
- [object_oriented_programming/2_OOP_Concepts_wrt_FM_yield_curve.ipynb](object_oriented_programming/2_OOP_Concepts_wrt_FM_yield_curve.ipynb) - OOP concepts applied to yield curve construction

#### Financial Mathematics Foundations
- [time_value_of_money/1_intro_to_compound_frequency.ipynb](time_value_of_money/1_intro_to_compound_frequency.ipynb) - Understanding compound interest and frequency conventions
- [time_value_of_money/2_time_weighted_averages.ipynb](time_value_of_money/2_time_weighted_averages.ipynb) - Computing time-weighted average rates
- [time_value_of_money/3_exponential_interpolation.ipynb](time_value_of_money/3_exponential_interpolation.ipynb) - Interpolation techniques for yield curves
- [time_value_of_money/4_discount_vs_atmat.ipynb](time_value_of_money/4_discount_vs_atmat.ipynb) - Relationship between discount factors and amounts at maturity

#### Working Notebooks
- [1_zero_curve_working.ipynb](1_zero_curve_working.ipynb) - Hands-on practice with the `ZeroCurve` class
- [2_instruments_working.ipynb](2_instruments_working.ipynb) - Creating and manipulating financial instruments
- [3_yield_curve_working.ipynb](3_yield_curve_working.ipynb) - Building yield curves through bootstrapping

#### Tutorial
- [tutorial/yield_curve_tutorial.ipynb](tutorial/yield_curve_tutorial.ipynb) - Guided exercise to create a Forward Bank Bill class using inheritance

## Getting Started

### Prerequisites

- Python 3.7+
- Jupyter Notebook or JupyterLab

### Installation

1. Clone this repository:
```bash
git clone https://github.com/howesrichard/FM_yield_curve.git
cd FM_yield_curve
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Launch Jupyter:
```bash
jupyter notebook
```

### Recommended Learning Path

1. **Start with OOP basics**: Begin with [0_beginners_intro_to_OOP.ipynb](object_oriented_programming/0_beginners_intro_to_OOP.ipynb) if you're new to OOP
2. **Learn financial foundations**: Work through the [time_value_of_money/](time_value_of_money/) notebooks to understand the mathematical concepts
3. **Explore the classes**: Review [1_overview_of_FM_yield_curve_objects.ipynb](object_oriented_programming/1_overview_of_FM_yield_curve_objects.ipynb) to see how OOP is applied to finance
4. **Practice with examples**: Work through the numbered working notebooks ([1_zero_curve_working.ipynb](1_zero_curve_working.ipynb), etc.)
5. **Apply your knowledge**: Complete the [tutorial](tutorial/yield_curve_tutorial.ipynb) to build your own Forward Bank Bill class

## Key Concepts Covered

### Object-Oriented Programming
- **Classes and Objects**: Blueprint vs. instance relationship
- **Inheritance**: Creating specialized classes from base classes (e.g., `Bond` inheriting from `CashFlows`)
- **Method Overriding**: Customizing behavior in child classes
- **Composition**: Building complex objects from simpler ones (e.g., `Portfolio` containing multiple instruments)

### Financial Engineering
- **Zero Coupon Bonds**: Pricing and yield calculations for bank bills
- **Coupon Bonds**: Managing multiple cash flows and payment frequencies
- **Yield Curve Construction**: Bootstrapping zero curves from market instruments
- **Discount Factors**: Present value calculations across different maturities
- **Interpolation**: Estimating rates for non-standard maturities using exponential interpolation

## Contributing

This is an educational repository. If you find errors or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by [howesrichard](https://github.com/howesrichard) for teaching object-oriented programming to finance students.