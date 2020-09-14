import numpy as np
from pydub import AudioSegment
import glob
import os
files = glob.glob('*.flac')
for f in files:
    audio = AudioSegment.from_file(f,'flac').export(f.split('-')[-1].replace('flac','wav'), format="wav")
    del audio