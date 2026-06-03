package algorithm

import (
	"errors"
	"fmt"
	"simple_factory/contracts"
)

type Algorithm interface {
	CalculateTax(salary_details *contracts.SalaryDetails) float64
}

func GetTaxAlgorithm(regime string) (Algorithm, error) {
	switch regime {
	case "OLD":
		return &OldTaxAlgorithm{}, nil
	case "NEW":
		return &NewTaxAlgorithm{}, nil
	}
	return nil, errors.New(fmt.Sprintf("Invalid regime provided %s; supported types OLD, NEW", regime))
}
