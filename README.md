# benchmark_DL
Objectives:
1) Quantifying different approaches when coding deep neural networks from scratch using numpy.
2) Exploring and tinkering with different directions in DL like curve smoothening, optimization etc.
3) Exploring PyTorch.
4) Having fun !
## Vectorization_sample 
Exploring the time difference (~50%) between vectorized vs iterated computation. Try running for differnt input shapes and plottingt the rate of change of time difference WRT input size.
Run Vectorization_sample.py for the base code template

## Bias_correction_moving_average
Using exponential weighted averages (used in ADAM and RMSprop optimizers) to find approximate gradient values.
![Momentum for cureve smoothening](https://github.com/EpcLoler/benchmark_DL/blob/master/plot_momentum_2.png)
