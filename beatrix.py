"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
BEATRIX: A rhythmic drum beat sequencer.
Author:
    - Tanisha Madhusudhan : tm3805@nyu.edu
    - Shubham Shandilya   : ss15590@nyu.edu

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#########################################################
# Required Libraries: 
# Use python3 -m pip install requirements.txt

import pygame
import pyaudio
from scipy.fftpack import fft
from scipy import signal as sig
from pygame import mixer
from pygame.locals import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import os
import roomImpulse

#########################################################
# Initialize the pygame library
pygame.init()

# Compute the convolution between the beat sounds and the room impulse
roomImpulse.convolve()

#########################################################
# COLOUR PALETTE
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
GRAY        = (128, 128, 128)
DARK_GRAY   = (50, 50, 50)
LIGHT_GRAY  = (170, 170, 170)
GOLD        = (212, 175, 55)


blue        = [(92, 174, 190), (4, 191, 191), (0, 171, 216), (14, 234, 255)]
red         = [(246, 38, 49), (205, 8, 19), (137, 5, 13), (185, 18, 27)]
green       = [(126, 182, 60), (98, 141, 47), (190, 219, 57), (150, 202, 45)]
orange      = [(255, 97, 56), (210, 54, 0), (250, 91, 15), (255, 109, 31)]
purple      = [(66, 15, 141), (107, 20, 166), (81, 45, 168), (76, 18, 115)]
yellow      = [(255, 190, 0), (255, 225, 26), (255, 211, 78), (255, 238, 88)]

# Dimensions of the pygameGUI
WIDTH       = 1400
HEIGHT      = 800

#########################################################
# Sound to be used 
hi_hat  = {'original': mixer.Sound('sounds\hi hat.wav'), 'auditorium': mixer.Sound('IR\convolved\hi hat\hi hat_auditorium.wav'), 'hall': mixer.Sound('IR\convolved\hi hat\hi hat_hall.wav'), 'church': mixer.Sound('IR\convolved\hi hat\hi hat_church.wav'), 'summer_park': mixer.Sound('IR\convolved\hi hat\hi hat_summer_park.wav'), 'stairway': mixer.Sound('IR\convolved\hi hat\hi hat_stairway.wav'), 'factory': mixer.Sound('IR\convolved\hi hat\hi hat_factory.wav'),
            'dungeon': mixer.Sound('IR\convolved\hi hat\hi hat_dungeon.wav'), 'kiln': mixer.Sound('IR\convolved\hi hat\hi hat_kiln.wav'), 'tunnel': mixer.Sound('IR\convolved\hi hat\hi hat_tunnel.wav'), 'winter_park': mixer.Sound('IR\convolved\hi hat\hi hat_winter_park.wav'), 'studio': mixer.Sound('IR\convolved\hi hat\hi hat_studio.wav'), 'chamber': mixer.Sound('IR\convolved\hi hat\hi hat_chamber.wav')}

snare   = {'original': mixer.Sound('sounds\snare.wav'), 'auditorium': mixer.Sound('IR\convolved\snare\snare_auditorium.wav'), 'hall': mixer.Sound('IR\convolved\snare\snare_hall.wav'), 'church': mixer.Sound('IR\convolved\snare\snare_church.wav'), 'summer_park': mixer.Sound('IR\convolved\snare\snare_summer_park.wav'), 'stairway': mixer.Sound('IR\convolved\snare\snare_stairway.wav'), 'factory': mixer.Sound('IR\convolved\snare\snare_factory.wav'),
            'dungeon': mixer.Sound('IR\convolved\snare\snare_dungeon.wav'), 'kiln': mixer.Sound('IR\convolved\snare\snare_kiln.wav'), 'tunnel': mixer.Sound('IR\convolved\snare\snare_tunnel.wav'), 'winter_park': mixer.Sound('IR\convolved\snare\snare_winter_park.wav'), 'studio': mixer.Sound('IR\convolved\snare\snare_studio.wav'), 'chamber': mixer.Sound('IR\convolved\snare\snare_chamber.wav')}

kick    = {'original': mixer.Sound('sounds\kick.wav'), 'auditorium': mixer.Sound('IR\convolved\kick\kick_auditorium.wav'), 'hall': mixer.Sound('IR\convolved\kick\kick_hall.wav'), 'church': mixer.Sound('IR\convolved\kick\kick_church.wav'), 'summer_park': mixer.Sound('IR\convolved\kick\kick_summer_park.wav'), 'stairway': mixer.Sound('IR\convolved\kick\kick_stairway.wav'), 'factory': mixer.Sound('IR\convolved\kick\kick_factory.wav'),
            'dungeon': mixer.Sound('IR\convolved\kick\kick_dungeon.wav'), 'kiln': mixer.Sound('IR\convolved\kick\kick_kiln.wav'), 'tunnel': mixer.Sound('IR\convolved\kick\kick_tunnel.wav'), 'winter_park': mixer.Sound('IR\convolved\kick\kick_winter_park.wav'), 'studio': mixer.Sound('IR\convolved\kick\kick_studio.wav'), 'chamber': mixer.Sound('IR\convolved\kick\kick_chamber.wav')}

