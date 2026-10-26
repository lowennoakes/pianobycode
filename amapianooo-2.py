
 from earsketch import *

setTempo(113)

# ============================================================
# AMAPIANO TRACK - 113 BPM
#
# 1-6   Intro
# 6-13  Groove
# 13-17 Build
# 17-25 Drop 1
# 25-29 Breakdown
# 29-37 Drop 2
# 37-41 Outro
# ============================================================


# ============================================================
# TRACK 1 - THOKOZANI
# MAIN MUSICAL LOOP
# ============================================================

fitMedia(LOWENNOAKES_AFROBEAT_PRODUCERS_THOKOZANI_EMIN_113BPM, 1, 1, 41)

#Slow fade into song
setEffect(1, VOLUME, GAIN, -30, 1, -7, 4)

#Main level
setEffect(1, VOLUME, GAIN, -7, 4, -6, 13)

#Pull back slightly for build
setEffect(1, VOLUME, GAIN, -6, 13, -9, 16)

#Return for first drop
setEffect(1, VOLUME, GAIN, -9, 16, -5, 18)

#Fade into breakdown
setEffect(1, VOLUME, GAIN, -5, 23, -16, 26)

#Build back
setEffect(1, VOLUME, GAIN, -16, 27, -6, 30)

#Second drop
setEffect(1, VOLUME, GAIN, -6, 30, -5, 35)

#Outro
setEffect(1, VOLUME, GAIN, -5, 37, -35, 41)

setEffect(1, DELAY, DELAY_TIME, 100)


# ============================================================
# TRACK 2 - TEMPELA
# SECONDARY E MINOR TEXTURE
# ============================================================

fitMedia(LOWENNOAKES_AFROBEAT_PRODUCERS_TEMPELA_EMIN_110BPM, 2, 21, 33)

#Slowly enter close to the end of Drop 1
setEffect(2, VOLUME, GAIN, -35, 21, -15, 24)

# Take over during breakdown
setEffect(2, VOLUME, GAIN, -15, 24, -7, 26)

# Stay soft in the background
setEffect(2, VOLUME, GAIN, -7, 26, -8, 28)

# Fade whhen the second drop starts
setEffect(2, VOLUME, GAIN, -8, 28, -35, 32)

setEffect(2, DELAY, DELAY_TIME, 120)


# ============================================================
# TRACK 3 - 3 STEP SHAKER
# QUIET / BACKGROUND
# ============================================================

fitMedia(LOWENNOAKES_SCOVINIEBEATZ_SCOVINIEBEATZ_3_STEP_SHAKER_1_539505, 3, 6, 24)
fitMedia(LOWENNOAKES_SCOVINIEBEATZ_SCOVINIEBEATZ_3_STEP_SHAKER_1_539505, 3, 29, 37)

# gentle entrance
setEffect(3, VOLUME, GAIN, -35, 6, -18, 10)

# keep very quiet
setEffect(3, VOLUME, GAIN, -18, 10, -15, 16)

# Small lift for drop
setEffect(3, VOLUME, GAIN, -15, 16, -13, 19)

# fadeaway
setEffect(3, VOLUME, GAIN, -13, 21, -35, 24)

# Second drop
setEffect(3, VOLUME, GAIN, -35, 29, -16, 31)

setEffect(3, VOLUME, GAIN, -16, 31, -14, 34)

# Exit early so outro has space
setEffect(3, VOLUME, GAIN, -14, 34, -35, 37)


# ============================================================
# TRACK 4 - RED EYE PERCUSSION
# VERY LIGHT PERCUSSION
# ============================================================

fitMedia(LOWENNOAKES_AFROBEAT_PRODUCERS_PERC_LOOP_RED_EYE_115BPM, 4, 9, 17)
fitMedia(LOWENNOAKES_AFROBEAT_PRODUCERS_PERC_LOOP_RED_EYE_115BPM, 4, 30, 36)

# First appearance
setEffect(4, VOLUME, GAIN, -35, 9, -20, 12)

setEffect(4, VOLUME, GAIN, -20, 12, -17, 15)

setEffect(4, VOLUME, GAIN, -17, 15, -35, 17)

# Second appearance
setEffect(4, VOLUME, GAIN, -35, 30, -19, 32)

setEffect(4, VOLUME, GAIN, -19, 32, -17, 34)

setEffect(4, VOLUME, GAIN, -17, 34, -35, 36)


# ============================================================
# TRACK 5 - BULLY PERCUSSION
# SMALL PERCUSSION ACCENTS
# ============================================================
LOWENNOAKES_SCOVINIEBEATZ_SCOVINIEBEATZ_3_STEP_SHAKER_1_539505
LOWENNOAKES_AMAPIANO_PERCS_110BPM_E_MINOR
LOWENNOAKES_AMAPIANO_DRY_BASS_A_MINOR
fitMedia(LOWENNOAKES_AFROBEAT_PRODUCERS_PERC_LOOP_BULLY_115BPM, 5, 14, 18)
fitMedia(LOWENNOAKES_AFROBEAT_PRODUCERS_PERC_LOOP_BULLY_115BPM, 5, 32, 36)

# Build 1
setEffect(5, VOLUME, GAIN, -35, 14, -20, 16)

setEffect(5, VOLUME, GAIN, -20, 16, -17, 17)

setEffect(5, VOLUME, GAIN, -17, 17, -35, 18)

# Drop 2 accent
setEffect(5, VOLUME, GAIN, -35, 32, -19, 34)

setEffect(5, VOLUME, GAIN, -19, 34, -35, 36)


# ============================================================
# TRACK 6 - BANNY AMAPIANO BASE
# BASS FOUNDATION
# ============================================================

