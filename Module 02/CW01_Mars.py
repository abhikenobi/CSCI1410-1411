# speed of light = 186,000 miles/second
# closest distance between Mars and Earth = 34 million miles

# calculate how long it will take for Mars rover to send photos to Nasa at speed of light
# when Mars is closest to Earth

def main():

    #initial variables
    lightspeed = 186000
    distance = 34000000

    #calculation
    time_seconds = distance/lightspeed

    #display results
    print(f"It takes {time_seconds} seconds for Curiosity to send photos to NASA")

    # converting time into min/seconds
    time_min = time_seconds // 60
    remainder_seconds = time_seconds % 60

    print(f"{time_min} minutes and {remainder_seconds} seconds to be exact.")

main()