crash   = {'original': mixer.Sound('sounds\crash.wav'), 'auditorium': mixer.Sound('IR\convolved\crash\crash_auditorium.wav'), 'hall': mixer.Sound('IR\convolved\crash\crash_hall.wav'), 'church': mixer.Sound('IR\convolved\crash\crash_church.wav'), 'summer_park': mixer.Sound('IR\convolved\crash\crash_summer_park.wav'), 'stairway': mixer.Sound('IR\convolved\crash\crash_stairway.wav'), 'factory': mixer.Sound('IR\convolved\crash\crash_factory.wav'),
            'dungeon': mixer.Sound('IR\convolved\crash\crash_dungeon.wav'), 'kiln': mixer.Sound('IR\convolved\crash\crash_kiln.wav'), 'tunnel': mixer.Sound('IR\convolved\crash\crash_tunnel.wav'), 'winter_park': mixer.Sound('IR\convolved\crash\crash_winter_park.wav'), 'studio': mixer.Sound('IR\convolved\crash\crash_studio.wav'), 'chamber': mixer.Sound('IR\convolved\crash\crash_chamber.wav')}

clap    = {'original': mixer.Sound('sounds\clap.wav'), 'auditorium': mixer.Sound('IR\convolved\clap\clap_auditorium.wav'), 'hall': mixer.Sound('IR\convolved\clap\clap_hall.wav'), 'church': mixer.Sound('IR\convolved\clap\clap_church.wav'), 'summer_park': mixer.Sound('IR\convolved\clap\clap_summer_park.wav'), 'stairway': mixer.Sound('IR\convolved\clap\clap_stairway.wav'), 'factory': mixer.Sound('IR\convolved\clap\clap_factory.wav'),
            'dungeon': mixer.Sound('IR\convolved\clap\clap_dungeon.wav'), 'kiln': mixer.Sound('IR\convolved\clap\clap_kiln.wav'), 'tunnel': mixer.Sound('IR\convolved\clap\clap_tunnel.wav'), 'winter_park': mixer.Sound('IR\convolved\clap\clap_winter_park.wav'), 'studio': mixer.Sound('IR\convolved\clap\clap_studio.wav'), 'chamber': mixer.Sound('IR\convolved\clap\clap_chamber.wav')}
            
tom     = {'original': mixer.Sound('sounds\\tom.wav'), 'auditorium': mixer.Sound('IR\convolved\\tom\\tom_auditorium.wav'), 'hall': mixer.Sound('IR\convolved\\tom\\tom_hall.wav'), 'church': mixer.Sound('IR\convolved\\tom\\tom_church.wav'), 'summer_park': mixer.Sound('IR\convolved\\tom\\tom_summer_park.wav'), 'stairway': mixer.Sound('IR\convolved\\tom\\tom_stairway.wav'), 'factory': mixer.Sound('IR\convolved\\tom\\tom_factory.wav'),
            'dungeon': mixer.Sound('IR\convolved\\tom\\tom_dungeon.wav'), 'kiln': mixer.Sound('IR\convolved\\tom\\tom_kiln.wav'), 'tunnel': mixer.Sound('IR\convolved\\tom\\tom_tunnel.wav'), 'winter_park': mixer.Sound('IR\convolved\\tom\\tom_winter_park.wav'), 'studio': mixer.Sound('IR\convolved\\tom\\tom_studio.wav'), 'chamber': mixer.Sound('IR\convolved\\tom\\tom_chamber.wav')}

# sets the display where pygame will open its window or screen. 
screen  = pygame.display.set_mode([WIDTH, HEIGHT])

# Set the Caption
pygame.display.set_caption('BEATRIX')

# Define the fonts
label_font  = pygame.font.Font('Roboto-Bold.ttf', 24)
medium_font = pygame.font.Font('Roboto-Bold.ttf', 16)

# Global variables
active_length   = 0                     # Active length of the beat grid
active_beat     = 0                     # Active grid
beat_changed    = True                  # Beat changed
timer           = pygame.time.Clock()   # Create a clock to control the frame rate
fps             = 60                    # Frames per seconds 
beats           = 8                     # Defaut beats
bpm             = 240                   # Default beats per minute
playing         = False                 # Default state of play/paused
room            = 'original'            # Default state of the room : Original
left_vol        = 1.0                   # Default volume of left speakers
right_vol       = 1.0                   # Default volume of right speakers

# Defaut instruments with colour codes
instruments     = [purple[0], blue[0], green[0], yellow[0], orange[0], red[0]]

# Directory of the grid boxes being clicked
clicked = [[-1 for _ in range(beats)] for _ in range(len(instruments))]

# List of active instruments
active_list = [1 for _ in range(len(instruments))]

# set the total number of playback channels
pygame.mixer.set_num_channels(len(instruments) * 3)

# GUI Controls
save_menu   = False         # Control to save the playback thus created.
load_menu   = False         # Control to load the saved playback

