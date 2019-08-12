![alt text](https://miro.medium.com/max/640/0*AaKD-VocK5nHixGz.PNG)
# Copula
A python library for sampling and generating new Data points by multivariate Gaussian copulas.
## Overview
A python libray to build multivariate gaussian copula for given data points and sample arbitary number of new data points from input data distribution. In short *given some input data points, it can generate more  such data points which follow the input data distribution*

## Installation
Install using pip
```
pip install copula
```

## Usage

If you have some data points and distribution of this multivariate data points is not explicitly given. Then this library can be used to sample new points from this dritribution.
*gendata()* funtion number of new samples to be generated as input
```python
>>>from copula import pyCopula
>>>data = [[2,1,2,4],[3,1,7,4],[2,9,1,0],[3,6,1,6] ]
>>>cop = pyCopula.Copula(data)
>>>samples = cop.gendata(3)
>>>print(samples)
[2.697128268374179, 6.29726013955287, 2.983951810593502, 2.1149729235834496], [3.0, 1.0, 6.831369733333171, 4.631091408593663], [2.147377031275032, 6.75098812552581, 1.9789800708813163, 1.1200891337867478]]
```

## Assumptions
data provided to copula must be a 2D numeric array

Data must be clean (no null values)

Every row of input data must contain same number of columns
