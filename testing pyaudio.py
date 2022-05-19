import pyaudio
import wave
import sys
import audioop
import numpy as np
import matplotlib.pyplot as plt
import struct

#[Description of chunks]
#imports - matplotlib is a library that allows to create graphs, wave allows us to work with wav files and to read and write with them. pyaudio is a library that helps to allow the program to tune to the proper hardware capabilites of the computer
#imports pt 2 - numpy is used in conjunction with arrays,they supposedly speed up the ability of python to use an array by 50x.
#imports pt 3 - audioop is used to calculate and manipulate audio fragment data coming from the audio file and the hardware
#import pt 4 - struct is used to convert python native data to binary and vice versa

#[Links]
#NumPy - https://numpy.org/doc/stable/user/absolute_beginners.html





# [Chunk]
#the number of frames that will be set in the buffer/waiting room. Before they are sent out to be played/outputed
#Correction - the number of samples that will be held in one chunk/portion. In this case we are holding 4096 samples in our chunk to be recorded/held to be played/outputed
chunk = 1024 * 4


#[File variable]
#this allows us to open the audio file(wav file) and store it in a variable
#rb is the command working in "read" mode in which they interpret the code
#the information before it is the directory to find the music
#Remember you \\ example 'C:\\Visual Equaliter\\Visual-Equalizer\\fukashigi no carte (kosu remix).wav'
wf = wave.open ( 'C:\\Users\\danie\\Documents\\Github\\Visual-Equalizer\\fukashigi no carte (kosu remix).wav' , 'rb')


#[Portaudio system]
#p is instantiating "pyaudio to use as a portaudio system(allows it to be used on computer platforms)
#port audio is an API used to tune the program towards the platform and the device's audio capabilties
p = pyaudio.PyAudio()


#[Streaming]
#streams work by sending packets/portions of data, and then interpreting and building the data in audio in which then it can play as sound and a portion of the audio file. The packets must be built/pre-established for those incoming portions before playing. It will be queued in a buffer if it can establsih the data quicker than it can output it

#in this command we are using pyaudio to manipulate the data from our wave variable
#the Get format method helps to configure the algorithm by tuning itself to the audio hardware of a device, with the device's capabilities of supported sample rates and the number of supported input and output channels.(the channels are dependent on the ports/cables plugged in to direct data into or out of the device/computer)
#Channels are the routes which audio travel to a point. ex stereo has two channels due to two paths of audio
#samplewidth is the number of bits within a sample/portion of the song (Pyaudio uses a fixed number of bits in order to tell where the data starts and ends)
#The rate is how many frames are being played per second, frames are samples but with additional information such as volume or the combining information of all channels at that particular portion/time of the audio file. For example if there are two channels that need to be played, then the frame will have 2 sets of samples instead of 1 for 1 channel
#output command tells the program that this information is going to be sent out rather than inputed

#I think it is typed, in order to setup the format, we haven't fully established it to interpet data, only to set it up to find specific working conditions
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True,
                frames_per_buffer = chunk
                )


#[Reading data]
#In this command I believe we are now trying to interpret the audio of the frames with in the packages/chunks 

data = wf.readframes(chunk)
#rms = audioop.rms(data,2)


#[Length]
#measures the length/size of data 
#our song got the number of bits working in the file sample, in this example we have 8 bits in our samples
format = p.get_format_from_width(wf.getsampwidth())
print(format)
print(len(data))



#[Graph section]
#To create our graph we require native python data instead of binary data, at least for me to understand. Most of the data in our python code is binary since that is the data being given to the computer to understand on its own computational level.
# some of the imports/libraries in python 3.x work in bytes, so struct comes handy in this situation

#struct is unpacking binary data into str and we inserted a certain amount of code, in this case we inserted the entirety of the audio file which is 4 chunks long.
#According to the website, 'struct.unpack' takes two arguments of the format or desired format and the buffer (holding place)
#in our case, the format we want from unpacking is a string that is the length of 4 chunks/16384 samples. 
# 'b' = bytes in this case, i think we are telling the command that this data is in bytes.
# dtype also tells the program the type of element/data is used in our array
#And our buffer is located in data
#//data_int = np.array(struct.unpack(str(4*chunk) + 'B', data), dtype ='b' )

#the result should provide a tuple.
# a tuple is just combining all the information/elements in the conversion around parentheses
#print(data_int)

#Creating graph object
#plt is matploblib but shortened as shown at the top of the file
#subplotts is a method used to create plots with parameters of rows and columms, and an id/number associated with the graph
#fig helps to tell the program that we creating a template, and then the ax tells the program that we are creating a square/cell, in which the subplots are there to create the x and y axis
fig, ax = plt.subplots()



#Creating an animated graph
#Instead of creating a new graph everytime, we will try to update the lines/data itself in the graph instead.
#NumPy/np is there to create an array 
#the method arange is used to tell the array how long the array should be, or the range in this case
#This arange() method is used to create an array that holds specific conditions
#The first number indicate where it starts, so at 0 
#The second number indicates where the last number is which is 8 chunks long
# and the third tells the array how many steps/numbers each element in the array is increased by in intervals, but i deleted it since we dont need them in intervals

x = np.arange(0, 4 * chunk)
line, = ax.plot(x , np.random.rand(4 * chunk) )
ax.set_ylim(0,255)
ax.set_xlim(0,chunk)

while True:
    for x in range(4):
        data_1 = stream.read(chunk)
        data_int = np.array(struct.unpack(str(4 * chunk) + 'B', data_1) , dtype ='b' )
        line.set_ydata(data_int)
        fig.canvas.draw()
        fig.canvas.flush_events()




#[play stream]
#now we play the audio 

#the stream was already formated before hand, and is set there before any of the data can be written/interpreted. The stream is established first, then the audio is interpreted from file to samples and frames, then written out and being outputed as sound. 
#I assume since it starts the argument with "as long as the variable contains data or is not empty" it will continue to write and read/play the frames until there is no data left

    #while data != '':
        #stream.write(data)
        #data = wf.readframes(chunk)


#[volume]
#now how do we manipulate the volume?
#it most likely I assume would have to involve the frames, as they contain additional data outside the file's core audio data.
#however from researching it is based on manipulating the power/voltage that is being sent in the system
#a command that can help measure power is RMS









