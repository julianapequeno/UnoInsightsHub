## Digging deep into UNO - Data Analysis

For testing purposes, we are using some metrics to run the model. I will call the first test HANDS from now on.


<div align='center'>

### HANDS 

</div>
HANDS is a study about how the first 7 cards of a person's round can impact in the game's result. E.g., I would like to study if it really exists a 'good hand' and a 'bad hand' for the round. Accordingly with the UNO rules applied. 

The model is already ready to use. Before all of the analysis, I've done a statistics sanity test for evaluate if the results of the model can possibly be true. The following histogram showed up, confirming the good performance of the model. 
<div align='center'>
    <img src='documents\images\sanity_test.png' height='250' align='center'>
</div>
<br>
Therefore, we can apply the real test for checking if the player first has a impact in the result. How? Cheking std() and mean() of each result of simulations with randomic hands and comparing to one that had one fixed hand.  
<br>
- For instance, lets say you have...<br>

<br>

First of all, we can run a UNO ROUND with initial cards for each player. Each player has 7 cards, and I want to run a UNO round *n times*. For taking the winning probabilities out of this, it will be needed to run this simulation _n times_ with the same initial cards. As a result, we will have a winning probability:
```python
 >>> 0.256
 ```

obs. I'm observing 'Player 0' results for making this analysis.

Fine, now that we did this, and runned _n times_ what next? Now we will do what I will call RANDOMIC-TEST-DISTRIBUTION. The purpose here is to extract a normal distribution of these results with randomic initial hands. Then, we will have to run the same simulation that I've described before _m times_, each one of the _m times_ having its initial cards changed. Hence, we will have a list of winning probabilites, it will look like this:
```python
 >>> [0.256, 0.24, 0.235, 0.27...]
 ```

Last but not least, there's _w_. The last loop will have as a purpose repeat the same process a number of times, to guarantee the sampling taken in the study. Finally, we will have a matrix:
 ```python
 >>> [[0.256, 0.24, 0.235, 0.27...],
      [0.220, 0.2489, 0.25, 0.234...],
      [0.220,0.254, 0.213, 0.20...],
      ...]
 ```

Bellow, is some outputs of this study.

#### Outputs Relatory
- w = 10, m = 200, n = 500 <br><br>
<div align='center'>
<img src='documents\images\output_w10_m200_n500.png' align='center' height='300'>
</div>
<br>

**References**: Black Code Formatter [(ref)](https://github.com/psf/black) , <img align="center" alt="python" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"> <img align="center" alt="notebook" height="30" width="40" src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg">
<br>

_@2023.2_
