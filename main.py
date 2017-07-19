import tensorflow as tf
import gym
import numpy as np
from Qlearn import *
from gym import wrappers
from presentNN import genPic,save2Pic
import math

RENDER_ENV = False
ENV_NAME = 'CartPole-v0'
SAVE_PATH = './cartpole_q'
maxBuffSize = 10000
BATCH_SIZE = 64
SAVE_PER_STEP = 1000

OBSERVE = False
NN_PRESENT = True
OBSERVE_TIME = 0
FINAL_EPSILON = 0.0001 # final value of epsilon
INITIAL_EPSILON = 0.001 # starting value of epsilon
EXPLORE = 200000000
SUMMARY_DIR = './summary'
# Max training steps
MAX_EPISODES = 2000
# Max episode length
MAX_EP_STEPS = 1000
LEARNING_RATE = 0.001
# Discount factor
GAMMA = 0.99
# Soft target update param
TAU = 0.001
STEP = [0.1,0.1]
MAX_RANGE = 10
BASE_DIR_PIC = './picDir/'

def train(sess,env,network,high,low):
    rewardSummary = tf.Variable(0.0)
    maxQSummary = tf.Variable(0.0)
    tf.summary.scalar("Reward", rewardSummary)
    tf.summary.scalar("Maxium Q", maxQSummary)
    writer = tf.summary.FileWriter(SUMMARY_DIR, sess.graph)

    sess.run(tf.global_variables_initializer())
    network.initTarget()
    Buff = replayBuff(maxBuffSize)
    saver = tf.train.Saver()
    checkpoint = tf.train.get_checkpoint_state("savedQnetwork")
    epsilon = INITIAL_EPSILON
    t = 0
    if checkpoint and checkpoint.model_checkpoint_path:
        saver.restore(sess, checkpoint.model_checkpoint_path)
        print("Successfully loaded:", checkpoint.model_checkpoint_path)
    else:
        print("Could not find old network weights")
    for i in xrange(MAX_EPISODES):
    #i = 0
    #while True:
        s = env.reset()
        reward = 0
        maxQ = 0
        #i += 1
        for j in xrange(MAX_EP_STEPS):
            if RENDER_ENV:
                env.render()
            if random.random() <= epsilon:

            s = s2
            t += 1
            if t % SAVE_PER_STEP == 0:
                if NN_PRESENT:
                    ranges = []
                    for i in range(len(high)):
                        if high[i] >= MAX_RANGE:
                            high[i] = MAX_RANGE
                            low[i] = -MAX_RANGE
                        ranges.append([low[i],high[i]])
                    genPic(network,ranges,STEP,[1,3],MAX_RANGE,BASE_DIR_PIC,t,theta = 0)
                    genPic(network,ranges,STEP,[1,3],MAX_RANGE,BASE_DIR_PIC,t,theta = 10*2*math.pi/360)
                saver.save(sess, 'savedQnetwork/' + ENV_NAME + '-dqn', global_step = t)
            # print info
            state = ""
            if t <= OBSERVE_TIME:
                state = "observe"
            elif t > OBSERVE_TIME and t <= OBSERVE_TIME + EXPLORE:
                state = "explore"
            else:
                state = "train"
            print("TIMESTEP", t, "/ STATE", state, "/ EPSILON", epsilon, "/ ACTION", a, "/ REWARD", r, "/ Q_MAX %e" % np.max(q))
            #print(aIndex)
            #print(a)
            if d:
                print("break")
                break
        #print("run out of steps")
    print ("run out of episodes")
    env.close()
    print(t)
    #if NN_PRESENT:
        #save2Pic(BASE_DIR_PIC,t,SAVE_PER_STEP)

def main():
    env = gym.make(ENV_NAME)
    env = wrappers.Monitor(env, SAVE_PATH)
    sess = tf.InteractiveSession()
    sDim = env.observation_space.shape[0]
    aDim = env.action_space.n
    high = env.observation_space.high
    low = env.observation_space.low
    network = Qnetwork(sess,sDim,aDim,LEARNING_RATE,TAU)
    train(sess,env,network,high,low)

if __name__ == "__main__":
    main()
