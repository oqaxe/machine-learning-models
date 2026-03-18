// types.ts

enum Algorithm {
  LinearRegression,
  DecisionTree,
  RandomForest,
  SupportVectorMachine,
  NeuralNetwork
}

type ModelInput = {
  data: number[][];
  target: number[];
};

type ModelOutput = {
  model: {
    coefficients: number[];
    intercept: number;
  };
  metrics: {
    accuracy: number;
    meanSquaredError: number;
  };
};

type Hyperparameters = {
  algorithm: Algorithm;
  decisionTreeMaxDepth: number;
  randomForestN_estimators: number;
  supportVectorMachineKernel: string;
  neuralNetworkLayers: number[];
};