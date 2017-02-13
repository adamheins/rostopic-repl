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

You are now in the Python interactive interpreter. You're newly received
message is stored in the variable `msg`. You can now inspect and play with it
using the power of Python.

Here's simple example of inspecting some properties of an Image message:

```
./rostopic-repl /camera/rgb/image_raw
Waiting for message from [topic]...
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


### Options
This tool supports using [IPython](http://ipython.org/) if the user has it
installed. Simply pass the `-i` flag, like so:

```
./rostopic-repl -i [topic]
```
