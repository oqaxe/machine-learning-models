package machine_learning_models

import (
	"fmt"
)

// calculateMean calculates the mean of a slice of numbers.
func calculateMean(numbers []float64) (float64, error) {
	if len(numbers) == 0 {
		return 0, fmt.Errorf("Cannot calculate mean of an empty slice")
	}

	var sum float64
	for _, num := range numbers {
		sum += num
	}

	return sum / float64(len(numbers)), nil
}

// calculateStandardDeviation calculates the standard deviation of a slice of numbers.
func calculateStandardDeviation(numbers []float64, mean float64) (float64, error) {
	if len(numbers) == 0 {
		return 0, fmt.Errorf("Cannot calculate standard deviation of an empty slice")
	}

	var sumOfSquaredDifferences float64
	for _, num := range numbers {
		sumOfSquaredDifferences += (num - mean) * (num - mean)
	}

	return math.Sqrt(sumOfSquaredDifferences / float64(len(numbers))), nil
}

// calculateVariance calculates the variance of a slice of numbers.
func calculateVariance(numbers []float64, mean float64) (float64, error) {
	var sumOfSquaredDifferences float64
	for _, num := range numbers {
		sumOfSquaredDifferences += (num - mean) * (num - mean)
	}

	return sumOfSquaredDifferences / float64(len(numbers)), nil
}