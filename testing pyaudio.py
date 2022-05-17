import pyaudio
import wave
import sys
import audioop
import numpy as np
import matplotlib
import struct

#[Description of chunks]
#imports - matplotlib is a library that allows to create graphs, wave allows us to work with wav files and to read and write with them. pyaudio is a library that helps to allow the program to tune to the proper hardware capabilites of the computer
#imports pt 2 - numpy is used in conjunction with arrays,they supposedly speed up the ability of python to use an array by 50x.
#imports pt 3 - audioop is used to calculate and manipulate audio fragment data coming from the audio file and the hardware
#import pt 4 - struct is used to convert python native data to binary and vice versa


# [Chunk]
#the number of frames that will be set in the buffer/waiting room. Before they are sent out to be played/outputed
#Correction - the number of samples that will be held in one chunk/portion. In this case we are holding 4096 samples in our chunk to be recorded/held to be played/outputed
chunk = 1024 * 4


#[File variable]
#this allows us to open the audio file(wav file) and store it in a variable
#rb is the command working in "read" mode in which they interpret the code
#the information before it is the directory to find the music
#Remember you \\ example 'C:\\Visual Equaliter\\Visual-Equalizer\\fukashigi no carte (kosu remix).wav'
wf = wave.open ( 'put your path here' , 'rb')


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
                output = True)


#[Reading data]
#In this command I believe we are now trying to interpret the audio of the frames with in the packages/chunks 

data = wf.readframes(chunk)
rms = audioop.rms(data,2)


#[Length]
#measures the length/size of data 
#our song got the number of bits working in the file sample, in this example we have 8 bits in our samples
format = p.get_format_from_width(wf.getsampwidth())
print(format)
print(len(data))


#[play stream]
#now we play the audio 

#the stream was already formated before hand, and is set there before any of the data can be written/interpreted. The stream is established first, then the audio is interpreted from file to samples and frames, then written out and being outputed as sound. 
#I assume since it starts the argument with "as long as the variable contains data or is not empty" it will continue to write and read/play the frames

while data != '':
    stream.write(data)
    data = wf.readframes(chunk)

#[volume]
#now how do we manipulate the volume?
#it most likely I assume would have to involve the frames, as they contain additional data outside the file's core audio data.
#however from researching it is based on manipulating the power/voltage that is being sent in the system
#a command that can help measure power is RMS


#[Graph section]
#To create our graph we require native python data instead of binary data, at least for me to understand. Most of the data in our python code is binary since that is the data being given to the computer to understand on its own computational level.
# some of the imports/libraries in python 3.x work in bytes, so struct comes handy in this situation

#struct is unpacking binary data into str and we inserted a certain amount of code, in this case we inserted the entirety of the audio file which is 4 chunks long.
data_int = struct.unpack(str(4*chunk))

# p.stream.close()






