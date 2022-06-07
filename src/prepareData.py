
sourceFilename = r'C:\FER\10. semestar\Diplomski rad\community-detection\SNAP_data\twitch.txt'
destFilename = r'C:\FER\10. semestar\Diplomski rad\community-detection\SNAP_data\twitchReady.txt'

source = open(sourceFilename, 'r')
destination = open(destFilename, 'w')

for line in source.readlines():
    line = line.replace(",", " ")
    destination.write(line)