package main

import (
	"fmt"
	"simple_factory/algorithm"
	"simple_factory/contracts"
)

func main() {
	fmt.Println("Tax Factory implementation")
	salary_details := contracts.GetSalaryDetails(15, 4, 1)
	old_regime_calc, err := algorithm.GetTaxAlgorithm("OLD")
	if err != nil {
		fmt.Println(err)
		return
	}

	new_regime_calc, err := algorithm.GetTaxAlgorithm("NEW")
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("Tax for Old regime: ", old_regime_calc.CalculateTax(salary_details))
	fmt.Println("Tax for New regime: ", new_regime_calc.CalculateTax(salary_details))
}