fitMedia(LOWENNOAKES_BANNYFERNANDES77_AMAPIANO_LOOP_BASE_BANNY_FERNANDES_297939, 6, 10, 25)
fitMedia(LOWENNOAKES_BANNYFERNANDES77_AMAPIANO_LOOP_BASE_BANNY_FERNANDES_297939, 6, 28, 38)

# Slow introduction of bass
setEffect(6, VOLUME, GAIN, -35, 10, -15, 13)

# Build toward first drop
setEffect(6, VOLUME, GAIN, -15, 13, -8, 16)

# Drop
setEffect(6, VOLUME, GAIN, -8, 16, -4, 18)

# Hold
setEffect(6, VOLUME, GAIN, -4, 18, -4, 22)

# remove bass for breakdown
setEffect(6, VOLUME, GAIN, -4, 22, -35, 25)

# slow tease of bass before drop 2
setEffect(6, VOLUME, GAIN, -35, 28, -10, 29)

# Drop 2
setEffect(6, VOLUME, GAIN, -10, 29, -3, 31)

# Hold
setEffect(6, VOLUME, GAIN, -3, 31, -3, 35)

# Fade out
setEffect(6, VOLUME, GAIN, -3, 35, -35, 38)


# ============================================================
# TRACK 7 - CORIGATED LOG
# FIRST LOG DRUM
# DROP 1 ONLY
# ============================================================

fitMedia(LOWENNOAKES_DRIVATEMXI_CORIGATED_LOG_1_350577, 7, 16, 25)

# Tease log drum
setEffect(7, VOLUME, GAIN, -35, 16, -10, 17)

# Drop!
setEffect(7, VOLUME, GAIN, -10, 17, -3, 18)

# Main log drum level
setEffect(7, VOLUME, GAIN, -3, 18, -3, 22)

# Smoothly remove it
setEffect(7, VOLUME, GAIN, -3, 22, -35, 25)


# ============================================================
# TRACK 8 - SAUCE LOGDRUM
# SECOND LOG DRUM
# DROP 2 ONLY
# ============================================================

fitMedia(LOWENNOAKES_SCOVINIEBEATZ_SAUCE_LOGDRUM_3_431879, 8, 28, 38)

# Quiet preview before drop
setEffect(8, VOLUME, GAIN, -35, 28, -12, 29)

# Drop 2
setEffect(8, VOLUME, GAIN, -12, 29, -2, 30)

# Main level
setEffect(8, VOLUME, GAIN, -2, 30, -2, 35)

# Gradually disappear
setEffect(8, VOLUME, GAIN, -2, 35, -35, 38)


# ============================================================
# TRACK 9 - AMAPIANO FX
# TRANSITIONS
# ============================================================

# FX before first drop
fitMedia(LOWENNOAKES_SCOVINIEBEATZ_AMAPIANO_FX_3_SCOVINIEBEATZ_432582, 9, 15, 17)

# FX before second drop
fitMedia(LOWENNOAKES_SCOVINIEBEATZ_AMAPIANO_FX_3_SCOVINIEBEATZ_432582, 9, 27, 29)

# Keep FX at a controlled level
setEffect(9, VOLUME, GAIN, -10)

## ------------------------------------------------------------
# TRACK 10 - WHISTLE FX
# Rare accent - stands out when it appears
# ------------------------------------------------------------

# First whistle introduces the main groove
fitMedia(
    LOWENNOAKES_AMAPIANO_WHISTLE_FX,
    10, 16, 17
)

# Second whistle  late-song accent
fitMedia(
    LOWENNOAKES_AMAPIANO_WHISTLE_FX,
    10, 32, 33
)

# Keep first whistle slightly further back in the composition
setEffect(
    10, VOLUME, GAIN,
    -18, 16,
    -11, 16.5
)

setEffect(
    10, VOLUME, GAIN,
    -11, 16.5,
    -20, 17
)

# Second whistle stands out more, slightly louder
setEffect(
    10, VOLUME, GAIN,
    -16, 32,
    -8, 32.5
)

setEffect(
    10, VOLUME, GAIN,
    -8, 32.5,
    -20, 33
)


# ============================================================
# AMAPIANO VOCAL ARRANGEMENT
# Tracks 11 - 14
# ============================================================

# TRACK 11 - TEMPELA
# Atmospheric opening - measures 5 to 13

fitMedia(
    LOWENNOAKES_AFROBEAT_PRODUCERS_TEMPELA_EMIN_110BPM,
    11, 5, 13
)

# Slow fade in across 2 measures
setEffect(11, VOLUME, GAIN, -35, 5, -14, 7)

# Hold vocal
setEffect(11, VOLUME, GAIN, -14, 7, -14, 10)

# Long fade out
setEffect(11, VOLUME, GAIN, -14, 10, -40, 13)


# TRACK 12 - LOCATION
# Main recurring vocal hook
# Measures 13-21 and 25-33

fitMedia(
    LOWENNOAKES_EMP_CMACV1_LOCATION_05_WET_FMIN_124BPM_66,
    12, 13, 21
)

fitMedia(
    LOWENNOAKES_EMP_CMACV1_LOCATION_05_WET_FMIN_124BPM_66,
    12, 25, 33
)

# First appearance
setEffect(12, VOLUME, GAIN, -35, 13, -11, 15)
setEffect(12, VOLUME, GAIN, -11, 15, -11, 18)
setEffect(12, VOLUME, GAIN, -11, 18, -40, 21)

# Second appearance
setEffect(12, VOLUME, GAIN, -35, 25, -9, 27)
setEffect(12, VOLUME, GAIN, -9, 27, -9, 30)
setEffect(12, VOLUME, GAIN, -9, 30, -40, 33)
