# https://github.com/jiaaro/pydub

from pydub import AudioSegment

files_path = ''
file_name = ''

startMin = 9
startSec = 50

endMin = 13
endSec = 30

# Time to miliseconds
startTime = startMin*60*1000+startSec*1000
endTime = endMin*60*1000+endSec*1000

# Opening file and extracting segment
song = AudioSegment.from_mp3( files_path+file_name+'.mp3' )
extract = song[startTime:endTime]

# Saving
extract.export( file_name+'-extract.mp3', format="mp3")