# File to store the saved playbacks and its corresponding parameters
saved_beats = []            # List of saved beats
file = open('saved_beats.txt', 'r')

# Read the lines from the file
for line in file:
    saved_beats.append(line)

beat_name   = ''            # Load the saved beat_name or save a new one.
typing      = False         # Whether typing or not
index       = 100           # Total number of beat tha can be saved
rotation    = -1            # Grid rotation

######################################################################################################
# Function to design the GUI Layout
######################################################################################################

def draw_grid(clicks, beat, actives):

    global rotation, instruments

    rotation = rotation + 1
    
    #########################################################
    # Rotate the colour of the beats
    instruments = [purple[(rotation//20) % 4], blue[(rotation//20) % 4], green[(rotation//20) % 4], yellow[(rotation//20) % 4], orange[(rotation//20) % 4], red[(rotation//20) % 4]]
    
    # Beat boxes
    boxes = []

    # Left BEAT-box GUI layout
    for i in range(len(instruments)):
        if actives[i] == 1:
            color = instruments[i]
        else:
            color = DARK_GRAY

        left_box    = pygame.draw.rect(screen, color, [0, 100 + i * 50, 100, 50], 0, 3)
        pygame.draw.rect(screen, WHITE, [0, 100 + i * 50, 100, 50], 5, 5)
        pygame.draw.rect(screen, BLACK, [0, 100 + i * 50, 100, 50], 2, 5)

    # Top Control GUI layout
    top_box     = pygame.draw.rect(screen, DARK_GRAY, [0, 0, WIDTH, 100])   

    # Bottom Control GUI layout             
    bottom_box  = pygame.draw.rect(screen, BLACK, [0, 400, WIDTH, 400])

    # Colour pallette for BEAT text: denoting the active
    colors = [GRAY, WHITE, GRAY]

    # Create the text renderer and place the surface onto the Screen at given coordinates
    hi_hat_text = medium_font.render('Hi Hat', True, colors[actives[0]])
    screen.blit(hi_hat_text, (15, 115))
    
    snare_text = medium_font.render('Snare', True, colors[actives[1]])
    screen.blit(snare_text, (15, 165))
    
    kick_text = medium_font.render('Bass Drum', True, colors[actives[2]])
    screen.blit(kick_text, (15, 215))
    
    crash_text = medium_font.render('Crash', True, colors[actives[3]])
    screen.blit(crash_text, (15, 265))
    
    clap_text = medium_font.render('Clap', True, colors[actives[4]])
    screen.blit(clap_text, (15, 315))
    
    tom_text = medium_font.render('Floor Tom', True, colors[actives[5]])
    screen.blit(tom_text, (15, 365))
    
    # Activate the BEAT-boxes when clicked
    for i in range(beats):
        for j in range(len(instruments)):
            if clicks[j][i] == -1:
                color = GRAY
            else:
                if actives[j] == 1:
                    color = instruments[j]
                else:
                    color = DARK_GRAY

            rect = pygame.draw.rect(screen, color, [i * ((WIDTH - 100) // beats) + 105, (j * 50) + 105, ((WIDTH - 100) // beats) - 5, 45], 0, 3)
            pygame.draw.rect(screen, WHITE, [i * ((WIDTH - 100) // beats) + 100, j * 50 + 100, ((WIDTH - 100) // beats), 50], 5, 5)
            pygame.draw.rect(screen, BLACK,[i * ((WIDTH - 100) // beats) + 100, j * 50 + 100, ((WIDTH - 100) // beats), 50], 2, 5)
            boxes.append((rect, (i, j)))

    # Create the ACTIVE Grid rectangle with GOLD
    active = pygame.draw.rect(screen, GOLD, [beat * ((WIDTH - 100) // beats) + 100, 100, ((WIDTH - 100) // beats), len(instruments) * 50], 5, 3)
    
    return boxes

######################################################################################################
# Function to select the notes within the corresponding room to be played
######################################################################################################

def play_notes(room):

    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1 and active_list[i] == 1:
            
            # Stop the playback if it's overlapping with one to be played next
            snare[room].stop()
            kick[room].stop()
            crash[room].stop()
            clap[room].stop()
            tom[room].stop()
            hi_hat[room].stop()

            # Play the BEAT sound under the influence of the selected ROOM 
            if i == 0:
                channel = hi_hat[room].play()
            if i == 1:
                channel = snare[room].play()
            if i == 2:
                channel = kick[room].play()
            if i == 3:
                channel = crash[room].play()
            if i == 4:
                channel = clap[room].play()
            if i == 5:
                channel = tom[room].play()
            
            # Set the Volume of the Speakers to chosen amount
            channel.set_volume(left_vol, right_vol)

######################################################################################################
# Function to define the 'SAVE' GUI Screen 
######################################################################################################

def draw_save_menu(beat_name, typing):

    # Draw a rectangle for entering the beat_name
    pygame.draw.rect(screen, BLACK, [0, 0, WIDTH, HEIGHT])
    menu_text = label_font.render('SAVE MENU: Enter a Name for this beat', True, WHITE)
    screen.blit(menu_text, (400, 40))
    
    # Draw a rectangle for close button
    exit_btn = pygame.draw.rect(screen, GRAY, [WIDTH - 200, HEIGHT - 100, 180, 90], 0, 5)
    exit_text = label_font.render('Close', True, WHITE)
    screen.blit(exit_text, (WIDTH - 160, HEIGHT - 70))
    
    # Draw a rectangle for saving the beat-mix and its corresponding parameters under the given name
    saving_btn = pygame.draw.rect(screen, GRAY, [WIDTH // 2 - 100, HEIGHT * 0.75, 200, 100], 0, 5)
    saving_text = label_font.render('Save Beat', True, WHITE)
    screen.blit(saving_text, (WIDTH // 2 - 70, HEIGHT * 0.75 + 30))
    
    # Draw a rectangle for typing in the name
    if typing:
        pygame.draw.rect(screen, DARK_GRAY, [400, 200, 600, 200], 0, 5)
    
    entry_rect = pygame.draw.rect(screen, GRAY, [400, 200, 600, 200], 5, 5)
    entry_text = label_font.render(f'{beat_name}', True, WHITE)
    screen.blit(entry_text, (430, 250))
    
    return exit_btn, saving_btn, beat_name, entry_rect

######################################################################################################
# Function to define the 'LOAD' GUI screen
######################################################################################################
def draw_load_menu(index):
    loaded_clicked = []
    loaded_beats = 0
    loaded_bpm = 0
    
    # Draw a rectangle to show the Load menu
    pygame.draw.rect(screen, BLACK, [0, 0, WIDTH, HEIGHT])
    menu_text = label_font.render('LOAD MENU: Select a beat to load in', True, WHITE)
    screen.blit(menu_text, (400, 40))
    
    # Draw a rectangle to close the Load screen
    exit_btn = pygame.draw.rect(screen, GRAY, [WIDTH - 200, HEIGHT - 100, 180, 90], 0, 5)
    exit_text = label_font.render('Close', True, WHITE)
    screen.blit(exit_text, (WIDTH - 160, HEIGHT - 70))
    
    # Draw a button for loading
    loading_btn = pygame.draw.rect(screen, GRAY, [WIDTH // 2 - 100, HEIGHT * 0.87, 200, 100], 0, 5)
    loading_text = label_font.render('Load Beat', True, WHITE)
    screen.blit(loading_text, (WIDTH // 2 - 70, HEIGHT * 0.87 + 30))
    
    # Draw a button for deleting the selected beat-mix
    delete_btn = pygame.draw.rect(screen, GRAY, [WIDTH // 2 - 400, HEIGHT * 0.87, 200, 100], 0, 5)
    delete_text = label_font.render('Delete Beat', True, WHITE)
    screen.blit(delete_text, (WIDTH // 2 - 385, HEIGHT * 0.87 + 30))

    if 0 <= index < len(saved_beats):
        pygame.draw.rect(screen, LIGHT_GRAY, [190, 100 + index*50, 1000, 50])
    
    for beat in range(len(saved_beats)):
        if beat < 10:
            beat_clicked = []
            row_text = medium_font.render(f'{beat + 1}', True, WHITE)
            screen.blit(row_text, (200, 100 + beat * 50))
            
            name_index_start = saved_beats[beat].index('name: ') + 6
            name_index_end = saved_beats[beat].index(', beats:')
            
            name_text = medium_font.render(saved_beats[beat][name_index_start:name_index_end], True, WHITE)
            
            screen.blit(name_text, (240, 100 + beat * 50))
        
        if 0 <= index < len(saved_beats) and beat == index:
            beats_index_end = saved_beats[beat].index(', bpm:')
            loaded_beats = int(saved_beats[beat][name_index_end + 8:beats_index_end])
            
            bpm_index_end = saved_beats[beat].index(', selected:')
            loaded_bpm = int(saved_beats[beat][beats_index_end + 6:bpm_index_end])
            
            loaded_clicks_string = saved_beats[beat][bpm_index_end + 14: -3]
            loaded_clicks_rows = list(loaded_clicks_string.split("], ["))
            
            for row in range(len(loaded_clicks_rows)):
            
                loaded_clicks_row = (loaded_clicks_rows[row].split(', '))
            
                for item in range(len(loaded_clicks_row)):
                    if loaded_clicks_row[item] == '1' or loaded_clicks_row[item] == '-1':
                        loaded_clicks_row[item] = int(loaded_clicks_row[item])
            
                beat_clicked.append(loaded_clicks_row)
                loaded_clicked = beat_clicked
    
    loaded_info = [loaded_beats, loaded_bpm, loaded_clicked]
    entry_rect = pygame.draw.rect(screen, GRAY, [190, 90, 1000, 600], 5, 5)
    
    return exit_btn, loading_btn, entry_rect, delete_btn, loaded_info


# Global variables
freq    = []        # collect all the frequencies
PSD     = []        # Power spectral density

######################################################################################################
# Callback loop for audio processing used for spectrum display
#######################################################################################################

def callback(in_data, frame_count, time_info, status):
    global freq, PSD

    # convert audio stream to correct format
    audio = np.frombuffer(in_data, dtype=np.int16)

    # fft - generate frequency and power spectrum arrays
    freq, PSD = sig.periodogram(audio, sampleRate, nfft=sampleRate/10)

    # return, continue audio processing
    return (in_data, pyaudio.paContinue)

# hide matplotlib toolbar
matplotlib.rcParams['toolbar'] = 'None'

# create a fullscreen black window
fig = plt.figure(figsize = (7, 4))
mng = plt.get_current_fig_manager()
fig.patch.set_facecolor('black')

# number of frequency divisions
numDivs = 80

# generate plot limits and hide axes
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0,1.1), ax.set_xticks([])
ax.set_ylim(-40, 40), ax.set_yticks([])

# audio sampling parameters
chunk       = 256
bandwidth   = 2
channels    = 1
sampleRate  = 44100

# create PyAudio instance
p = pyaudio.PyAudio()

# get connected audio device names
deviceInfo      = p.get_host_api_info_by_index(0)
numDevices      = deviceInfo.get('deviceCount')
inputChannel    = 0

# look for audio mirror named 'Stereo Mix' and save that channel
# Stereo Mix has to be enabled for this to work
for i in range(0,numDevices):
    if 'Stereo Mix' in p.get_device_info_by_host_api_device_index(0, i).get('name'):
        inputChannel = i

# start audio sampling
try:
    stream = p.open(format=p.get_format_from_width(bandwidth),
                    channels=channels,rate=sampleRate,
                    input=True,
                    output=False,
                    input_device_index = 2,
                    frames_per_buffer=chunk,
                    stream_callback=callback)


# quit if Stereo Mix is not available
except:
    print('Error - Enable Stereo Mix')
    quit()

divs = np.zeros(numDivs)

# linear colormap normalized to numDivs
cMap = matplotlib.pyplot.get_cmap('gist_rainbow')
cInd = matplotlib.colors.Normalize(vmin=0, vmax=numDivs)

# create frequency plot using matplotlib lines
waves = []
for i in range(0, numDivs):
    wave, = plt.plot([0.05 + i/numDivs, 0.05 + i/numDivs], [0,0], color=cMap(cInd(i)), linewidth = 3)
    waves.append(wave)

# generate frequency spectrum
freqDivs = []
freqDivs.append([0])
freqDivs.append([1,2])

for i in range(2, numDivs):
    prevLow = freqDivs[i-1][0]
    prevHigh = freqDivs[i-1][1]

    freqDivs.append([prevHigh+1,prevHigh+1+(prevHigh-prevLow)*1.0625])

    # use the full fft spectrum
    if len(freqDivs) == numDivs:
        freqDivs[numDivs-1] = [freqDivs[numDivs-1][0], len(freq)]

# Amplitude array
amp = np.zeros(numDivs)

# Let's begin...
stream.start_stream()

###################################################
# This is the main game loop
###################################################
run = True

while run:
    # Set the ticks as the required frames per second
    timer.tick(fps)

    # Fill the Screen colour as Black
    screen.fill(BLACK)

    # Draw the layout on the MAIN GUI Screen
    boxes = draw_grid(clicked, active_beat, active_list)
    
    ###################################################
    # drawing play_pause button
    play_pause  = pygame.draw.rect(screen, WHITE, [0, 0, 200, 98])

    # Show the pause icon when the music is playing    
    if playing:
        img = pygame.image.load('img\pause.png').convert()
        img = pygame.transform.scale(img, (75, 75))
        play_pause_text  = label_font.render('PAUSE', True, red[0])

    # Show the play icon when the music is not playing
    else:
        img = pygame.image.load('img\play.png').convert()
        img = pygame.transform.scale(img, (75, 75))
        play_pause_text  = label_font.render('PLAY', True, green[0])
        
    # Place the play/pause icon accordingly
    screen.blit(img, (12, 11))
    screen.blit(play_pause_text, (100, 34))
    
    ###################################################
    # Beats per minute GUI menu
    bpm_rect            = pygame.draw.rect(screen, GRAY, [604, 0, 138, 98], 2, 0)

    # Downtempo
    bpm_downtempo       = pygame.draw.rect(screen, GRAY, [202, 0, 200, 32], 2, 5)
    bpm_downtempo_text  = label_font.render('285: Downtempo', True, WHITE)
    screen.blit(bpm_downtempo_text, (210, 2))

    # Hip hop
    bpm_hip_hop         = pygame.draw.rect(screen, GRAY, [202, 33, 200, 32], 2, 5)
    bpm_hip_hop_text    = label_font.render('300: Hip Hop', True, WHITE)
    screen.blit(bpm_hip_hop_text, (210, 36))

    # House
    bpm_house           = pygame.draw.rect(screen, GRAY, [202, 66, 200, 32], 2, 5)
    bpm_house_text      = label_font.render('360: House', True, WHITE)
    screen.blit(bpm_house_text, (210, 70))

    # Techno
    bpm_techno          = pygame.draw.rect(screen, GRAY, [403, 0, 200, 32], 2, 5)
    bpm_techno_text     = label_font.render('390: Techno', True, WHITE)
    screen.blit(bpm_techno_text, (410, 2))

    # Dubstep
    bpm_dubstep         = pygame.draw.rect(screen, GRAY, [403, 33, 200, 32], 2, 5)
    bpm_dubstep_text    = label_font.render('420: Dubstep', True, WHITE)
    screen.blit(bpm_dubstep_text, (410, 36))

    # Juke
    bpm_juke            = pygame.draw.rect(screen, GRAY, [403, 66, 200, 32], 2, 5)
    bpm_juke_text       = label_font.render('480: Juke', True, WHITE)
    screen.blit(bpm_juke_text, (410, 70))

    bpm_text            = label_font.render('BPM: %d'%(bpm), True, red[0])
    screen.blit(bpm_text, (620, 20))

    # Increase the tempo (BPM) in order of +/- 5.
    bpm_add_rect = pygame.draw.rect(screen, GRAY, [630, 50, 35, 35], 0, 5)
    bpm_sub_rect = pygame.draw.rect(screen, GRAY, [672, 50, 35, 35], 0, 5)
    
    add_text = medium_font.render('+5', True, BLACK)
    screen.blit(add_text, (637, 57))
    
    sub_text = medium_font.render('-5', True, BLACK)
    screen.blit(sub_text, (679, 57))
    
    ###################################################
    # Beats per loop GUI buttons
    beats_rect = pygame.draw.rect(screen, GRAY, [744, 0, 154, 98], 2, 0)
    beats_text = label_font.render('#Beats: %d'%(beats), True, WHITE)
    screen.blit(beats_text, (764, 20))
    
    beats_add_rect = pygame.draw.rect(screen, GRAY, [779, 50, 35, 35], 0, 5)
    beats_sub_rect = pygame.draw.rect(screen, GRAY, [821, 50, 35, 35], 0, 5)
    add_text2 = medium_font.render('+1', True, BLACK)
    screen.blit(add_text2, (786, 57))

    sub_text2 = medium_font.render('-1', True, BLACK)
    screen.blit(sub_text2, (828, 57))
    
    ###################################################
    # Clear board GUI button
    clear = pygame.draw.rect(screen, GRAY, [900, 50, 200, 48], 2, 0)
    play_text = label_font.render('Clear Board', True, WHITE)

    img = pygame.image.load('img\clear.png').convert()
    img = pygame.transform.scale(img, (46, 46))
    screen.blit(img, (902, 50))

    screen.blit(play_text, (952, 60))
    
    ###################################################
    # Save buttons
    save_button = pygame.draw.rect(screen, GRAY, [900, 0, 200, 48],2, 0)
    img = pygame.image.load('img\save.png').convert()
    # Scale the image to your needed size
    img = pygame.transform.scale(img, (46, 46))
    screen.blit(img, (902, 2))

    save_text = label_font.render('SAVE', True, WHITE)
    screen.blit(save_text, (952, 10))
    
    ###################################################
    # Load buttons
    load_button = pygame.draw.rect(screen, GRAY, [1102, 0, 300, 98], 2, 0)
    load_text = label_font.render('Your Custom beat', True, WHITE)
    screen.blit(load_text, (1150, 34))

    ###################################################
    # Room Impulse MENU
    room_impulse        = pygame.draw.rect(screen, orange[0], [30, 415, 370, 40], 0, 25)
    room_impulse_text   = label_font.render('Choose a room', True, WHITE)
    screen.blit(room_impulse_text, (125, 420))
    
    auditorium        = pygame.draw.rect(screen, WHITE, [30, 465, 180, 40], 0, 50)
    auditorium_text   = label_font.render('Auditorium', True, orange[0])
    screen.blit(auditorium_text, (50, 470)) 

    hall        = pygame.draw.rect(screen, WHITE, [30, 510, 180, 40], 0, 50)
    hall_text   = label_font.render('Hall', True, orange[0])
    screen.blit(hall_text, (50, 515)) 

    church        = pygame.draw.rect(screen, WHITE, [30, 555, 180, 40], 0, 50)
    church_text   = label_font.render('Church', True, orange[0])
    screen.blit(church_text, (50, 560)) 

    summer_park        = pygame.draw.rect(screen, WHITE, [30, 600, 180, 40], 0, 50)
    summer_park_text   = label_font.render('Summer_park', True, orange[0])
    screen.blit(summer_park_text, (50, 605))

    stairway        = pygame.draw.rect(screen, WHITE, [30, 645, 180, 40], 0, 50)
    stairway_text   = label_font.render('Stairway', True, orange[0])
    screen.blit(stairway_text, (50, 650))

    factory        = pygame.draw.rect(screen, WHITE, [30, 690, 180, 40], 0, 50)
    factory_text   = label_font.render('Factory', True, orange[0])
    screen.blit(factory_text, (50, 695))

    dungeon        = pygame.draw.rect(screen, WHITE, [220, 465, 180, 40], 0, 50)
    dungeon_text   = label_font.render('Dungeon', True, orange[0])
    screen.blit(dungeon_text, (240, 470)) 

    kiln        = pygame.draw.rect(screen, WHITE, [220, 510, 180, 40], 0, 50)
    kiln_text   = label_font.render('Kiln', True, orange[0])
    screen.blit(kiln_text, (240, 515)) 

    tunnel        = pygame.draw.rect(screen, WHITE, [220, 555, 180, 40], 0, 50)
    tunnel_text   = label_font.render('Tunnel', True, orange[0])
    screen.blit(tunnel_text, (240, 560)) 

    winter_park        = pygame.draw.rect(screen, WHITE, [220, 600, 180, 40], 0, 50)
    winter_park_text   = label_font.render('Winter_park', True, orange[0])
    screen.blit(winter_park_text, (240, 605)) 

    studio        = pygame.draw.rect(screen, WHITE, [220, 645, 180, 40], 0, 50)
    studio_text   = label_font.render('Studio', True, orange[0])
    screen.blit(studio_text, (240, 650))

    chamber        = pygame.draw.rect(screen, WHITE, [220, 690, 180, 40], 0, 50)
    chamber_text   = label_font.render('Chamber', True, orange[0])
    screen.blit(chamber_text, (240, 695))

    original        = pygame.draw.rect(screen, WHITE, [115, 735, 180, 40], 0, 50)
    original_text   = label_font.render('Original', True, orange[0])
    screen.blit(original_text, (150, 740))

    ###################################################
    # Stereo Controls
    left_vol_div    = pygame.draw.rect(screen, GRAY, [420, 405, 95, 390])
    center_vol_div  = pygame.draw.rect(screen, GRAY, [520, 405, 80, 390])
    right_vol_div   = pygame.draw.rect(screen, GRAY, [605, 405, 95, 390])

    volume_rect     = pygame.draw.rect(screen, BLACK, [420, 405, 280, 390])

    img = pygame.image.load('img\speaker.png').convert()
    img = pygame.transform.scale(img, (280, 280))
    screen.blit(img, (420, 440))
    
    ###################################################
    # instrument rectangles
    instrument_rects = []
    for i in range(len(instruments)):
        rect = pygame.rect.Rect((0, 100 + i * 50), (100, 50))
        instrument_rects.append(rect)

    ###################################################
    # Play the notes if the beat change request is made   
    if beat_changed:
        play_notes(room)
        beat_changed = False

    ###################################################
    # Draw the 'Load' menu screen when requested
    if load_menu:
        exit_button, loading_button, entry_rect, delete_button, loaded_information = draw_load_menu(index)

    ###################################################
    # Draw the 'Save' menu screen when requested
    elif save_menu:
        playing = False
        exit_button, saving_button, beat_name, entry_rect = draw_save_menu(beat_name, typing)
    
    ###################################################
    # Check for pygame events (such as key presses)
    for event in pygame.event.get():
        
        # 'QUIT' when requested
        if event.type == pygame.QUIT:
            run = False

        # Activate the controls on the main screen is clicked: 'MOUSE_DOWN'
        if event.type == pygame.MOUSEBUTTONDOWN and not save_menu and not load_menu:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
        
        # Initate the control action at the 'MOUSE_UP'
        if event.type == pygame.MOUSEBUTTONUP and not save_menu and not load_menu:
            
            # Play/Pause button is clicked
            if play_pause.collidepoint(event.pos) and playing:
                playing = False
            elif play_pause.collidepoint(event.pos) and not playing:
                playing = True
                active_beat = 0
                active_length = 0
            
            # Request to add/remove beats in the loop
            if beats_add_rect.collidepoint(event.pos):
                beats += 1
                for i in range(len(clicked)):   clicked[i].append(-1)
            elif beats_sub_rect.collidepoint(event.pos):
                beats -= 1
                for i in range(len(clicked)):   clicked[i].pop(-1)

            # Request to increment/decrement the tempo(BPM)
            if bpm_add_rect.collidepoint(event.pos):    bpm     += 5
            elif bpm_sub_rect.collidepoint(event.pos):  bpm     -= 5
            elif bpm_downtempo.collidepoint(event.pos): bpm     = 285
            elif bpm_hip_hop.collidepoint(event.pos):   bpm     = 300
            elif bpm_house.collidepoint(event.pos):     bpm     = 360
            elif bpm_techno.collidepoint(event.pos):    bpm     = 390
            elif bpm_dubstep.collidepoint(event.pos):   bpm     = 420
            elif bpm_juke.collidepoint(event.pos):      bpm     = 480

            # Request to activate the room Impulse
            if auditorium.collidepoint(event.pos):      room    = 'auditorium'
            elif hall.collidepoint(event.pos):          room    = 'hall'
            elif church.collidepoint(event.pos):        room    = 'church'
            elif summer_park.collidepoint(event.pos):   room    = 'summer_park'
            elif stairway.collidepoint(event.pos):      room    = 'stairway'
            elif factory.collidepoint(event.pos):       room    = 'factory'
            elif dungeon.collidepoint(event.pos):       room    = 'dungeon'
            elif kiln.collidepoint(event.pos):          room    = 'kiln'
            elif tunnel.collidepoint(event.pos):        room    = 'tunnel'
            elif winter_park.collidepoint(event.pos):   room    = 'winter_park'
            elif studio.collidepoint(event.pos):        room    = 'studio'
            elif chamber.collidepoint(event.pos):       room    = 'chamber'
            elif original.collidepoint(event.pos):      room    = 'original'
            
            # Request to clear the board: deactivate the entire grid
            if clear.collidepoint(event.pos):
                clicked = [[-1 for _ in range(beats)] for _ in range(len(instruments))]

            # Activate/De-activate the selected beat 
            for i in range(len(instrument_rects)):
                if instrument_rects[i].collidepoint(event.pos):
                    active_list[i] *= -1

            # Activate the save menu screen when clicked
            if save_button.collidepoint(event.pos):
                save_menu = True

            # Activate the load menu screen when clicked
            if load_button.collidepoint(event.pos):
                load_menu = True
                playing = False
            
            # Activate both the speakers when clicked on the center speaker icon
            if center_vol_div.collidepoint(event.pos):
                left_vol    = 1.0
                right_vol   = 1.0
            
            # Activate only the left speaker when clicked on the left speaker icon
            elif left_vol_div.collidepoint(event.pos):
                left_vol    = 1.0
                right_vol   = 0.0
            
            # Activate only the right speaker when clicked on the right speaker icon
            elif right_vol_div.collidepoint(event.pos):
                left_vol    = 0.0
                right_vol   = 1.0

        
        elif event.type == pygame.MOUSEBUTTONUP:
            
            # Request to exit
            if exit_button.collidepoint(event.pos):
                save_menu = False
                load_menu = False
                playing = True
                typing = False
                beat_name = ''
            
            # Request to save/load
            if entry_rect.collidepoint(event.pos):
                if save_menu:
                    if typing:
                        typing = False
                    else:
                        typing = True
                if load_menu:
                    index = (event.pos[1] - 100) // 50

            # Request to Save the beat parameters
            if save_menu:
                if saving_button.collidepoint(event.pos):
                    file = open('saved_beats.txt', 'w')
                    saved_beats.append(f'\nname: {beat_name}, beats: {beats}, bpm: {bpm}, selected: {clicked}')
                    for i in range(len(saved_beats)):
                        file.write(str(saved_beats[i]))
                    file.close()
                    save_menu = False
                    load_menu = False
                    playing = True
                    typing = False
                    beat_name = ''

            # Request to load and/or delete 
            if load_menu:
                if delete_button.collidepoint(event.pos):
                    if 0 <= index < len(saved_beats):
                        saved_beats.pop(index)
                if loading_button.collidepoint(event.pos):
                    if 0 <= index < len(saved_beats):
                        beats = loaded_information[0]
                        bpm = loaded_information[1]
                        clicked = loaded_information[2]
                        index = 100
                        save_menu = False
                        load_menu = False
                        playing = True
                        typing = False

        # Save the typed in name
        if event.type == pygame.TEXTINPUT and typing:
            beat_name += event.text

        # While typing the name
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(beat_name) > 0:
                beat_name = beat_name[:-1]

    # Tempo
    beat_length = 1800 // bpm

    ###################################################
    # When playing
    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True  
        
        ###################################################
        # Take PSD data and create amplitude values for the frequency plot
        divs[0] = PSD[0]**0.5
        waves[0].set_ydata([-divs[0],divs[0]])

        for i in range(1, numDivs):
            
            # square-root of the average 'volume' for each frequency range
            divs[i] = np.average(PSD[int(freqDivs[i][0]):int(freqDivs[i][1])])**0.5

            # instant growth, proportional decay
            if divs[i] > amp[i]: 
                amp[i] = divs[i]
                
            elif divs[i] < amp[i]: 
                amp[i] = amp[i]-(amp[i]-divs[i])/1.8

            waves[i].set_ydata([-amp[i],amp[i]])

        # update figure canvas
        fig.canvas.draw()

        # Get the RGBA buffer from the figure and blit it to the Pygame surface
        buf = fig.canvas.tostring_argb()
        plot_surface = pygame.image.fromstring(buf, fig.canvas.get_width_height(), 'ARGB')

        # Draw the plot surface to the screen
        screen.blit(plot_surface, (700, 400))

    ###################################################
    # Update the Screen for the current iteration
    pygame.display.flip()

###################################################
# Write and save the beats to a text file
file = open('saved_beats.txt', 'w')

for i in range(len(saved_beats)):
    file.write(str(saved_beats[i]))

file.close()

###################################################
# stop audio stream and quit the pygame
print('stream closed')

stream.stop_stream()
stream.close()
p.terminate()
pygame.quit()



