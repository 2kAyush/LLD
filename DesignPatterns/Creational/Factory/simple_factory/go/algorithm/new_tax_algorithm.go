package algorithm

import (
	"fmt"
	"simple_factory/contracts"
)

type NewTaxAlgorithm struct {
}

func (ot *NewTaxAlgorithm) CalculateTax(salary_details *contracts.SalaryDetails) float64 {
	fmt.Println("salary_details: ", salary_details)
	return 2.5*salary_details.Base + 3.3*salary_details.HRA + 3.9*salary_details.LTA
}
