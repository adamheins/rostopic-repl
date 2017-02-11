from __future__ import print_function

import argparse
import code
import importlib
import sys

import rospy
import rostopic


def subscribe(topic):
    ''' Subscribe mode. REPL for receiving messages from a topic. '''

    def more(num=1):
        ''' Request more messages from the topic. '''
        if num < 1:
            return None

        s = 's' if num > 1 else ''
        print('Waiting for message{} from {}...'.format(s, topic))

        msg_class, _, _ = rostopic.get_topic_class(topic)
        num_rec = 0
        msgs = []

        # Wait for the desired number of messages to come in.
        while num_rec < num:
            try:
                msg = rospy.wait_for_message(topic, msg_class)
                msgs.append(msg)
                num_rec += 1
            except rospy.ROSInterruptException:
                print('canceled.')
                return msgs

        print('done.')
        if num == 1:
            return msgs[0]
        else:
            return msgs

    def help():
        print('Not yet implemented.')

    msg = more()
    code.interact(local=locals(), banner='')


def publish(topic):
    ''' Publish mode. REPL for publishing to a topic. '''
    topic_class, _, _ = rostopic.get_topic_class(topic)
    publisher = rospy.Publisher(topic, topic_class, queue_size=1)

    # Import some common messages for the user's convenience.
    std = importlib.import_module('std_msgs.msg')
    geo = importlib.import_module('geometry_msgs.msg')
    sensor = importlib.import_module('sensor_msgs.msg')

    def pub(msg):
        ''' Convenient short-form for publisher.publish(msg). '''
        publisher.publish(msg)

    def help():
        print('Not yet implemented.')

    print('Publishing to {}...'.format(topic))

    code.interact(local=locals(), banner='')


def main():
    rospy.init_node('repl_node', anonymous=True)

    parser = argparse.ArgumentParser()
    parser.add_argument('topic', help='Name of the topic to interact with.')
    parser.add_argument('-p', '--publish', help='Publish mode.', action='store_true')
    args = parser.parse_args()

    topic = args.topic
    if args.publish:
        publish(topic)
    else:
        subscribe(topic)


if __name__ == '__main__':
    main()
