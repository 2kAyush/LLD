package contracts

type SalaryDetails struct {
	Base float64
	HRA  float64
	LTA  float64
}

func GetSalaryDetails(base, hra, lta float64) *SalaryDetails {
	return &SalaryDetails{
		Base: base,
		HRA:  hra,
		LTA:  lta,
	}
}
