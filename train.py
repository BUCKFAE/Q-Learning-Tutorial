import random
import json
import argparse
import time

from Accountant import Accountant
from Drunkard import Drunkard
from DungeonSimulator import DungeonSimulator
from Gambler import Gambler


def main():
    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent', type=str, default='GAMBLER', help='Which agent to use')
    parser.add_argument('--learning_rate', type=float, default=0.1, help='How quickly the algorithm tries to learn')
    parser.add_argument('--discount', type=float, default=0.95, help='Discount for estimated future action')
    parser.add_argument('--iterations', type=int, default=2000, help='Iteration count')
    FLAGS, unparsed = parser.parse_known_args()

    # Informing the user
    print("Started the program with following parameters:")
    print("Agent:", FLAGS.agent)
    print("Learning Rate:", FLAGS.learning_rate)
    print("Discount:", FLAGS.discount)
    print("Iterations:", FLAGS.iterations)
    print()

# select agent
    if FLAGS.agent == 'GAMBLER':
        print("Training as Gambler!")
        agent = Gambler(learning_rate=FLAGS.learning_rate, discount=FLAGS.discount, iterations=FLAGS.iterations)
    elif FLAGS.agent == 'ACCOUNTANT':
        print("Training as Accountant")
        agent = Accountant()
    else:
        print("Training as Drunkard")
        agent = Drunkard()

    # setup simulation
    dungeon = DungeonSimulator()
    dungeon.reset()
    total_reward = 0 # Score keeping

    # main loop
    for step in range(FLAGS.iterations):
        old_state = dungeon.state # Store current state
        action = agent.get_next_action(old_state) # Query agent for the next action
        new_state, reward = dungeon.take_action(action) # Take action, get new state and reward
        agent.update(old_state, new_state, action, reward) # Let the agent update internals

        total_reward += reward  # Keep score
        if step % 250 == 0:  # Print out metadata every 100th iteration
            print(json.dumps({'step': step, 'total_reward': total_reward}))

        time.sleep(0.0001)  # Avoid spamming stdout too fast!

    print("Final Q-table", agent.q_table)


if __name__ == "__main__":
    main()

