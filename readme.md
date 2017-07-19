# A Q-learning version of CartPole

A naive Q-learning implement of Q-learning with memory replay and soft target network using tensorflow and gym.

Here's some gif to show the process:

![alt text](https://github.com/li012589/Cartpole-Q/blob/master/demo/Qlearning.gif "Train process")
![alt text](https://github.com/li012589/Cartpole-Q/blob/master/demo/combine_theta0-compressed.gif "View the output of the Q network")

## HOW TO RUN

```
python ./main.py
```
It will take few hours to balance the pole.
## DEMO
1. Move the files in demo to the savedQnetwork folders 
2. Change "RENDER_ENV" to "True" in main.py
3. Run the main.py

## TO BE MORE SPECIFIC
In the main:
1. RENDER_ENV controls if render gym's output or not
2. NN_PRESENT controls if save Q network's value(will take more time), then modify revealPic.py and run it to output pictures of these value and modify animation.py to out gif version.


