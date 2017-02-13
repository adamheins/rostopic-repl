# rostopic-repl
A tool for inspecting messages from ROS topics using the Python Read-Eval-Print
Loop (REPL).

## Usage
The tool can be used to interactively subscribe and publish messages to and
from ROS topics, respectively.

### Subscribe Mode
Subscribe mode is the default mode. Just run the following in your shell.

```
./rostopic-repl [topic]
```

where `topic` is the name of the topic to which you want to subscribe and
inspect messages.

The tool will run and wait for a message to arrive from the specified topic.
You should see the following:

```
Waiting for message from [topic]...
done.

>>>
```

You are now in the Python interactive interpreter. Your newly received message
is stored in the variable `msg`. You can now inspect and play with it using the
power of Python.

Here's simple example of inspecting some properties of an `Image` message:

```
./rostopic-repl /camera/rgb/image_raw
Waiting for message from /camera/rgb/image_raw...
done.

>>> type(msg)
<class 'sensor_msgs.msg._Image.Image'>
>>> msg.header
seq: 24
stamp:
  secs: 1486948936
  nsecs: 226464979
frame_id: camera_rgb_optical_frame
>>> msg.encoding
'rgb8'
>>> (msg.width, msg.height)
(640, 480)
>>> exit()
```

### Publish Mode
Publish mode is activated by passing the `-p` flag on the command line:

```
./rostopic-repl -p [topic]
```

Similarly to Subscribe mode, you should see something like:

```
Publishing to [topic]...

>>>
```

You're supplied with a `publish(msg)` function, which takes a message and
publishes it to the topic. Further, some of the more common message packages
are already imported for your use:
* `std_msgs.msg` as `std`
* `geometry_msgs.msg` as `geo`
* `sensor_msgs.msg` as `sensor`

Here's a simple example of the creation and publishing of a `Twist` message to
the topic `/my_robot/twist`:

```
./rostopic-repl -p /my_robot/twist
Publishing to /my_robot/twist...

>>> msg = geo.Twist()
>>> msg.linear.x = 10
>>> msg.angular.z = 2
>>> publish(msg)
>>> exit()
```

### Other Options
This tool supports using the [IPython](http://ipython.org/) interpreter instead
of the default Python one, if the user has IPython installed. Simply pass the
`-i` flag, like so:

```
./rostopic-repl -i [topic]
```
