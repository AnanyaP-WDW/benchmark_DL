# benchmark_DL
Objectives:
1) Quantifying different approaches when coding deep neural networks from scratch using only NumPy.
2) Exploring and tinkering different directions in DL like curve smoothening, optimization etc.
3) Exploring PyTorch.
4) Having fun!

## Vectorization_sample 
Time difference (~50%) between vectorized vs iterated computation. Try running for different input shapes and plotting the rate of change of time difference WRT input size.

## Bias_correction_moving_average
Exponentially weighted averages (used in ADAM and RMSprop optimizers) to find approximate gradient values.
Run Bias_correction_moving_average.py
![Momentum for cureve smoothening](https://github.com/EpcLoler/benchmark_DL/blob/master/plot_momentum_2.png)

## visualize_MSE_loss
Forward propogation, loss calculation and gradient calculation.

